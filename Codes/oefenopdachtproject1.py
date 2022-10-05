age = 20
pasje = 'ja'
begeleider = 'ja'
age_begeleider = 20
naam_begeleider = 'Joseph'

if age == 12: 
  print('welko')
elif  age < 12 and age_begeleider >= 20:
  print('welkom met een begeleider')
elif age <= 14 and pasje == "ja":
  print('welkom met een pasje !')
elif naam_begeleider == "Vladimir":
  print('welkom met begeleider Valdimir!') 
else:
  print('je bent niet welkom man')