import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load COVID-19 data from your dataset
covid_data = pd.read_csv("C:\\Users\\Simran Gawri\\Downloads\\archive (4)\\country_wise_latest.csv")  # Replace with the actual path to your dataset

# Data Cleaning and Preprocessing
# Drop rows with missing values (if any)
covid_data.dropna(inplace=True)

# Create visualizations

# Bar chart for COVID-19 data in India
india_data = covid_data[covid_data['Country/Region'] == 'India']
plt.figure(figsize=(12, 6))
plt.bar('India', india_data['Confirmed'].values[0], color='blue', label='Confirmed')
plt.bar('India', india_data['Deaths'].values[0], color='red', label='Deaths')
plt.bar('India', india_data['Recovered'].values[0], color='green', label='Recovered')
plt.xlabel('Country')
plt.ylabel('Counts')
plt.title('COVID-19 Data in India')
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart for COVID-19 data in top 10 countries
world_data = covid_data[covid_data['Country/Region'] != 'India']
top_10_countries = world_data.sort_values(by='Confirmed', ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.bar(top_10_countries['Country/Region'], top_10_countries['Confirmed'], color='blue', label='Confirmed')
plt.bar(top_10_countries['Country/Region'], top_10_countries['Deaths'], color='red', label='Deaths')
plt.bar(top_10_countries['Country/Region'], top_10_countries['Recovered'], color='green', label='Recovered')
plt.xlabel('Country')
plt.ylabel('Counts')
plt.title('COVID-19 Data in Top 10 Countries')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Compare India with top 10 countries
plt.figure(figsize=(12, 6))
plt.bar('India', india_data['Confirmed'].values[0], color='blue', label='Confirmed')
plt.bar('India', india_data['Deaths'].values[0], color='red', label='Deaths')
plt.bar('India', india_data['Recovered'].values[0], color='green', label='Recovered')
for i, row in top_10_countries.iterrows():
    plt.bar(row['Country/Region'], row['Confirmed'], alpha=0.5)
    plt.bar(row['Country/Region'], row['Deaths'], alpha=0.5)
    plt.bar(row['Country/Region'], row['Recovered'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Counts')
plt.title('Comparison of COVID-19 Data between India and Top 10 Countries')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
