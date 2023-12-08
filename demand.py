# Comprehensive and Detailed Simulation Code for Cancer Drug Demand

# Importing necessary libraries
import pandas as pd
import numpy as np
from random import randint, uniform, choice

# Let's begin by defining our list of cities. These are the locations where we'll be simulating the demand for cancer drugs.
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
          "San Antonio", "San Diego", "Dallas", "San Francisco", "Miami", "Atlanta",
          "Boston", "Seattle", "Denver", "Las Vegas", "Washington, D.C.", "Austin",
          "Nashville", "Orlando", "New Orleans", "San Jose", "Minneapolis", "Detroit",
          "Portland", "Charlotte", "Indianapolis", "Jacksonville", "Columbus",
          "Memphis", "Baltimore", "Milwaukee", "Fort Worth", "Louisville", "Albuquerque",
          "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa",
          "Virginia Beach", "Colorado Springs", "Omaha", "Raleigh", "Miami Beach",
          "Oakland", "Tulsa", "Cleveland", "Wichita", "Arlington", "Tampa", "Bakersfield",
          "Aurora"]

# For a more realistic simulation, let's establish the demand persona. This persona represents the typical patient or group of patients in need of cancer drugs.
def define_demand_persona():
    age_group = choice(['<18', '18-40', '40-65', '>65'])
    income_level = choice(['Low', 'Medium', 'High'])
    healthcare_access = choice(['Low', 'Medium', 'High'])
    disease_prevalence = choice(['Low', 'Medium', 'High'])
    return age_group, income_level, healthcare_access, disease_prevalence

# Now, let's write a function to generate our comprehensive demand data. We'll include several details like the day of the month to capture daily demand fluctuations.
def generate_comprehensive_demand_data(num_data_points):
    data = []
    for _ in range(num_data_points):
        city = choice(cities)
        month = randint(1, 12)
        day = randint(1, 28)  # A simplification for the day of the month
        demand = randint(250, 300)  # Demand varies between 250 and 300 units

        # Gathering persona attributes
        age_group, income_level, healthcare_access, disease_prevalence = define_demand_persona()
        patient_count = randint(1, 100)  # Number of patients affected in the city
        treatment_frequency = choice(['Regular', 'Occasional', 'Rare'])  # Frequency of treatment needed
        drug_type_preference = choice(['Generic', 'Branded'])  # Type of drug preferred
        urgency_level = choice(['High', 'Medium', 'Low'])  # Urgency of need for the drug
        insurance_coverage = choice(['Full', 'Partial', 'None'])  # Insurance coverage level

        # Appending all these details to our dataset
        data.append({
            'City': city,
            'Month': month,
            'Day': day,
            'Demand': demand,
            'Age Group': age_group,
            'Income Level': income_level,
            'Healthcare Access': healthcare_access,
            'Disease Prevalence': disease_prevalence,
            'Patient Count': patient_count,
            'Treatment Frequency': treatment_frequency,
            'Drug Type Preference': drug_type_preference,
            'Urgency Level': urgency_level,
            'Insurance Coverage': insurance_coverage
        })

    return pd.DataFrame(data)

# Generating the dataset with a random number of data points between 250 and 300 for a robust simulation
num_data_points = randint(250, 300)
comprehensive_demand_data = generate_comprehensive_demand_data(num_data_points)

df = pd.DataFrame(comprehensive_demand_data)
df.to_csv('cancer_drugs_demand_dataset.csv', index=False)

# Let's take a peek at the first few rows of our dataset
print(comprehensive_demand_data.head())