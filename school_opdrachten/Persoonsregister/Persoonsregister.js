document.addEventListener("DOMContentLoaded", function() {
    // De gegevens van de persoon in JSON-formaat (dit zou normaal geladen worden vanuit een bestand)
    const persoonGegevens = {
        "voornaam": "Piet",
        "achternaam": "Heijn",
        "nationaliteit": "Nederlandse",
        "leeftijd": 47,
        "gewicht": 86
    };

    // Het DOM-elementen selecteren waar we de gegevens in willen plaatsen
    document.getElementById("voornaam").textContent = persoonGegevens.voornaam;
    document.getElementById("achternaam").textContent = persoonGegevens.achternaam;
    document.getElementById("nationaliteit").textContent = persoonGegevens.nationaliteit;
    document.getElementById("leeftijd").textContent = persoonGegevens.leeftijd;
    document.getElementById("gewicht").textContent = persoonGegevens.gewicht;
});
