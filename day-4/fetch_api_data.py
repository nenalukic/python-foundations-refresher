# Working with APIs in Python
# Basic Example — Using the requests Library
# Let’s start with a simple API call to a free public data API.

import requests
import pandas as pd

def fetch_data_from_api():
    """Fetch data from a public API and convert to DataFrame."""
    url = "https://jsonplaceholder.typicode.com/users"  # Fake sample API
    response = requests.get(url)

    # Check if request succeeded
    if response.status_code == 200:
        data = response.json()  # Convert response to Python list/dict
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    df = fetch_data_from_api()
    if df is not None:
        print("✅ Data fetched successfully!\n")
        print(df.head())
        df.to_csv("api_users.csv", index=False)
        print("\n💾 Data saved to api_users.csv")
    else:
        print("❌ Failed to fetch data from API.")  

# Key Takeaways:
# The requests library makes it easy to call APIs.
# Always check the response status code.
# Convert JSON responses to pandas DataFrames for analysis.
# Save the data locally for future use.
