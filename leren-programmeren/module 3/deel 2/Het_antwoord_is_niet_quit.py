Fouten = 0
while True:
    vraag = input("? ")
    if vraag == "quit":
        print(Fouten)
        break
    else:
        Fouten += 1
        