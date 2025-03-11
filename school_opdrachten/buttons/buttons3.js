document.addEventListener("DOMContentLoaded", function () {
    // Aantal knoppen instellen
    const totalButtons = 30;  // Je kunt dit getal wijzigen naar 10, 15, 20, etc.
    const buttonsPerRow = 5;  // Aantal knoppen per rij
    const container = document.getElementById("container");

    // Functie om de knoppen te maken
    const createButtons = () => {
        const panel = document.createElement("div");
        panel.style.display = "grid";  // Gebruik grid voor de opmaak
        panel.style.gridTemplateColumns = `repeat(${buttonsPerRow}, 1fr)`;  // Zorg voor 5 kolommen
        panel.style.gap = "10px";  // Afstand tussen de knoppen
        panel.style.margin = "20px";
        
        for (let i = 1; i <= totalButtons; i++) {
            const button = document.createElement("button");
            button.innerText = `Button ${i}`;
            button.style.padding = "15px 20px";
            button.style.border = "none";
            button.style.fontSize = "16px";
            button.style.cursor = "pointer";
            button.style.backgroundColor = "green";
            button.style.color = "white";
            button.style.borderRadius = "5px";

            let clickCount = 0;  // Aantal klikken per knop

            // Event listener voor de kleurverandering
            button.addEventListener("click", function () {
                clickCount++;

                // Verander de kleur op basis van het aantal klikken
                if (clickCount === 1) {
                    button.style.backgroundColor = "red";
                } else if (clickCount === 2) {
                    button.style.backgroundColor = "purple";
                } else if (clickCount === 3) {
                    button.style.backgroundColor = "blue";
                } else if (clickCount === 4) {
                    button.style.backgroundColor = "black";
                } else if (clickCount === 5) {
                    button.remove();  // Verwijder de knop na 5 klikken
                }
            });

            panel.appendChild(button);
        }

        container.appendChild(panel);  // Voeg het panel toe aan de container
    };

    createButtons();  // Roep de functie aan om de knoppen te genereren
});
