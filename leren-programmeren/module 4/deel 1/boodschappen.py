boodschappenlijst = {}
extra_invoegen_in_het_boodschappenlijstje = "ja"
while extra_invoegen_in_het_boodschappenlijstje == "ja":
    product = input("Welke product wil je toevoegen aan uw boodschappenlijst?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    
    if product not in boodschappenlijst:
        boodschappenlijst.update({product: aantal})    
    
    else:
        boodschappenlijst[product] += aantal
    extra_invoegen_in_het_boodschappenlijstje = input("Wil je nog een product toevoegen?: ").lower()

print("BOODSCHAPPENLIJST")
for aantal, product in boodschappenlijst.items():
    print(f"{product} x {aantal}")