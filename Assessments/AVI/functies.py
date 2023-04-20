EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    #geeft terug per letter 1 nummer 
    return len(text) - text.count(" ") - text.count(",") - text.count(".") - text.count("!")

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    # Lijst met leestekens die het einde van een zin aangeven
    end_punctuations = [".", "?", "!"]

    # Totaal aantal zinnen
    num_sentences = 0

    # Loop door elk karakter in de tekst
    for char in text:
        # Als het karakter een leesteken is dat het einde van een zin aangeeft, voeg dan 1 toe aan het totale aantal zinnen
        if char in end_punctuations:
            num_sentences += 1

    # Geef het totale aantal zinnen terug
    return num_sentences

# opdracht 3
def getNumberOfWords(text: str) -> int:
    return len(text.split())

# opdracht 5
def wordsPerSentence (text: str) -> int:
    wordsPerSentence = getNumberOfSentences(text) / getNumberOfWords(text)
    if wordsPerSentence <= 7: 
        aviscore = 5
    elif wordsPerSentence == 8: 
        aviscore = 6
    elif wordsPerSentence == 9: 
        aviscore = 7
    elif wordsPerSentence == 10: 
        aviscore = 8
    elif wordsPerSentence == 11:
        aviscore = 11
    elif wordsPerSentence >= 11: 
        aviscore = 12
    return(aviscore)