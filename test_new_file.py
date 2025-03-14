# Incorrect Naming Convention (should be snake_case)
def CalculateSum(a, b):
    return a + b

# Missing Docstring


def validate_input(user_input):
    if not isinstance(user_input, int):
        raise ValueError("Input must be an integer")
    return True

# Unused Variable


def process_data(data):
    temp_var = 100  # Unused variable
    return [d * 2 for d in data]


# Security Risk: API key stored in plain text
API_KEY = "sk-1234567890abcdef"

# Formatting Issue: Indentation (should be 4 spaces)


def fetch_data():
    print("Fetching data...")  # Incorrect indentation

# Inefficient Loop (Should use list comprehension)


def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result
