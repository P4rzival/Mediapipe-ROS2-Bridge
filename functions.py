import os
from tkinter import filedialog

# Starts the robot in Gazebo with model taken in at runtime.
def startRobot(pathToRobotModel):
    os.system("gz sim " + pathToRobotModel)

# Function for opening the
# file explorer window
# Source: https://www.geeksforgeeks.org/file-explorer-in-python-using-tkinter/
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = ".",
                                          title = "Select Model File",
                                          filetypes = (("SDF files",
                                                        "*.sdf*"),
                                                       ("all files",
                                                        "*.*")))
    return filename