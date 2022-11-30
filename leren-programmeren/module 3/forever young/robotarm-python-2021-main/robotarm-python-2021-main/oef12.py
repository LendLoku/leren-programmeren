from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
teller = 9
for arm in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for arm in range(teller):
            robotArm.moveRight()
        robotArm.drop()
        for arm in range(teller-1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    teller -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()