from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
moves = 9
robotArm.grab()
for arm in range(5):
    for x in range(moves):
        robotArm.moveRight()
    robotArm.drop()
    moves = moves - 1
    for i in range(moves):
        robotArm.moveLeft()
    if arm < 4:
        robotArm.grab()
    moves = moves - 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()