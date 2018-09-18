schermWidth = 40
woordMax = 14

naam = input("Naam: ")
leeftijd = input("Leeftijd: ")


def print_shit(regel):
              print("| {:" + str(schermWidth - 4)+ "} |".format(regel))


text = ("| Naam: {:14} Leeftijd: {:23} |".format(naam, leeftijd))
dashes = len(text)

print("-"*dashes)
print(text)
print("-"*dashes)
