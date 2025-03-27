fetch('opdracht2_bijlage.json')
    .then(response => response.json())
    .then(personen => {
        console.log(personen); // Log de data om te controleren
        toonPersonen(personen);
    })
    .catch(error => console.error('Error loading JSON:', error));
