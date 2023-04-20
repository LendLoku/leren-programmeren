def naam():
    naam = input('wat is uw naam soldaat: ')
    return naam

def Beindigt_spel(naam):
    print(f'Goed {naam} gevochten strijder.')
    exit()

def vraag_optie(prompt:str, antwoorden:list):
    while True:
        antwoord = input (prompt)
        if antwoord in antwoorden:
            return antwoord




def vraag_richting1():
    # while True:
    #     richting1 = input ('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)\n')
    #     if richting1 in ['links','rechts']:
    #         return richting1
    return vraag_optie('welke kant kies je om verder te gaan aan de linker kant staan 3 soldaten te bewaken en aan de rechterkant staat 1 soldaat (links/rechts)\n', ['links','rechts'])







def vraag_wapen():
    # while True:
    #     wapen = input ('Wil je zijn wapen (ak74) op pakken (ja/nee) \n')
    #     if wapen in ['ja','nee']:
            return vraag_optie('Wil je zijn wapen (ak74) op pakken (ja/nee) \n', ['ja','nee'])

def vraag_richting2():
    while True:
        richting2 = input ('Je komt aan de linker kant 2 soldaten tegen, rechts kom je iets tegen wat je nooit hebt gezien en rechtdoor staat er iets op je te wachten (links/rechts/rechtdoor) \n')
        if richting2 in ['links','rechts', 'rechtdoor']:
            return richting2
        
def vraag_richting3():
    richting3 = input ('Je kan kiezen tussen 3 richtingen rechtdoor, links of rechts. (links/rechtdoor/rechts)\n')
    while True:
        if richting3 == 'links':    
            print ('Je loopt een hele eind door en gaat naar links. Maar aan het einde kom je in de slaapkamer van de soldaten waar 300 soldaten nu zijn.')
            print ('Je besluit dus om nu snel terug te rennen en een andere kant kiezen')
            terug = input ('Wil je terug rennen (ja/nee)')
            if terug == 'nee':
                print ('Maar een van de 300 soldaten zag jou en rent nu achter jou aan met 60 man en schieten jou dood')
                print (f'{naam} u hebt gevochten als een echte soldaat, je zal altijd in ons hart blijven.\n') 
                exit ()
            return richting3