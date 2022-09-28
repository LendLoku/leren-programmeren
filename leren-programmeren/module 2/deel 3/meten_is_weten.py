a = int (input('voer een getal in voor variable a : '))
b = int (input('voer een getal in voor variable b : '))

if b > a:
    print(f'b ({b}) is groter dan a ({a})')
elif a == b:
    print(f'a ({a}) is gelijk aan b ({b})')
else:
    print(f'a ({a}) is groter dan b ({b})')
