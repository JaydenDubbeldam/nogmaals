# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot en met de opgegeven dag.

ma = "maandag"
di = "dinsdag"
wo = "woensdag"
do = "donderdag"
vr = "vrijdag"
za = "zaterdag"
zo = "zondag"

dag = input("Noem een dag! (ma,di,wo,do,vr,za,zo) ")

if dag == "ma":
    print("Omdat maandag het begin van de week is heeft het geen voorgaande dagen!")
elif dag == "di":
    print("Voorgaande dagen:")
    print("Maandag")
elif dag == "wo":
    print("Voorgaande dagen:")
    print("Maandag")
    print("Dinsdag")
elif dag == "do":
    print("Voorgaande dagen:")
    print("Maandag")
    print("Dinsdag")
    print("Woendag")
elif dag == "vr":
    print("Voorgaande dagen:")
    print("Maandag")
    print("Dinsdag")
    print("Woendag")
    print("Donderdag")
elif dag == "za":
    print("Voorgaande dagen:")
    print("Maandag")
    print("Dinsdag")
    print("Woendag")
    print("Donderdag")
    print("Vrijdag")
elif dag == "zo":
    print("Voorgaande dagen:")
    print("Maandag")
    print("Dinsdag")
    print("Woendag")
    print("Donderdag")
    print("Vrijdag")
    print("Zaterdag")