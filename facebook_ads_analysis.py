
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('facebook_ads_data.csv')

# 1. Daily Analysis (2021)
# Grouping data by date and filtering for the year 2021
df['ad_date'] = pd.to_datetime(df['ad_date'])
daily_data = df[df['ad_date'].dt.year == 2021].groupby('ad_date').sum()

# Plotting daily ad spend in 2021
plt.figure(figsize=(10, 6))
plt.plot(daily_data.index, daily_data['total_spend'], label='Daily Ad Spend')
plt.title('Daily Ad Spend in 2021')
plt.xlabel('Date')
plt.ylabel('Total Spend')
plt.legend()
plt.show()

# Plotting daily ROMI in 2021
plt.figure(figsize=(10, 6))
plt.plot(daily_data.index, daily_data['romi'], label='Daily ROMI', color='orange')
plt.title('Daily ROMI in 2021')
plt.xlabel('Date')
plt.ylabel('ROMI')
plt.legend()
plt.show()

# 2. Campaign-Level Analysis
# Grouping data by campaign name
campaign_data = df.groupby('campaign_name').sum()

# Plotting total ad spend by campaign
plt.figure(figsize=(12, 8))
sns.barplot(x=campaign_data.index, y=campaign_data['total_spend'])
plt.title('Total Ad Spend by Campaign')
plt.xlabel('Campaign Name')
plt.ylabel('Total Spend')
plt.xticks(rotation=90)
plt.show()

# Plotting total ROMI by campaign
plt.figure(figsize=(12, 8))
sns.barplot(x=campaign_data.index, y=campaign_data['romi'], color='orange')
plt.title('Total ROMI by Campaign')
plt.xlabel('Campaign Name')
plt.ylabel('ROMI')
plt.xticks(rotation=90)
plt.show()

# 3. Distribution Analysis
# Box plot of daily ROMI by campaign
plt.figure(figsize=(12, 8))
sns.boxplot(x='campaign_name', y='romi', data=df)
plt.title('Daily ROMI Distribution by Campaign')
plt.xlabel('Campaign Name')
plt.ylabel('ROMI')
plt.xticks(rotation=90)
plt.show()

# Histogram of ROMI distribution
plt.figure(figsize=(10, 6))
plt.hist(df['romi'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of ROMI Distribution')
plt.xlabel('ROMI')
plt.ylabel('Frequency')
plt.show()

# 4. Correlation Analysis
# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Linear regression plot between total spend and total value
sns.lmplot(x='total_spend', y='total_value', data=df, aspect=2, height=6)
plt.title('Linear Regression between Total Spend and Total Value')
plt.xlabel('Total Spend')
plt.ylabel('Total Value')
plt.show()
