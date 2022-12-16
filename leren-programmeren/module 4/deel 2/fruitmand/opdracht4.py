from fruitmand import fruitmand
import random

aantal = int(input("Hoeveel fruit wilt u?: "))
for f in range(aantal):
    print(random.choice(fruitmand)['name'])