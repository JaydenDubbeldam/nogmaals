mm = input("Wil je de hele uren van de morgen of middag zien? ").lower()

i = 0
if mm == "morgen":
    while i < 13:
        print(i,": 00 AM")
        i = i + 1

elif mm == "middag":
    while i < 13:
        print(i,": 00 PM")
        i = i + 1