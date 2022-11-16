from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.grab()
for block1 in range (5):
    robotArm.moveRight()
robotArm.drop()
for block1 in range (5):
    robotArm.moveLeft()
robotArm.grab()
for block2 in range (4):
    robotArm.moveRight()
robotArm.drop()
for block2 in range (4):
    robotArm.moveLeft()
robotArm.grab()
for block3 in range (3):
    robotArm.moveRight()
robotArm.drop()
for block3 in range (3):
    robotArm.moveLeft()
robotArm.grab()
for block4 in range (2):
    robotArm.moveRight()
robotArm.drop()
for block4 in range (2):
    robotArm.moveLeft()
robotArm.grab()
for block5 in range(1):
    robotArm.moveRight()
robotArm.drop()
for block1 in range (1):
    robotArm.moveRight()
robotArm.grab()
for block1 in range (1):
    robotArm.moveLeft()
robotArm.drop()
for block2 in range (2):
    robotArm.moveRight()
robotArm.grab()
for block2 in range (2):
    robotArm.moveLeft()
robotArm.drop()
for block3 in range (3):
    robotArm.moveRight()
robotArm.grab()
for block3 in range (3):
    robotArm.moveLeft()
robotArm.drop()
for block4 in range (4):
    robotArm.moveRight()
robotArm.grab()
for block4 in range (4):
    robotArm.moveLeft()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()