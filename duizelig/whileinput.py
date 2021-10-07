# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’. 
# Print het aantal iteraties per iteratie. (Het aantal keren dat de vraag is gesteld)
invoer = ""
i = 0
while invoer != "quit":
    invoer = input("Noem een getal! ")
    i = i + 1
    print ("U heeft", i, "keer gebruik gemaakt van de input!" )
