import os

# Starts the robot in Gazebo with model taken in at runtime.
def startRobot(pathToRobotModel):
    os.system("gz sim " + pathToRobotModel)