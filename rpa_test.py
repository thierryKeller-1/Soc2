import rpa as robot


robot.init()
robot.url("https://widgets.scorenco.com/old/61237b1e4a5cf15b5874d8d4")
robot.wait() # ensure results are fully loaded
robot.close()