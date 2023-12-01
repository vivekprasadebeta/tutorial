# Import necessary libraries
import pandas as pd

# Function to check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()

# Function to validate class and stream
def validate_class_stream(class_name, stream_name):
    valid_classes = ['10th', '12th']
    valid_streams = ['Science', 'Commerce']
    return class_name in valid_classes and stream_name in valid_streams

# Function to sanitize the percentage
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to assign grades based on percentages
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
