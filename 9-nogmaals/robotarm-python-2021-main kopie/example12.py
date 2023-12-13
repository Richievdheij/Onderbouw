## Oefening 12

from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2

for x in range(9, 0, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for y in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
