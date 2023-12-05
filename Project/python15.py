import pandas as pd
import sys


def sanitize_data(df):

        # Remove rows with incorrect data
        df = df[df['Student Name'].str.isalpha()]
        df = df[df['Class'].isin(['12th', '10th'])]
        df = df[df['Stream'].isin(['Science', 'Commerce'])]
        df['Percentage'] = pd.to_numeric(df['Percentage'], errors='coerce')  # Convert 'Percentage' to numeric

        # Drop rows with NaN in 'Percentage'
        df = df.dropna(subset=['Percentage'])

        # Assign Grades based on Percentage
        def assign_grade(percentage):
            if percentage < 35:
                return 'F'
            elif 35 <= percentage < 45:
                return 'C'
            elif 45 <= percentage < 60:
                return 'B'
            elif 60 <= percentage < 75:
                return 'A'
            else:
                return 'A+'

        df['Grade'] = df['Percentage'].apply(assign_grade)
        return df[['Student Name', 'Class', 'Stream', 'Grade']]

def main(file_path):
    try:
        df = pd.read_csv(file_path)  # Read the CSV file
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    print("Columns in the Input DataFrame:")
    print(df.columns)  # Print columns from the DataFrame

    # Sanitize and process data
    sanitized_data = sanitize_data(df)

    # Writing to CSV
    sanitized_data.to_csv('result.csv', index=False)
    print("Output CSV file generated successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_csv_file_path>")
    else:
        input_file = sys.argv[1]
        main(input_file)
