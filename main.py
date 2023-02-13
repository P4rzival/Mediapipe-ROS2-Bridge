from functions import *

# Setup ROS2 Environment
os.system("source /opt/ros/humble/setup.bash")

pathToRobotModel = browseFiles()  

startRobot(pathToRobotModel)

#TODO manipulate the robot

#TODO Print inputs from mediapipe

#TODO Pass mediapipe inputs to ROS2
