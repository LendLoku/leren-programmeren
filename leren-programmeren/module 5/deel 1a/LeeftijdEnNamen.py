def naamENleeftijd():
    namen = []
    leeftijd = []

    while True:
        vraagNaam = input("vul stop in als je klaar bent! Wat is je naam?: ")
        if vraagNaam == "stop":
            break
        vraagLeeftijd = input("Vul stop in als je klaar bent! Wat is je leeftijd?: ")
        if vraagLeeftijd == "stop":
            break
        namen.append(vraagNaam)
        leeftijd.append(vraagLeeftijd)
    x = zip(namen , leeftijd)
    return x

for naam , leeftijd in naamENleeftijd():
    print(f"{naam} is {leeftijd} jaar oud ")