import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Fun with Shapes!")
screen.bgcolor("purple")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing
pen.pensize(2)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Function to draw a circle
def draw_circle(size):
    pen.circle(size)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Function to draw a polygon
def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(size)
        pen.left(angle)

# Random color generator
def random_color():
    return random.random(), random.random(), random.random()

# Main menu for drawing shapes
def draw_shapes():
    while True:
        print("\nFun with Shapes!")
        print("1. Square")
        print("2. Triangle")
        print("3. Circle")
        print("4. Star")
        print("5. Polygon")
        print("6. Clear Screen")
        print("7. Exit")
        
        choice = input("Choose a shape to draw (1-7): ")
        
        if choice == "1":
            pen.color(random_color())
            size = int(input("Enter the size of the square: "))
            draw_square(size)
        elif choice == "2":
            pen.color(random_color())
            size = int(input("Enter the size of the triangle: "))
            draw_triangle(size)
        elif choice == "3":
            pen.color(random_color())
            size = int(input("Enter the radius of the circle: "))
            draw_circle(size)
        elif choice == "4":
            pen.color(random_color())
            size = int(input("Enter the size of the star: "))
            draw_star(size)
        elif choice == "5":
            pen.color(random_color())
            sides = int(input("Enter the number of sides for the polygon: "))
            size = int(input("Enter the size of each side: "))
            draw_polygon(sides, size)
        elif choice == "6":
            pen.clear()  # Clear the screen
        elif choice == "7":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main menu
draw_shapes()

# Close the window when done
turtle.done()
