from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for stapel in range (1,5):
   for box in range (stapel):
      robotArm.grab()
   for move in range(5):
      robotArm.moveRight()
   robotArm.drop()
   if box < stapel - 1:
      moves = 5
   else:
      moves = 4

   for move in range(moves):
      robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()