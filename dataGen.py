import requests
import pandas as pd

try:
    # Fetching data from APIs
    owners_api = requests.get('http://localhost:8000/owners')
    owners_api.raise_for_status()
    owners_api_data = owners_api.json()

    bus_api = requests.get('http://localhost:8000/buses')
    bus_api.raise_for_status()
    bus_api_data = bus_api.json()

    # Create DataFrames
    owners_df = pd.DataFrame(owners_api_data)
    buses_df = pd.DataFrame(bus_api_data)





    # Merge on the correct fields
    merged_df = pd.merge(buses_df, owners_df, left_on='id', right_on='id', suffixes=('_bus', '_owner'))

    # Ensure 500,000 rows
    if len(merged_df) < 500_000:
        factor = 500_000 // len(merged_df) + 1
        merged_df = pd.concat([merged_df] * factor, ignore_index=True)
        merged_df = merged_df.head(500_000)

    # Shape of the dataset
    print("\nShape of the Dataset:")
    print(merged_df.shape)



    # Final Dataset Output
    print("\nMerged DataFrame:")
    print(merged_df.head())

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
