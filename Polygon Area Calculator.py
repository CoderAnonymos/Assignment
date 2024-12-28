from abc import ABC, abstractmethod
import math

# Abstract Base Class for Polygon
class Polygon(ABC):
    def __init__(self, sides: int):
        self.sides = sides

    # Abstract method to calculate area, will be implemented in subclasses
    @abstractmethod
    def calculate_area(self, side_length: float) -> float:
        pass

    # Method to get the name of the polygon
    def get_polygon_name(self):
        if self.sides == 3:
            return "Triangle"
        elif self.sides == 4:
            return "Square"
        elif self.sides == 5:
            return "Pentagon"
        elif self.sides == 6:
            return "Hexagon"
        elif self.sides == 7:
            return "Heptagon"
        elif self.sides == 8:
            return "Octagon"
        else:
            return f"{self.sides}-gon"

# Subclass for calculating the area of a Square
class Square(Polygon):
    def __init__(self, sides: int = 4):
        super().__init__(sides)

    def calculate_area(self, side_length: float) -> float:
        return side_length ** 2

# Subclass for calculating the area of a Triangle
class Triangle(Polygon):
    def __init__(self, sides: int = 3):
        super().__init__(sides)

    def calculate_area(self, side_length: float) -> float:
        # Area of equilateral triangle = (side^2 * sqrt(3)) / 4
        return (side_length ** 2 * math.sqrt(3)) / 4

# Main function to run the polygon area calculator
def polygon_area_calculator():
    print("Welcome to the Polygon Area Calculator!")
    
    try:
        # Ask the user for the number of sides and the unit of measurement
        sides = int(input("How many sides does your polygon have? "))
        unit_of_measurement = input("What unit of measurement are you using? (e.g., cm, m, etc.) ").strip()
        
        if sides < 3:
            print("Sorry, a polygon must have at least 3 sides.")
            return

        polygon = None

        # Determine which polygon class to instantiate based on number of sides
        if sides == 3:
            polygon = Triangle(sides)
        elif sides == 4:
            polygon = Square(sides)
        else:
            print(f"Sorry, this calculator only supports polygons with 3 or 4 sides.")
            return

        # Ask for the length of one side of the polygon, ensuring the user provides a valid float
        side_length_input = input(f"How long is one side of the {polygon.get_polygon_name()}?").strip()
        
        # Try to extract and convert the numeric part of the input to float
        try:
            side_length = float(side_length_input)
        except ValueError:
            print("Please enter a valid number for the side length.")
            return
        
        # Calculate the area using the correct formula for the polygon
        area = polygon.calculate_area(side_length)
        print(f"The area of your {polygon.get_polygon_name()} is: {area:.2f} square {unit_of_measurement}.")
    
    except ValueError:
        print("Please enter a valid number for the number of sides.")

# Run the program
polygon_area_calculator()
