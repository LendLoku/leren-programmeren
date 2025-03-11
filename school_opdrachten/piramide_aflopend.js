const readline = require("readline");

// Maak een interface voor gebruikersinvoer
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Vraag de gebruiker om een getal
rl.question("Voer een getal in: ", function(input) {
    let num = parseInt(input);

    // Controleer of de invoer een geldig getal is
    if (!isNaN(num) && num > 0) {
        let output = "";

        // Print de aflopende piramide
        for (let i = num; i >= 1; i--) {
            output = "";
            for (let j = 1; j <= i; j++) {
                output += j + " ";
            }
            process.stdout.write(output.trim() + "\n");
        }
    } else {
        console.error("Voer een geldig getal in.");
    }

    // Sluit de readline interface af
    rl.close();
});
