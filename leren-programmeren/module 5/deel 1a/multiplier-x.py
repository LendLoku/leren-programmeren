def multiplier(tafel):
  for nummer in range(1, 11):
    print(nummer, "x", tafel, "=", tafel*nummer)

num = input("Van welk getal wilt u de tafel zien? ")
multiplier(int(num))
  