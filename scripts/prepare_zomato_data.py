"""
Zomato Data Preparation & Exploratory Pipeline
Reproducible preprocessing script for Tableau Public integration.
Author: Antigravity & Vaibhav (B.Sc Data Science & AI Case Study)
"""

import os
import numpy as np
import pandas as pd

def run_pipeline():
    print("=" * 70)
    print("STARTING DATA PREPARATION & CLEANING PIPELINE")
    print("=" * 70)

    # 1. Load Raw Dataset
    raw_path = "raw_data/zomato_raw.csv"
    country_path = "raw_data/Country-Code.xlsx"
    
    print(f"[Step 1] Loading raw dataset: {raw_path}")
    try:
        df = pd.read_csv(raw_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(raw_path, encoding='latin-1')
    
    print(f"Loaded raw records: {df.shape[0]} rows, {df.shape[1]} columns")

    # Load country mapping
    country_df = pd.read_excel(country_path)
    df = df.merge(country_df, on="Country Code", how="left")
    print(f"Merged Country Code. Countries mapped: {df['Country'].nunique()}")

    # 2. Text standardization & whitespace trimming
    text_cols = ['Restaurant Name', 'City', 'Locality', 'Locality Verbose', 'Address', 'Cuisines', 'Currency']
    for c in text_cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()

    # 3. Handle Missing Cuisines
    null_cuisines = df['Cuisines'].isna() | (df['Cuisines'] == 'nan')
    print(f"[Step 2] Found {null_cuisines.sum()} missing cuisine entries. Imputing with 'Not Specified'")
    df.loc[null_cuisines, 'Cuisines'] = 'Not Specified'

    # Extract Primary Cuisine and Cuisine Count
    df['Primary_Cuisine'] = df['Cuisines'].apply(lambda x: x.split(',')[0].strip() if x != 'Not Specified' else 'Not Specified')
    df['Cuisine_Count'] = df['Cuisines'].apply(lambda x: len(x.split(',')) if x != 'Not Specified' else 0)

    # 4. Handle Cost Zero Values & Outliers
    df['Average_Cost_Raw'] = df['Average Cost for two']
    zero_cost_mask = df['Average Cost for two'] == 0
    print(f"[Step 3] Found {zero_cost_mask.sum()} zero-cost entries.")

    # Impute zero costs using City & Price Range median cost
    df['Average_Cost_Clean'] = df['Average Cost for two'].astype(float)
    for (city, pr), group in df[~zero_cost_mask].groupby(['City', 'Price range']):
        median_val = group['Average Cost for two'].median()
        idx_to_fill = df[(df['City'] == city) & (df['Price range'] == pr) & zero_cost_mask].index
        if len(idx_to_fill) > 0 and not np.isnan(median_val):
            df.loc[idx_to_fill, 'Average_Cost_Clean'] = median_val

    # Fallback to Country & Price Range median for any remaining
    remaining_zero = df['Average_Cost_Clean'] == 0
    if remaining_zero.sum() > 0:
        for (country, pr), group in df[~remaining_zero].groupby(['Country', 'Price range']):
            median_val = group['Average_Cost_Clean'].median()
            idx_to_fill = df[(df['Country'] == country) & (df['Price range'] == pr) & remaining_zero].index
            if len(idx_to_fill) > 0 and not np.isnan(median_val):
                df.loc[idx_to_fill, 'Average_Cost_Clean'] = median_val

    print(f"Remaining zero-cost entries after tiered median imputation: {(df['Average_Cost_Clean'] == 0).sum()}")

    # 5. Rating Status & Cold-Start Isolation
    df['Is_Rated'] = (df['Aggregate rating'] > 0.0).astype(int)
    df['Rating_Status'] = df['Is_Rated'].map({1: 'Rated', 0: 'Unrated / New Entrant'})
    print(f"[Step 4] Rating distribution: {df['Rating_Status'].value_counts().to_dict()}")

    # 6. Normalization & Logarithmic Engagement Transformation
    # Max votes across dataset
    max_votes = df['Votes'].max()
    max_log_votes = np.log(1 + max_votes)

    df['Log_Votes'] = np.log(1 + df['Votes'])
    # Scaled to 0-100
    df['Normalized_Rating_Score'] = (df['Aggregate rating'] / 5.0) * 100.0
    df['Normalized_Engagement_Score'] = (df['Log_Votes'] / max_log_votes) * 100.0

    # Round normalized scores
    df['Normalized_Rating_Score'] = df['Normalized_Rating_Score'].round(2)
    df['Normalized_Engagement_Score'] = df['Normalized_Engagement_Score'].round(2)

    # 7. Operational Service Profiling
    def categorize_service(row):
        table = (row['Has Table booking'].strip().lower() == 'yes')
        online = (row['Has Online delivery'].strip().lower() == 'yes')
        if table and online:
            return 'Both (Delivery & Booking)'
        elif online and not table:
            return 'Online Delivery Only'
        elif table and not online:
            return 'Table Booking Only'
        else:
            return 'Dine-in Only'

    df['Service_Profile'] = df.apply(categorize_service, axis=1)

    # 8. Price Tier Categorization
    price_tier_map = {
        1: 'Budget (Tier 1)',
        2: 'Moderate (Tier 2)',
        3: 'Upscale (Tier 3)',
        4: 'Fine Dining (Tier 4)'
    }
    df['Price_Tier'] = df['Price range'].map(price_tier_map)

    # 9. Coordinate Validation Flag
    df['Has_Valid_Coordinates'] = ~((df['Longitude'] == 0.0) & (df['Latitude'] == 0.0))
    print(f"[Step 5] Coordinate audit: {df['Has_Valid_Coordinates'].value_counts().to_dict()}")

    # 10. Strategic Restaurant Segmentation Matrix (Lab 7.2 LOD alignment)
    def assign_segment(row):
        if row['Is_Rated'] == 0:
            return 'Unrated / New Entrant'
        rating = row['Aggregate rating']
        votes = row['Votes']
        if rating >= 4.0:
            if votes >= 200:
                return 'Market Leader'
            else:
                return 'Hidden Gem'
        elif 3.0 <= rating < 4.0:
            if votes >= 200:
                return 'Popular Volume Driver'
            else:
                return 'Average Performer'
        else:  # rating < 3.0
            return 'Underperforming'

    df['Restaurant_Segment'] = df.apply(assign_segment, axis=1)
    print(f"[Step 6] Segmentation Matrix:\n{df['Restaurant_Segment'].value_counts()}")

    # 11. Rename columns cleanly for Tableau compatibility
    tableau_col_rename = {
        'Restaurant ID': 'Restaurant_ID',
        'Restaurant Name': 'Restaurant_Name',
        'Country Code': 'Country_Code',
        'Has Table booking': 'Has_Table_Booking',
        'Has Online delivery': 'Has_Online_Delivery',
        'Is delivering now': 'Is_Delivering_Now',
        'Price range': 'Price_Range',
        'Aggregate rating': 'Aggregate_Rating',
        'Rating color': 'Rating_Color',
        'Rating text': 'Rating_Text'
    }
    df = df.rename(columns=tableau_col_rename)

    # 12. Create destination directories
    os.makedirs("data/processed", exist_ok=True)

    # Export Global Clean
    global_export_path = "data/processed/zomato_global_clean.csv"
    df.to_csv(global_export_path, index=False)
    print(f"\n[Step 7] Exported Global Cleaned Dataset: {global_export_path} ({df.shape[0]} rows)")

    # Export India Clean (Country_Code == 1)
    df_india = df[df['Country_Code'] == 1].copy()
    india_export_path = "data/processed/zomato_india_clean.csv"
    df_india.to_csv(india_export_path, index=False)
    print(f"Exported India Cleaned Dataset: {india_export_path} ({df_india.shape[0]} rows)")

    # Export Delhi-NCR Clean (New Delhi, Gurgaon, Noida, Faridabad, Ghaziabad)
    ncr_cities = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad']
    df_ncr = df_india[df_india['City'].isin(ncr_cities)].copy()
    ncr_export_path = "data/processed/zomato_ncr_clean.csv"
    df_ncr.to_csv(ncr_export_path, index=False)
    print(f"Exported Delhi-NCR Cleaned Dataset: {ncr_export_path} ({df_ncr.shape[0]} rows)")

    # Export Exploded Cuisines Table for NCR (Relational bridge for Tableau multi-cuisine exploration)
    cuisine_records = []
    for _, row in df_ncr.iterrows():
        rid = row['Restaurant_ID']
        cuisines_str = row['Cuisines']
        if cuisines_str != 'Not Specified':
            for c in cuisines_str.split(','):
                cuisine_records.append({'Restaurant_ID': rid, 'Cuisine': c.strip()})
        else:
            cuisine_records.append({'Restaurant_ID': rid, 'Cuisine': 'Not Specified'})
    df_cuisines = pd.DataFrame(cuisine_records)
    cuisines_export_path = "data/processed/zomato_ncr_cuisines.csv"
    df_cuisines.to_csv(cuisines_export_path, index=False)
    print(f"Exported NCR Cuisines Bridge Dataset: {cuisines_export_path} ({df_cuisines.shape[0]} rows)")

    # Update root convenience copies for immediate Tableau access
    df.to_csv("zomato_cleaned.csv", index=False)
    df_india.to_csv("zomato_india_cleaned.csv", index=False)

    print("\n" + "=" * 70)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    run_pipeline()

