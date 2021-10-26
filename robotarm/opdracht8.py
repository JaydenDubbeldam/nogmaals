from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
robotArm.grab()

aantal = 0

for i in range(4):

    aantal += 1

    for c in range(0,aantal,1):
        robotArm.grab()

        for g in range(5):
            robotArm.moveRight()

        robotArm.drop()
        for g in range(5):
            robotArm.moveLeft()

    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#Verplaats alle stapels vijf stappen naar rechts.

#Je mag maximaal 12 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
