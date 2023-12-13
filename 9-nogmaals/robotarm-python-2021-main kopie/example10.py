## Oefening 10

from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2

y = 9
for x in range(5):
    robotArm.grab()
    for z in range(y):
        robotArm.moveRight()
    y -= 1
    robotArm.drop()
    for z in range(y):
        robotArm.moveLeft()
    y -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
