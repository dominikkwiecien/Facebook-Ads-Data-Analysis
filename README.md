
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

2. **Campaign-Level Analysis**:
   - **Total Ad Spend by Campaign**: A bar chart displaying the total ad spend for each campaign.
   - **Total ROMI by Campaign**: A bar chart showing the total ROMI for each campaign.
   
   ```python
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
   ```

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

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/facebook-ads-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd facebook-ads-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the Jupyter Notebook and run the cells to see the analysis:
   ```bash
   jupyter notebook zajęcia_5.ipynb
   ```

## Conclusion

This project serves as an excellent example of using Python for data analysis and visualization, providing valuable insights into Facebook advertising campaigns. The visualizations offer a clear understanding of the data trends and relationships, enabling data-driven decision-making.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Instructor**: Thanks to the course instructor for providing the dataset and guiding through the project.
- **OpenAI GPT-4**: Assistance in generating the content for this README.
