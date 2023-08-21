import pandas as pd

# Read data/winemag-data-130k-v2.csv.zip file
reviews = pd.read_csv("data\winemag-data-130k-v2.csv.zip")

# Number of reviews for each unique country
country_count = reviews.country.value_counts()

# Average points per unique country
points_avg = reviews.groupby('country')['points'].mean().round(1)

# Create a summary of the data
summary_df = pd.DataFrame.merge(country_count, points_avg, on='country', how='inner')

# Write the summary to a new file in data folder named reviews-per-country.csv
summary_df.to_csv("./data/reviews-per-country.csv")
