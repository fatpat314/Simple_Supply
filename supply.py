import pandas as pd
import numpy as np
from random import randint, uniform

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Francisco",
          "Miami", "Atlanta", "Boston", "Seattle", "Denver", "Las Vegas", "Washington, D.C.", "Austin", "Nashville", "Orlando",
          "New Orleans", "San Jose", "Minneapolis", "Detroit", "Portland", "Charlotte", "Indianapolis", "Jacksonville", "Columbus",
          "Memphis", "Baltimore", "Milwaukee", "Fort Worth", "Louisville", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach",
          "Kansas City", "Mesa", "Virginia Beach", "Atlanta", "Colorado Springs", "Omaha", "Raleigh", "Miami Beach", "Oakland", "Tulsa",
          "Cleveland", "Wichita", "Arlington", "Tampa", "Bakersfield", "Aurora", "New York City", "Los Angeles", "Chicago", "Houston",
          "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Francisco", "Miami", "Atlanta", "Boston", "Seattle",
          "Denver", "Las Vegas", "Washington, D.C.", "Austin", "Nashville", "Orlando", "New Orleans", "San Jose", "Minneapolis", "Detroit",
          "Portland", "Charlotte", "Indianapolis", "Jacksonville", "Columbus", "Memphis", "Baltimore", "Milwaukee", "Fort Worth", "Louisville",
          "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Virginia Beach", "Atlanta", "Colorado Springs",
          "Omaha", "Raleigh", "Miami Beach", "Oakland", "Tulsa", "Cleveland", "Wichita", "Arlington", "Tampa", "Bakersfield", "Aurora"]

# Set the random seed for reproducibility
np.random.seed(42)

# Change Inventory
inventory_min = 0
inventory_max = 1500

# Change Cost
unit_cost_min = 50.0
unit_cost_max = 200.0

# Function to generate synthetic data for the dataset
def generate_supply_data(num_cities, num_months):
    data = []

    for city_id in cities:
        for month in range(1, num_months + 1):
            # Generate random values for inventory and cost
            inventory = randint(inventory_min, inventory_max)
            cost_per_unit = uniform(unit_cost_min, unit_cost_max)

            # Calculate total cost
            total_cost = inventory * cost_per_unit

            # Append the data to the list
            data.append({
                'City_Name': f'City: {city_id}',
                'Month': month,
                'Inventory': inventory,
                'Cost_Per_Unit': cost_per_unit,
                'Total_Cost': total_cost
            })

    return data

# Specify the number of cities and months
num_cities = len(cities)
num_months = 12

# Generate synthetic data
supply_data = generate_supply_data(num_cities, num_months)

# Create a DataFrame from the generated data
df = pd.DataFrame(supply_data)

# Save the DataFrame to a CSV file
df.to_csv('cancer_drugs_supply_dataset.csv', index=False)

# Display the first few rows of the generated dataset
print(df.head())
