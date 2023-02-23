def bereken_poten(giraffen, struisvogels, zebras):
    totaal_poten = (4 * giraffen) + (2 * struisvogels) + (4 * zebras)
    return totaal_poten

g = int(input("Hoeveel giraffen zijn er? "))
s = int(input("Hoeveel struisvogels zijn er? "))
z = int(input("Hoeveel zebra's zijn er? "))

totaal_poten = bereken_poten(g, s, z)
print("Het totaal aantal poten is:", totaal_poten)