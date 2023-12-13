from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 1
startPosition_amount = 3
endPosition_amount = 1

for i in range(1, 4):
    robotArm.grab()

    for i in range(startPosition_amount):
        robotArm.moveRight()

    robotArm.drop()

    for i in range(startPosition_amount):
        robotArm.moveLeft()


    startPosition_amount -= 1


for i in range(2):
    for i in range(2):
        robotArm.moveRight()

    robotArm.grab()

    for i in range(endPosition_amount):
        robotArm.moveLeft()

    robotArm.drop()

    endPosition_amount += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()