import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_data
from src.visualizer import plot_temperature, plot_relationship

def main():
    df = load_data("sample.csv")

    if df is not None:
        print(df.head())

        plot_temperature(df)
        plot_relationship(df)

if __name__ == "__main__":
    main()