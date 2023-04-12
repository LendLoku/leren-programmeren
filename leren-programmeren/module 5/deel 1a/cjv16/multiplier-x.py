def multiplier(tafel):
  for nummer in range (1,11):
    print(nummer, 'x', tafel, '=', tafel*nummer)
  
num = input('welk nummer wilt u invoeren? ')

multiplier(int(num))