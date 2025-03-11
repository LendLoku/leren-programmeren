document.addEventListener("DOMContentLoaded", function() {
    // De hoeveelheid personen die we willen weergeven (aanpasbaar)
    const aantalPersonen = 7;  // Dit kan worden aangepast naar een ander aantal, zoals 3, 5, 10, etc.

    // Functie om gegevens van meerdere personen weer te geven
    const toonPersonen = (personen) => {
        const container = document.getElementById("container");

        // Zorg ervoor dat de container leeg is voordat we nieuwe data toevoegen
        container.innerHTML = "<h1>Persoonsgegevens</h1>"; 

        // Loop door het aantal personen dat we willen weergeven
        for (let i = 0; i < aantalPersonen; i++) {
            // Verkrijg de gegevens van de huidige persoon
            const persoon = personen[i];

            // Maak een div voor elke persoon
            const persoonDiv = document.createElement("div");
            persoonDiv.classList.add("persoon");

            // Voeg de gegevens van de persoon toe aan de div
            persoonDiv.innerHTML = `
                <p><strong>Voornaam:</strong> ${persoon.voornaam}</p>
                <p><strong>Achternaam:</strong> ${persoon.achternaam}</p>
                <p><strong>Nationaliteit:</strong> ${persoon.nationaliteit}</p>
                <p><strong>Leeftijd:</strong> ${persoon.leeftijd}</p>
                <p><strong>Gewicht:</strong> ${persoon.gewicht} kg</p>
            `;

            // Voeg de div toe aan de container
            container.appendChild(persoonDiv);
        }
    };

    // Laad de JSON-gegevens (gebruik fetch voor een extern bestand)
    fetch('opdracht2_bijlage.json')
        .then(response => response.json())
        .then(personen => {
            toonPersonen(personen);
        })
        .catch(error => console.error('Error loading JSON:', error));
});
