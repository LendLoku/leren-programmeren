from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for arm in range(8):
    robotArm.moveRight()
for arm in range(9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if arm < 8:
        robotArm.moveLeft() 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()