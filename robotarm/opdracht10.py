from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
for f in range(10):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#Verplaats alle witte blokken één plek naar rechts. 

#Let op, de blokken zijn iedere keer anders als je het programma start!

