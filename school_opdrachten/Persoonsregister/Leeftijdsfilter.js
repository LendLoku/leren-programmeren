document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("container");

    // Functie om gegevens van meerdere personen weer te geven
    const toonPersonen = (personen) => {
        // Zorg ervoor dat de container leeg is voordat we nieuwe data toevoegen
        container.innerHTML = "<h1>Persoonsgegevens</h1>";
        
        // Voeg het invoerveld en de knop toe
        const leeftijdInput = document.createElement("input");
        leeftijdInput.type = "number";
        leeftijdInput.id = "leeftijdInput";
        leeftijdInput.placeholder = "Voer een leeftijd in";
        
        const filterButton = document.createElement("button");
        filterButton.textContent = "Toon personen ouder dan opgegeven leeftijd";
        filterButton.id = "filterButton";

        container.appendChild(leeftijdInput);
        container.appendChild(filterButton);
        
        // Maak een functie om de gefilterde personen te tonen
        const filterPersonen = () => {
            const leeftijd = parseInt(leeftijdInput.value);

            // Leeg de container en toon alleen de gefilterde personen
            container.innerHTML = "<h1>Persoonsgegevens</h1>";
            container.appendChild(leeftijdInput);
            container.appendChild(filterButton);
            
            // Filter de lijst van personen die ouder zijn dan de opgegeven leeftijd
            const gefilterdePersonen = personen.filter(persoon => persoon.leeftijd > leeftijd);

            gefilterdePersonen.forEach(persoon => {
                const persoonDiv = document.createElement("div");
                persoonDiv.classList.add("persoon");
                persoonDiv.innerHTML = `
                    <p><strong>Voornaam:</strong> ${persoon.voornaam}</p>
                    <p><strong>Achternaam:</strong> ${persoon.achternaam}</p>
                    <p><strong>Nationaliteit:</strong> ${persoon.nationaliteit}</p>
                    <p><strong>Leeftijd:</strong> ${persoon.leeftijd}</p>
                    <p><strong>Gewicht:</strong> ${persoon.gewicht} kg</p>
                `;
                container.appendChild(persoonDiv);
            });
        };

        // Voeg eventlistener toe voor de knop
        filterButton.addEventListener("click", filterPersonen);
    };

    // Laad de JSON-gegevens (gebruik fetch voor een extern bestand)
    fetch('opdracht2_bijlage.json')
        .then(response => response.json())
        .then(personen => {
            toonPersonen(personen);
        })
        .catch(error => console.error('Error loading JSON:', error));
});
