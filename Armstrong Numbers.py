# Function to check if a number is an Armstrong number
def is_armstrong(number):
    num_str = str(number)  # Convert the number to a string
    num_digits = len(num_str)  # Count the number of digits
    armstrong_sum = 0  # Initialize the sum

    # Loop through each digit
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits  # Add the digit raised to the power

    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Input from the user
num = int(input("Enter a number to check if it is an Armstrong number: "))

# Check and display the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")
