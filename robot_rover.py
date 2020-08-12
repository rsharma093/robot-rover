import turtle
class RobotRover:
    # Robot Actions
    STEP_FORWARD = "S"
    TURN_LEFT = "L"
    TURN_RIGHT = "R"
    SHOW_MESSAGE = "?"
    QUIT = "Q"

    ACTIONS = [STEP_FORWARD, TURN_RIGHT, TURN_LEFT, SHOW_MESSAGE, QUIT]

    def __init__(self):
        turtle.title("Robot Rover")
        self.robot = turtle.Turtle()
        # In Standard mode default face is towards East so make it North by setheading by 90.
        self.robot.seth(90)
    
    def get_position(self):
        x, y = self.robot.pos()
        return ((round(y), round(x)))

    def get_face_direction(self):
        # In standard mode
        anglewise_direction = {
            0: "East",
            90: "North",
            180: "West",
            270: "South"
        }
        
        return anglewise_direction.get(round(self.robot.heading()))
        
    def move_robot(self, action):
        if action == self.STEP_FORWARD:
            self.robot.forward(1)
        elif action == self.TURN_LEFT:
            self.robot.seth(round(self.robot.heading()) + 90)
        elif action == self.TURN_RIGHT:
            self.robot.seth(round(self.robot.heading()) - 90)

    
    def options(self):
        return ("Command the robot with:\n L - turn left\n R - turn right\n S - step forward\n ? - this message\n Q - quit")

if __name__ == "__main__":
    r = RobotRover()
    print("\nHello! Robot coming online.")
    print(r.options()+"\n")
    
    is_quit = False
    while not is_quit:
        action = input("> ")
        if action not in r.ACTIONS:
            print(r.options())
        if action == r.SHOW_MESSAGE:
            print(r.options())
        elif action == r.QUIT:
            is_quit = True
            print("Robot shutting down.")
            turtle.bye()
        else:
            r.move_robot(action)
            print("Robot at {} facing {}".format(r.get_position(), r.get_face_direction()))
