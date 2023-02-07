def fibonacci(minimum: int) -> str:
        nummer1, nummer2 = 0, 1
        teller = 0
        volgorde = ""
        while teller < 100:
            if nummer1 > minimum:
                volgorde += (str(nummer1) if volgorde == "" else ", {}".format(nummer1))
                teller += 1
            laatste_2_nummers = nummer1 + nummer2
            nummer1 = nummer2
            nummer2 = laatste_2_nummers
        return volgorde


while not (amount := input("Vanaf welk nummer wilt u dat wij printen?")).isdigit():
        print("Noem een NUMMER op, bedankt.")

print (fibonacci(int(amount)))