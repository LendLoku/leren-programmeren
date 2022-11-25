from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)    
# Jouw python instructies zet je vanaf hier:
teller = 9
move = True
while move:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "":
        print('geen blokje')
        bewegen = False
        robotArm.wait()
    else:
        for x in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,teller):
            robotArm.moveLeft()
        teller -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()