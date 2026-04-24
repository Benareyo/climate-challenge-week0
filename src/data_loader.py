import pandas as pd

def load_data(file_path):
    """
    Load dataset from a CSV file
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None


def preview_data(df, n=5):
    """
    Show first n rows
    """
    return df.head(n)