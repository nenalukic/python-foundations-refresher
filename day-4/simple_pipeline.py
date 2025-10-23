# A Mini ETL with Functions: Extract, Transform, Load
# Let’s make a simple pipeline that: reads a CSV file, cleans column names, saves it back to a new file.

import pandas as pd
import os

def extract(filepath):
    """Extract data from CSV file."""
    print(f"Extracting data from {filepath}")
    return pd.read_csv(filepath)

def transform(df):
    """Transform data by cleaning column names."""
    print("Transforming data...")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load(df, output_path):
    """Load (save) cleaned data to a new CSV file."""
    print(f"Saving cleaned data to {output_path}")
    df.to_csv(output_path, index=False)

def etl_pipeline(input_file, output_file):
    """Complete ETL process."""
    df = extract(input_file)
    df_clean = transform(df)
    load(df_clean, output_file)
    print("✅ Pipeline complete!")

# Run pipeline
if __name__ == "__main__":
    input_path = "data/raw_sales.csv"
    output_path = "data/clean_sales.csv"

    # Make sure folder exists
    os.makedirs("data", exist_ok=True)

    # Create dummy input data
    dummy_data = {
        "Product Name": ["Keyboard", "Mouse", "Monitor"],
        " Price": [25, 15, 200],
        "Quantity ": [10, 20, 5]
    }
    pd.DataFrame(dummy_data).to_csv(input_path, index=False)

    etl_pipeline(input_path, output_path)

# Key Takeaways:
# Functions make your code modular — great for ETL tasks.
# Each function does one clear job (Extract / Transform / Load).
# The if __name__ == "__main__": block ensures your pipeline runs only when you execute the file directly — not when you import it from another script.