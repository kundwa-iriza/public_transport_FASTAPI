import requests
import pandas as pd

try:
    # Fetching data from the owners API
    owners_api = requests.get('http://localhost:8000/owners')
    owners_api.raise_for_status()
    owners_api_data = owners_api.json()


    print("Raw data fetched from API:")
    print(owners_api_data)


    if not owners_api_data:
        print("No data available in the 'owners' table.")
    else:

        odf = pd.DataFrame(owners_api_data)


        print("DataFrame preview:")
        print(odf.head())

        # Fetch first 50 rows for the first CSV file
        odf_part1 = odf.head(50)

        # Fetch last 50 rows for the second CSV file
        odf_part2 = odf.tail(50)

        # Exporting the two DataFrames to CSV files
        odf_part1.to_csv("owners_part1.csv", index=False)
        odf_part2.to_csv("owners_part2.csv", index=False)

        print("Row-wise split files exported successfully as 'owners_part1.csv' and 'owners_part2.csv'.")


        concatenated_df = pd.concat([odf_part1, odf_part2], axis=0)
        concatenated_df.to_csv("owners_concatenated.csv", index=False)

        print("Concatenated file exported successfully as 'owners_concatenated.csv'.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except Exception as ex:
    print(f"An error occurred: {ex}")
