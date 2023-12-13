## Oefening 8

from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 3

robotArm.moveRight()
for x in range(7):
    robotArm.grab()

    for y in range(8):
        robotArm.moveRight()

    robotArm.drop()
    
    for y in range(8):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
