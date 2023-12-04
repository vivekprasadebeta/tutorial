import pandas as pd

# Sample Input CSV data
data = {
    'Student Name': ['Shivam', 'Manpreet', 'Aditi', 'Aditya', 'Shivaay12'],
    'Class': ['12th', '10th', '12th', '12th', '7th'],
    'Stream': ['Science', 'Commerce', 'Commerce', 'Commerce', 'Arts'],
    'Percentage': [36, 76, 46, 30, 'pass']
}

# Create DataFrame from input data
df = pd.DataFrame(data)

# Remove Percentage column
df.drop('Percentage', axis=1, inplace=True)

# Function to calculate grades based on percentage
def calculate_grade(percentage):
    if percentage == 'pass':
        return 'C'  # Default grade for pass
    elif percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C+'
    elif percentage >= 40:
        return 'C'
    else:
        return 'F'

# Add Grade column to DataFrame
df['Grade'] = df.apply(lambda row: calculate_grade(row['Percentage']) if row['Percentage'] != 'pass' else 'C', axis=1)

# Save the DataFrame to a new CSV file
df.to_csv('output.csv', index=False)

print("Output CSV generated successfully.")
