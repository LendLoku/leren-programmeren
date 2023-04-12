def gulden_snede(n1, n2):
    # deze functie berekent de gulden snede op basis van de laatste twee getallen in de Fibonacci-reeks
    return n2 / n1

def main():
# dit is de hoofdfunctie die de fibonacci-getallen en de gulden snede berekent en afdrukt
# specificeer het aantal te berekenen fibonacci-getallen    
    num_termen = 10
    # initialiseer de eerste twee termen
    eerste_term = 0
    tweede_term = 1

    # bereken en print de Fibonacci-getallen
    for i in range(num_termen):
        print(eerste_term)

        volgende_term = eerste_term + tweede_term
        eerste_term = tweede_term
        tweede_term = volgende_term

    # bereken en print de gulden snede op basis van de laatste twee termen
    de_gulde_snede = gulden_snede(eerste_term, tweede_term)
    print("De gulden snede is:", de_gulde_snede)

if __name__ == "__main__":
    main()