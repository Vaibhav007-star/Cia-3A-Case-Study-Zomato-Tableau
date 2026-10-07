"""
Zomato Exploratory Data Analysis & Statistical Validation Script
Extracts concrete metrics, distributions, and cross-tabulations.
"""

import pandas as pd
import numpy as np

def run_eda():
    df = pd.read_csv("data/processed/zomato_ncr_clean.csv")
    print("=" * 65)
    print("EXPLORATORY DATA ANALYSIS: DELHI-NCR SUBSET (N = 7,947)")
    print("=" * 65)

    # 1. Overall Summary
    print("\n--- 1. OVERALL METRIC DISTRIBUTIONS ---")
    rated_df = df[df['Is_Rated'] == 1]
    print(f"Total Restaurants: {len(df)}")
    print(f"Rated Restaurants: {len(rated_df)} ({len(rated_df)/len(df)*100:.2f}%)")
    print(f"Unrated Restaurants: {len(df)-len(rated_df)} ({(len(df)-len(rated_df))/len(df)*100:.2f}%)")

    print("\n[Average Cost for Two (INR)]")
    print(df['Average_Cost_Clean'].describe(percentiles=[0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]))

    print("\n[Aggregate Rating (Rated Venues Only)]")
    print(rated_df['Aggregate_Rating'].describe())

    print("\n[Votes Distribution (All Venues)]")
    print(df['Votes'].describe(percentiles=[0.25, 0.50, 0.75, 0.90, 0.95, 0.99]))

    # 2. Service Profiles Breakdown
    print("\n--- 2. SERVICE AVAILABILITY BREAKDOWN ---")
    print(df['Service_Profile'].value_counts())
    print("\nPercentages:")
    print(df['Service_Profile'].value_counts(normalize=True)*100)

    # 3. Cost vs Rating Correlation
    print("\n--- 3. CORRELATION ANALYSIS (RATED VENUES) ---")
    corr_cols = ['Aggregate_Rating', 'Votes', 'Log_Votes', 'Average_Cost_Clean', 'Price_Range', 'Cuisine_Count']
    corr_matrix = rated_df[corr_cols].corr()
    print(corr_matrix.round(3))

    # 4. Strategic Restaurant Segmentation Matrix
    print("\n--- 4. RESTAURANT SEGMENTATION MATRIX (DELHI-NCR) ---")
    seg_summary = df.groupby('Restaurant_Segment').agg(
        Count=('Restaurant_ID', 'count'),
        Mean_Rating=('Aggregate_Rating', lambda x: x[x > 0].mean()),
        Median_Votes=('Votes', 'median'),
        Mean_Votes=('Votes', 'mean'),
        Median_Cost=('Average_Cost_Clean', 'median'),
        Mean_Cost=('Average_Cost_Clean', 'mean'),
        Pct_Delivery=('Has_Online_Delivery', lambda x: (x == 'Yes').mean() * 100),
        Pct_TableBooking=('Has_Table_Booking', lambda x: (x == 'Yes').mean() * 100)
    ).reset_index()
    seg_summary['Pct_Total'] = (seg_summary['Count'] / len(df)) * 100
    print(seg_summary.to_string(index=False))

    # 5. Top 10 Localities with Highest Concentration of Hidden Gems
    print("\n--- 5. TOP LOCALITIES BY HIDDEN GEM CONCENTRATION ---")
    hg_df = df[df['Restaurant_Segment'] == 'Hidden Gem']
    locality_hg = hg_df.groupby('Locality').agg(
        Hidden_Gems=('Restaurant_ID', 'count'),
        Avg_Rating=('Aggregate_Rating', 'mean'),
        Avg_Cost=('Average_Cost_Clean', 'mean')
    ).sort_values(by='Hidden_Gems', ascending=False).head(10)
    print(locality_hg)

    # 6. Online Delivery vs Ratings & Cost
    print("\n--- 6. ONLINE DELIVERY COMPARATIVE ANALYSIS ---")
    deliv_comp = rated_df.groupby('Has_Online_Delivery').agg(
        Count=('Restaurant_ID', 'count'),
        Avg_Rating=('Aggregate_Rating', 'mean'),
        Median_Rating=('Aggregate_Rating', 'median'),
        Median_Cost=('Average_Cost_Clean', 'median'),
        Mean_Cost=('Average_Cost_Clean', 'mean'),
        Median_Votes=('Votes', 'median')
    )
    print(deliv_comp)

    # 7. Price Tier Performance
    print("\n--- 7. PRICE TIER PROFILES ---")
    pt_comp = df.groupby('Price_Tier').agg(
        Count=('Restaurant_ID', 'count'),
        Pct_Total=('Restaurant_ID', lambda x: len(x)/len(df)*100),
        Avg_Rating=('Aggregate_Rating', lambda x: x[x>0].mean()),
        Median_Cost=('Average_Cost_Clean', 'median'),
        Median_Votes=('Votes', 'median'),
        Pct_Delivery=('Has_Online_Delivery', lambda x: (x == 'Yes').mean() * 100)
    ).reindex(['Budget (Tier 1)', 'Moderate (Tier 2)', 'Upscale (Tier 3)', 'Fine Dining (Tier 4)'])
    print(pt_comp)

if __name__ == "__main__":
    run_eda()

