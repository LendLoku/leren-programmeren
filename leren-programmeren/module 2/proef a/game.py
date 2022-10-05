print ('Welkom soldaat')
print ('We hebben jou nodig om de baas van het andere leger uit te schakelen!')

naam_soldaat = input ('Wat is uw naam soldaat? ')
print (f'{naam_soldaat} je gaat nu de bunker in van het andere leger.')
richting1 = input ('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)')

if richting1 == 'links':
    print ('U bent helaas gesneuveld')
    print (f'{naam_soldaat} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.') 
    exit ()
if richting1 == 'rechts':
    print ('U hebt de soldaat dood gemaakt hij laat ze wapen vallen')
    wapen = input ('Wil je zijn wapen (ak74) op pakken (ja/nee)')
if wapen == 'ja':
    print (f'Goed gedaan {naam_soldaat} nu heb je een wapen om je zelf te beschermen!')


