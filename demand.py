import pandas as pd
import numpy as np
def generate_demand_dataset(num_months):
    """
    Generate a dataset simulating varying demand for a cancer drug over a specified number of months.

    Parameters:
    num_months (int): Number of months for which to generate the dataset.

    Returns:
    pandas.DataFrame: A DataFrame with simulated demand data.
    """
    # Generate monthly data
    months = pd.date_range(start='2023-01-01', periods=num_months, freq='M')
    np.random.seed(0)  # for reproducible results

    # Simulate original patient demand
    patients_demand_original = np.random.randint(100, 1001, size=len(months))

    # Add seasonal variation
    seasonal_variation = [1.2 if 1 <= month.month <= 3 or 10 <= month.month <= 12 else 0.8 for month in months]
    patients_demand_seasonal = (patients_demand_original * seasonal_variation).astype(int)

    # Simulate policy change impact (randomly between 0.9 to 1.1 to represent decrease or increase in demand)
    policy_change_impact = np.random.uniform(0.9, 1.1, size=len(months))
    final_demand = (patients_demand_seasonal * policy_change_impact).astype(int)

    # Create DataFrame
    demand_data = pd.DataFrame({
        'Month': months.month_name(),
        'Patients Demand (Original)': patients_demand_original,
        'Seasonal Variation Factor': seasonal_variation,
        'Patients Demand (Seasonal Adjusted)': patients_demand_seasonal,
        'Policy Change Impact': policy_change_impact,
        'Final Demand': final_demand
    })
    print(demand_data)
    return demand_data

# Example usage of the function
sample_dataset = generate_demand_dataset(12)
print(sample_dataset.head())  # Displaying the first few rows of the generated dataset