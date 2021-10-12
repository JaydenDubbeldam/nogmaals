# name of student: Jayden Dubbeldam
# number of student: 99066416
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #De vraag hoeveel je moet betalen

paid = int(float(input('Paid amount: ')) * 100) #Hoeveel je al hebt betaald

change = paid - toPay #kijken of je geld terug krijgt



if change > 0: #checkt of het getal groter dan 0 is.

  coinValue = 200 #hoeveel een munt waard is

  

  while change > 0 and coinValue > 0: #kijkt of ze hoger dan 0 zijn

    nrCoins = change // coinValue #berekend het aantal munten.



    if nrCoins > 0: #Is het aantal munten hoger dan nul

      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print het aantal munten en hoeveel ze waard zijn

      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #vraagt hoeveel munten je hebt gegeven

      change -= nrCoinsReturned * coinValue #Haalt een berekent aantal van het wisselgeld af.



# comment on code below: veranderd de coinvalue voor de vraag hierboven

    if coinValue == 200:

      coinValue = 100

    elif coinValue == 100:

      coinValue = 50

    elif coinValue == 50:

      coinValue = 20

    elif coinValue == 20:

      coinValue = 10

    elif coinValue == 10:

      coinValue = 5

    elif coinValue == 5:

      coinValue = 2

    elif coinValue == 2:

      coinValue = 1

    else:

      coinValue = 0



if change > 0: # checkt of hij groter dan 0 is

  print('Change not returned: ', str(change) + ' cents')

else:

  print('done')
  