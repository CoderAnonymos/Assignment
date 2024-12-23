# Lesson 12: Object-Oriented Programming, 2

# Create a class Expression
class Expression:
    # Constructor to initialize the attributes
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    # Method to calculate the addition of three numbers
    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

# Creating objects to test the implementation
if __name__ == "__main__":
    # Object 1
    expression1 = Expression(5, 10, 15)
    expression1.calculate_sum()

    # Object 2
    expression2 = Expression(20, 30, 40)
    expression2.calculate_sum()

    # Object 3
    expression3 = Expression(1, 2, 3)
    expression3.calculate_sum()
