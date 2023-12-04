import pandas as pd
import re

def sanitize_data(df):
    # Remove rows with incorrect data
    print(df.columns)
    df = df[df['Student Name'].str.isalpha()]
    df = df[df['Class'].isin(['12th', '10th'])]
    df = df[df['Stream'].isin(['Science', 'Commerce'])]
   # df = df[df['Percentage'] ]#apply(lambda x: isinstance(x, float))]
   # df = df[df['Percentage'].apply(lambda x: isinstance(x, float))]
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


def main():
    data = []
    while True:
        student_name = input("Enter Student Name: ")
        name1 = str(student_name)
        print(name1)
        name_pattern = r"^[a-zA-Z]+$"
        if re.match(name_pattern, name1):
            print("Yes ")
        else:
            print("No match")

        class_level = input("Enter Class (10th or 12th): ")
        stream = input("Enter Stream (Science or Commerce): ")
        try:
            percentage = float(input("Enter Percentage: "))
            percentage1 = float(percentage)
            print(percentage1)
            percentage_pattern = r"^[0-9][0-9,.]+$"

            if re.match(percentage_pattern, percentage):
                print("Yes Percentage")
            else:
                print("Please enter valid percentage")

        except ValueError:
            print("Please enter a valid percentage!")
            continue

        data.append([student_name, class_level, stream, percentage])

        more_students = input("Do you want to enter details for more students? (yes/no): ")
        if more_students.lower() != 'yes':
            break

    # Creating DataFrame
    columns = ['Student Name', 'Class', 'Stream', 'Percentage']
    df = pd.DataFrame(data, columns=columns)

    # Sanitize and process data
    sanitized_data = sanitize_data(df)

    # Writing to CSV
    sanitized_data.to_csv('result.csv', index=False)
    print("Output CSV file generated successfully!")


if __name__ == "__main__":
    main()