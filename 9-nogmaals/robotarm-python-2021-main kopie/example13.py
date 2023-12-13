## Oefening 13

from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2
robotArm.randomLevel(1,7)

color = 0
x = 1

while color != "":
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        break
    for y in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for y in range(x):
        robotArm.moveLeft()
    x += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
