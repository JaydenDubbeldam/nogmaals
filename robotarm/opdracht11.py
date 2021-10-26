from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
waarde = 0
for f in range(10):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    waarde +=1
    if color == "red":
            for g in range(10):
                robotArm.moveRight()
            robotArm.drop()
            for u in range(0,waarde):
                robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#Verplaats alle rode blokken naar het einde.

#Let op, de blokken zijn iedere keer anders als je het programma start!
