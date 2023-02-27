weight=int(input("Please enter your current earth weight: "))
print("I have information for the following planets:")
print("   1.Venus     2.Mars    3.Jupiter")
print("   4.Saturn    5.Uranus  6.Neptune")
planet=int(input("Which planet are you visiting? "))
Venus = 0.78*128
Mars = 0.39*128
Jupiter = 2.65*128
Saturn = 1.17*128
Uranus = 1.05*128
Neptune = 1.23*128
if planet==1:
    print("Your weight would be {} pounds on the planet.".format(Venus))
elif planet==2:
    print("Your weight would be {} pounds on the planet.".format(Mars))
elif planet==3:
    print("Your weight would be {} pounds on the planet.".format(Jupiter))
elif planet==4:
    print("Your weight would be {} pounds on the planet.".format(Saturn))
elif planet==5:
    print("Your weight would be {} pounds on the planet.".format(Uranus))
elif planet==6:
    print("Your weight would be {} pounds on the planet.".format(Neptune))
else:
    print("Please enter invalid number")