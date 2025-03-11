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
        for (let i = 1; i <= num; i++) {
            output += i + " ";
            process.stdout.write(output.trim() + "\n");
        }
    } else {
        console.error("Voer een geldig getal in.");
    }

    // Sluit de readline interface af
    rl.close();
});
