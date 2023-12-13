from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2

robotArm.grab()

for i in range(9):
    robotArm.moveRight()

robotArm.drop()

for i in range(5):
    robotArm.moveLeft()

robotArm.grab()

for i in range(6):
    robotArm.moveRight()

robotArm.drop()

for i in range(2):
    robotArm.moveLeft()

robotArm.grab()

for i in range(2):
    robotArm.moveRight()

robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()