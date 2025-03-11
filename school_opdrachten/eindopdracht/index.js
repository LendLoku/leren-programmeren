var games = [
    {
        "title": "Counter-Strike: Global Offensive",
        "price": 0.00,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "Dota 2",
        "price": 0.00,
        "genre": "MOBA",
        "rating": 3
    },
    {
        "title": "Goose Goose Duck",
        "price": 4.99,
        "genre": "Action",
        "rating": 2
    },
    // Voeg de overige games toe zoals gegeven in je `games.json`
];

let cart = [];

// Voeg games dynamisch toe aan de pagina
function displayGames() {
    const gameListContainer = document.getElementById("game-list");
    gameListContainer.innerHTML = "";

    games.forEach((game, index) => {
        const gameDiv = document.createElement("div");
        gameDiv.classList.add("game-item");
        
        gameDiv.innerHTML = `
            <h3>${game.title}</h3>
            <p>Prijs: €${game.price}</p>
            <p>Genre: ${game.genre}</p>
            <p>Rating: ${game.rating}</p>
            <button onclick="addToCart(${index})">Voeg toe aan winkelmandje</button>
        `;
        gameListContainer.appendChild(gameDiv);
    });
}

// Voeg game toe aan winkelmand
function addToCart(index) {
    const game = games[index];
    cart.push(game);
    alert(`${game.title} is toegevoegd aan het winkelmandje`);
    updateCart();
}

// Update winkelmand
function updateCart() {
    const cartItemsList = document.getElementById("cart-items");
    const totalPriceElement = document.getElementById("total-price");
    
    cartItemsList.innerHTML = "";
    let totalPrice = 0;

    cart.forEach((game, index) => {
        const li = document.createElement("li");
        li.textContent = `${game.title} - €${game.price}`;
        cartItemsList.appendChild(li);
        totalPrice += game.price;
    });

    totalPriceElement.textContent = totalPrice.toFixed(2);
}

// Bereken de prijs en laat het winkelmandje zien
document.getElementById("calculate-price").addEventListener("click", function() {
    document.getElementById("game-list").style.display = "none";
    document.getElementById("cart").style.display = "block";
});

// Filters toepassen
document.getElementById("price-filter").addEventListener("input", filterGames);
document.getElementById("genre-filter").addEventListener("change", filterGames);
document.getElementById("rating-filter").addEventListener("input", filterGames);

function filterGames() {
    const maxPrice = parseFloat(document.getElementById("price-filter").value) || Infinity;
    const genre = document.getElementById("genre-filter").value;
    const minRating = parseInt(document.getElementById("rating-filter").value) || 1;

    const filteredGames = games.filter(game => {
        return game.price <= maxPrice && 
               (genre === "" || game.genre === genre) &&
               game.rating >= minRating;
    });

    displayFilteredGames(filteredGames);
}

// Toon de gefilterde games
function displayFilteredGames(filteredGames) {
    const gameListContainer = document.getElementById("game-list");
    gameListContainer.innerHTML = "";

    filteredGames.forEach((game, index) => {
        const gameDiv = document.createElement("div");
        gameDiv.classList.add("game-item");
        
        gameDiv.innerHTML = `
            <h3>${game.title}</h3>
            <p>Prijs: €${game.price}</p>
            <p>Genre: ${game.genre}</p>
            <p>Rating: ${game.rating}</p>
            <button onclick="addToCart(${index})">Voeg toe aan winkelmandje</button>
        `;
        gameListContainer.appendChild(gameDiv);
    });
}

// Initialiseer met alle spellen
displayGames();
