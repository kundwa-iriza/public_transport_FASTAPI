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

    # Creating dataframes
    odf = pd.DataFrame(owners_api_data)
    bdf = pd.DataFrame(bus_api_data)

    # Printing the shape of each dataset
    print(f"Owners Dataset Shape: {odf.shape}")
    print(f"Buses Dataset Shape: {bdf.shape}")

    # Describing the owners dataset
    print("\nOwners Dataset Description:")
    print(odf.describe(include='all'))  # Statistical summary of the owners dataset

    # Describing the buses dataset
    print("\nBuses Dataset Description:")
    print(bdf.describe(include='all'))  # Statistical summary of the buses dataset

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
