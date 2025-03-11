document.addEventListener("DOMContentLoaded", function () {
    // Selecteer de container
    const container = document.getElementById("container");

    // Maak het panel
    const panel = document.createElement("div");
    panel.style.display = "flex";
    panel.style.justifyContent = "center";
    panel.style.alignItems = "center";
    panel.style.backgroundColor = "white";
    panel.style.padding = "20px";
    panel.style.borderRadius = "10px";
    panel.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
    panel.style.width = "200px";
    panel.style.margin = "auto";
    panel.style.marginTop = "20vh";

    // Kleuren en knoppen maken
    const colors = ["green", "red", "blue"];
    
    colors.forEach(color => {
        const button = document.createElement("button");
        button.innerText = color.charAt(0).toUpperCase() + color.slice(1);
        button.style.backgroundColor = color;
        button.style.color = "white";
        button.style.border = "none";
        button.style.padding = "10px 20px";
        button.style.margin = "5px";
        button.style.cursor = "pointer";
        button.style.borderRadius = "5px";
        button.style.fontSize = "16px";

        // Event listener om de achtergrondkleur te wijzigen
        button.addEventListener("click", function () {
            document.body.style.backgroundColor = color;
        });

        panel.appendChild(button);
    });

    // Voeg het panel toe aan de container
    container.appendChild(panel);
});