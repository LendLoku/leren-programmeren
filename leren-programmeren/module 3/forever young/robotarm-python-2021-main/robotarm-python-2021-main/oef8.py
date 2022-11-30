from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
robotArm.moveRight()
for block in range (7):
    robotArm.grab()
    for move in range (8):
        robotArm.moveRight()
    robotArm.drop()
    for move in range (8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 