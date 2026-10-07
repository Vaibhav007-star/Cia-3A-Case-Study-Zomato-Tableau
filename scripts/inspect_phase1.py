import pandas as pd
import numpy as np

# Load raw dataset
try:
    df_raw = pd.read_csv('raw_data/zomato_raw.csv', encoding='utf-8')
except UnicodeDecodeError:
    df_raw = pd.read_csv('raw_data/zomato_raw.csv', encoding='latin-1')

print("=" * 60)
print("1. BASIC DATASET DIMENSIONS")
print(f"Total Rows: {df_raw.shape[0]}")
print(f"Total Columns: {df_raw.shape[1]}")

print("\n" + "=" * 60)
print("2. COLUMN DETAILS, DATA TYPES & MISSING VALUES")
summary_list = []
for col in df_raw.columns:
    null_cnt = df_raw[col].isnull().sum()
    null_pct = (null_cnt / len(df_raw)) * 100
    n_unique = df_raw[col].nunique()
    dtype = str(df_raw[col].dtype)
    summary_list.append({
        'Column': col,
        'Dtype': dtype,
        'Null_Count': null_cnt,
        'Null_Pct': round(null_pct, 3),
        'Unique_Count': n_unique
    })
sum_df = pd.DataFrame(summary_list)
print(sum_df.to_string(index=False))

print("\n" + "=" * 60)
print("3. COUNTRY CODE & GEOGRAPHIC SPREAD")
# Read Country Code Excel
try:
    country_df = pd.read_excel('raw_data/Country-Code.xlsx')
    merged = df_raw.merge(country_df, on='Country Code', how='left')
    print("Country Breakdown:")
    print(merged['Country'].value_counts())
except Exception as e:
    print(f"Could not load Country-Code.xlsx: {e}")
    print(df_raw['Country Code'].value_counts())

print("\n" + "=" * 60)
print("4. INDIA FOCUS BREAKDOWN")
india_df = df_raw[df_raw['Country Code'] == 1].copy()
print(f"Total India Records: {len(india_df)} ({len(india_df)/len(df_raw)*100:.2f}%)")
print("Top 10 Cities in India:")
print(india_df['City'].value_counts().head(10))

# NCR breakdown
ncr_cities = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad']
ncr_df = india_df[india_df['City'].isin(ncr_cities)]
print(f"\nDelhi NCR Total Records: {len(ncr_df)} ({len(ncr_df)/len(india_df)*100:.2f}% of India)")

print("\n" + "=" * 60)
print("5. DUPLICATE ANALYSIS")
print(f"Exact row duplicates: {df_raw.duplicated().sum()}")
print(f"Duplicate Restaurant IDs: {df_raw.duplicated(subset=['Restaurant ID']).sum()}")
print(f"Duplicate (Restaurant Name, Address): {df_raw.duplicated(subset=['Restaurant Name', 'Address']).sum()}")
print(f"Duplicate Restaurant Names in India: {india_df.duplicated(subset=['Restaurant Name']).sum()}")
print("Top duplicate restaurant chains:")
print(india_df['Restaurant Name'].value_counts().head(10))

print("\n" + "=" * 60)
print("6. NUMERICAL VARIABLES & ANOMALIES")
print("\nAggregate rating stats (Overall):")
print(df_raw['Aggregate rating'].describe())
print(f"Zero Ratings (Unrated): {(df_raw['Aggregate rating'] == 0.0).sum()} ({(df_raw['Aggregate rating'] == 0.0).sum()/len(df_raw)*100:.2f}%)")
print("Rating Text Breakdown:")
print(df_raw['Rating text'].value_counts())

print("\nVotes stats:")
print(df_raw['Votes'].describe(percentiles=[0.25, 0.5, 0.75, 0.90, 0.95, 0.99]))
print(f"Zero Votes count: {(df_raw['Votes'] == 0).sum()}")

print("\nAverage Cost for two stats (INR / India):")
print(india_df['Average Cost for two'].describe(percentiles=[0.25, 0.5, 0.75, 0.90, 0.95, 0.99]))
print(f"Zero Cost for two in India: {(india_df['Average Cost for two'] == 0).sum()}")

print("\n" + "=" * 60)
print("7. CATEGORICAL VARIABLES & SERVICE AVAILABILITY (INDIA)")
print("\nHas Table booking:")
print(india_df['Has Table booking'].value_counts(normalize=True)*100)

print("\nHas Online delivery:")
print(india_df['Has Online delivery'].value_counts(normalize=True)*100)

print("\nIs delivering now:")
print(india_df['Is delivering now'].value_counts(normalize=True)*100)

print("\nPrice range distribution (1 to 4):")
print(india_df['Price range'].value_counts(normalize=True).sort_index()*100)

print("\n" + "=" * 60)
print("8. CUISINE ANALYSIS")
null_cuisines = df_raw['Cuisines'].isnull().sum()
print(f"Missing Cuisines in Raw: {null_cuisines}")
print(f"Unique Cuisine strings: {df_raw['Cuisines'].nunique()}")
# Explode cuisines
cuisines_split = df_raw['Cuisines'].dropna().apply(lambda x: [c.strip() for c in x.split(',')])
all_cuisines = pd.Series([c for sublist in cuisines_split for c in sublist])
print(f"Total Unique Individual Cuisines: {all_cuisines.nunique()}")
print("Top 10 Cuisines overall:")
print(all_cuisines.value_counts().head(10))

print("\n" + "=" * 60)
print("9. GEOGRAPHIC COORDINATES QUALITY")
zero_coords = ((df_raw['Longitude'] == 0) & (df_raw['Latitude'] == 0)).sum()
print(f"Records with Longitude=0 and Latitude=0: {zero_coords} ({zero_coords/len(df_raw)*100:.2f}%)")
if zero_coords > 0:
    print("Zero coords by Country/City:")
    print(df_raw[(df_raw['Longitude'] == 0) & (df_raw['Latitude'] == 0)][['City', 'Country Code']].value_counts())

