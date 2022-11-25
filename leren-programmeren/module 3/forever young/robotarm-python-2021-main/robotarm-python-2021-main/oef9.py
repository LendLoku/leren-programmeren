from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for x in range (1,5):
 for box in range (x):
  robotArm.grab()
  for move in range(5):
   robotArm.moveRight()
  robotArm.drop()
  for move in range (5 - int(box == x - 1)):
   robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()