class Robot:
    def __init__(self, name, model, purpose, color):
        self.name = name
        self.model = model
        self.purpose = purpose
        self.color = color

    def introduce(self):
        return (f"Hello, I am {self.name}. I am a {self.color} robot of model {self.model}. "
                f"My purpose is to {self.purpose}.")

# Example Usage
if __name__ == "__main__":
    robot = Robot(name="RoboHelper", model="X200", purpose="assist with household chores", color="silver")
    print(robot.introduce())
