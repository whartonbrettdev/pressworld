import pandas as pd
from preswald import table, text, plotly
import plotly.express as px

# Step 1: Load the dataset from the 'data' folder
df = pd.read_csv('data/LakeCounty_Health_-6177935595181947989.csv')  # Load CSV file

# Step 2: Use pandas' SQL-like query (pandas DataFrame query)
# Querying data where Obesity > 30 using pandas query
filtered_df = df.query('Obesity > 30')

# Step 3: Build an interactive UI using preswald
text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")  # Display the filtered data in a table

# Step 4: Create a visualization (Bar chart showing Obesity rates by region)
fig = px.bar(filtered_df, x='NAME', y='Obesity', title='Obesity Rates by Region')  # Bar chart
plotly(fig)  # Display the plot
