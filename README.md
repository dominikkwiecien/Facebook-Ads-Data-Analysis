
# Facebook Ads Data Analysis

## Overview

This project demonstrates an analysis of Facebook advertising campaigns using Python, focusing on data manipulation with Pandas and data visualization. The main objectives were to analyze daily expenditures and Return on Marketing Investment (ROMI) for different campaigns throughout 2021. The analysis includes various visualization techniques to better understand the relationships and trends within the dataset.

## Project Structure

- **Data Loading**: The project begins with loading the dataset `facebook_ads_data.csv` into a Pandas DataFrame.
- **Data Grouping**: The data is grouped by day and by campaign to facilitate the subsequent analyses.
- **Visualization**: Several types of visualizations were created to explore and present the data effectively.

## Visualizations

1. **Daily Analysis (2021)**:
   - **Daily Ad Spend**: A line chart showing the total ad spend per day throughout 2021.
   - **Daily ROMI**: A line chart depicting the daily ROMI in 2021.

   ```python
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
   ```
<img width="701" alt="image" src="https://github.com/user-attachments/assets/78fd5263-b391-4621-9aeb-95f283a67621">

<img width="700" alt="image" src="https://github.com/user-attachments/assets/08a67bbd-96fe-4960-8281-b289b49b24e1">


2. **Campaign-Level Analysis**:
   - **Total Ad Spend by Campaign**: A bar chart displaying the total ad spend for each campaign.
   - **Total ROMI by Campaign**: A bar chart showing the total ROMI for each campaign.
   
   ```python
   # Grouping data by campaign name
   campaign_data = df.groupby('campaign_name').sum()

   # Plotting total ad spend by campaign
   plt.figure(figsize=(12, 6))
   plt.bar(campaign_grouped_df['campaign_name'], campaign_grouped_df['total_spend'])
   plt.title('Total Ad Spend by Campaign')
   plt.xlabel('Campaign Name')
   plt.ylabel('Total Spend')
   plt.xticks(rotation=45, ha='right')
   plt.grid(True, axis='y')

   # Plotting total ROMI by campaign
   plt.figure(figsize=(12, 6))
   plt.bar(campaign_grouped_df['campaign_name'], campaign_grouped_df['romi'])
   plt.title('Average ROMI by Campaign')
   plt.xlabel('Campaign Name')
   plt.ylabel('Average ROMI')
   plt.xticks(rotation=45, ha='right')
   plt.grid(True, axis='y')
   ```
<img width="701" alt="image" src="https://github.com/user-attachments/assets/6f2653e4-2692-4f0b-a92e-1bb07cec5768">

<img width="700" alt="image" src="https://github.com/user-attachments/assets/b98aae92-7f1f-413f-8715-320955be0b48">

3. **Distribution Analysis**:
   - **Box Plot of Daily ROMI by Campaign**: A box plot highlighting the distribution of daily ROMI across campaigns.
   - **ROMI Histogram**: A histogram showing the distribution of ROMI values in the dataset.

   ```python
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
   ```

<img width="702" alt="image" src="https://github.com/user-attachments/assets/12f4f86b-8199-4b7e-b386-4f9870cb3b8d">

<img width="701" alt="image" src="https://github.com/user-attachments/assets/0321bd44-71de-48a5-b439-78483ff1fc15">


4. **Correlation Analysis**:
   - **Heatmap of Correlations**: A heatmap displaying the correlation between all numerical values in the dataset, identifying the highest and lowest correlations.
   - **Linear Regression Plot**: A scatter plot with a regression line illustrating the relationship between `total_spend` and `total_value` using the `lmplot()` function.

   ```python
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
   ```

<img width="701" alt="image" src="https://github.com/user-attachments/assets/a76ddd52-f3c0-46d0-a639-e5009b9e4a14">

<img width="701" alt="image" src="https://github.com/user-attachments/assets/8e66f528-ede1-4473-b103-c64888393ebe">


## Key Findings

- **Daily Trends**: Significant fluctuations in ad spend and ROMI were observed throughout 2021.
- **Campaign Performance**: The analysis revealed notable differences in performance across different campaigns.
- **Correlation Insights**: The heatmap provided a clear view of which metrics were most strongly correlated, particularly the relationship between `total_value` and other factors.

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**

## Conclusion

This project serves as an excellent example of using Python for data analysis and visualization, providing valuable insights into Facebook advertising campaigns. The visualizations offer a clear understanding of the data trends and relationships, enabling data-driven decision-making.
