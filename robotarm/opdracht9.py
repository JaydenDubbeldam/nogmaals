from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
aantal = 11
for i in range(5):
    aantal = aantal - 2
    robotArm.grab()
    for g in range(0,aantal):
        robotArm.moveRight()
    robotArm.drop()
    for g in range(0,aantal -1):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()


#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
