import pandas as pd
from datetime import datetime

# Load raw data
df = pd.read_csv('hr_data.csv')

# Convert dates
df['HireDate'] = pd.to_datetime(df['HireDate'])

# Add tenure column
df['TenureYears'] = (datetime.now() - df['HireDate']).dt.days // 365

# Save cleaned data
df.to_csv('cleaned_hr_data.csv', index=False)

print("✅ Cleaned data saved for Power BI.")
