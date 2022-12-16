boodschappenlijst = {}
extra = "ja"
while extra == "ja":
    product = input("Welke product wil je toevoegen aan uw boodschappenlijst?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    
    if product not in boodschappenlijst:
        boodschappenlijst.update({product: aantal})    
    
    else:
        boodschappenlijst[product] += aantal
    extra = input("Wil je nog een product toevoegen?: ").lower()

print("BOODSCHAPPENLIJST")
for aantal, product in boodschappenlijst.items():
    print(f"{product} x {aantal}")