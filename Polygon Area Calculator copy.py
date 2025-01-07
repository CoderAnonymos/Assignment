import math

class Polygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def display_sides(self):
        print(f"Each side length: {self.side_length}")

class AreaCalculator(Polygon):
    def __init__(self, num_sides, side_length, unit_of_measurement):
        super().__init__(num_sides, side_length)
        self.unit_of_measurement = unit_of_measurement

    def calculate_area(self):
        if self.num_sides < 3:
            return "Not a valid polygon."

        try:
            perimeter = self.num_sides * self.side_length
            apothem = self.side_length / (2 * math.tan(math.pi / self.num_sides))
            area = (perimeter * apothem) / 2
            return area
        except ZeroDivisionError:
            return "Invalid side length or number of sides for area calculation."

    def display_area(self):
        area = self.calculate_area()
        if isinstance(area, str):
            print(area)
        else:
            print(f"The area of the polygon is {area:.2f} {self.unit_of_measurement}^2.")

if __name__ == "__main__":
    try:
        while True:
            try:
                num_sides = int(input("Enter the number of sides of the polygon (up to 20): "))
                if num_sides < 3:
                    print("A polygon must have at least 3 sides.")
                    continue
                elif num_sides > 20:
                    print("This calculator supports polygons with up to 20 sides.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                side_length = float(input("Enter the length of each side (without units): "))
                if side_length <= 0:
                    print("Side length must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        unit_of_measurement = input("Enter the unit of measurement (e.g., cm, m, in): ")

        polygon = AreaCalculator(num_sides, side_length, unit_of_measurement)
        polygon.display_sides()
        polygon.display_area()
    except OSError as e:
        if e.errno == 29:
            print("I/O error occurred. Please try again.")
        else:
            print(f"An unexpected error occurred: {e}")
