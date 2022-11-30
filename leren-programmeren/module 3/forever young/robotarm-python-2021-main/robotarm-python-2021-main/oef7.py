from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.moveRight()
for x in range (5):
    for block in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for x in range (1):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()