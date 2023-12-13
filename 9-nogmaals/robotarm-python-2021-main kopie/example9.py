## Oefening 9

from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2

for x in range(4):
    for y in range(x + 1):
        robotArm.grab()
        for z in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
