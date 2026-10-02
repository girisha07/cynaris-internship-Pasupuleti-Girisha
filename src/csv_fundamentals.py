
import pandas as pd
from pathlib import Path


def main():
    # Create sample student data
    data = {
        "Name": ["Asha", "Ravi", "Priya", "Kiran", "Meena"],
        "Age": [20, 21, 20, 22, 21],
        "Study_Hours": [2, 3, 4, 5, 6],
        "Score": [50, 60, 70, 80, 90]
    }

    df = pd.DataFrame(data)

    # Create data folder
    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Save CSV file
    csv_path = data_dir / "students.csv"
    df.to_csv(csv_path, index=False)

    print("CSV file created successfully!")

    # Read CSV file
    df = pd.read_csv(csv_path)

    print("\nDataset:")
    print(df)

    # Display first 3 rows
    print("\nFirst 3 Rows:")
    print(df.head(3))

    # Dataset information
    print("\nDataset Information:")
    print(df.info())

    # Statistical summary
    print("\nStatistical Summary:")
    print(df.describe())

    # Average score
    print("\nAverage Score:", df["Score"].mean())

    # Students scoring above 70
    print("\nStudents scoring above 70:")
    print(df[df["Score"] > 70])

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())


if __name__ == "__main__":
    main()