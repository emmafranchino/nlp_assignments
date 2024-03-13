import pandas as pd
import os

# Read the CSV file
df = pd.read_csv("data/original.csv")  # Assuming tab-separated, adjust delimiter as needed

# Filter the data for the years 1999 and 2014
df_filtered = df[(df['year'] == 1999) | (df['year'] == 2014)]

# Group the filtered DataFrame by year, gender, and name, and calculate frequency
grouped = df_filtered.groupby(['year', 'gender', 'name']).agg({'count': 'sum'}).reset_index()

# Iterate over the groups and save to separate text files
for year in grouped['year'].unique():
    for gender in grouped['gender'].unique():
        year_gender_data = grouped[(grouped['year'] == year) & (grouped['gender'] == gender)]
        filename = f"data/{year}_{gender}.txt"
        with open(filename, 'w') as f:
            for index, row in year_gender_data.iterrows():
                name = row['name']
                name = name.replace('\x07', '').replace("'", "").replace("\n","")
                # Capitalize the first letter, make the rest of the name lowercase, and replace spaces with "-"
                name = name.capitalize().replace(" ", "-")
                count = row['count']
                # Write the name repeated count times to the file
                f.write((name + '\n') * count)
