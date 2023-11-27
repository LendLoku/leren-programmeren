document.addEventListener("DOMContentLoaded", function() {
    const path = document.querySelector(".path");
    const playersContainer = document.getElementById("players");
    const rollButton = document.getElementById("roll-button");
    const gameOver = document.getElementById("game-over");
  
    const playerTokens = [
      { color: "#ff0000", position: 0 },
      { color: "#00ff00", position: 0 },
      { color: "#0000ff", position: 0 },
      { color: "#ffff00", position: 0 }
    ];
  
    let currentPlayerIndex = 0;
    let gameOverFlag = false;
  
    // Generate path spots with numbers that add up to 50 in a zigzag pattern
    let currentSpot = 1;
    let isMovingForward = true;
    for (let i = 1; i <= 50; i++) {
      const spot = document.createElement("div");
      spot.classList.add("spot");
      spot.textContent = currentSpot;
      path.appendChild(spot);
  
      if (isMovingForward) {
        currentSpot++;
        if (currentSpot === 51) {
          currentSpot = 50;
          isMovingForward = false;
        }
      } else {
        currentSpot--;
        if (currentSpot === 0) {
          currentSpot = 1;
          isMovingForward = true;
        }
      }
    }
  
    // Create player tokens
    playerTokens.forEach((player, index) => {
      const token = document.createElement("div");
      token.classList.add("player-token");
      token.style.backgroundColor = player.color;
      playersContainer.appendChild(token);
    });
  
    function rollDice() {
      if (!gameOverFlag) {
        // Disable the roll button while rolling
        rollButton.disabled = true;
  
        // Roll the dice to get a random number between 1 and 6
        const diceResult = Math.floor(Math.random() * 6) + 1;
  
        // Move the current player's token up by the dice result
        const currentPlayer = playerTokens[currentPlayerIndex];
        currentPlayer.position += diceResult;
  
        // Ensure the player stays within the board
        if (currentPlayer.position >= 50) {
          currentPlayer.position = 50;
          gameOverFlag = true;
          gameOver.textContent = `Player ${currentPlayerIndex + 1} Wins!`;
          gameOver.style.display = "block";
          rollButton.style.display = "none";
        }
  
        // Update the current player's position on the board
        const spotWidth = path.offsetWidth / 50;
        const newPosition = currentPlayer.position * spotWidth;
        playerTokens.forEach((player, index) => {
          const token = playersContainer.children[index];
          token.style.left = player.position * spotWidth + "px";
        });
  
        // Switch to the next player
        currentPlayerIndex = (currentPlayerIndex + 1) % playerTokens.length;
  
        // Enable the roll button after rolling
        setTimeout(function() {
          rollButton.disabled = false;
        }, 500);
      }
    }
  
    rollButton.addEventListener("click", rollDice);
    document.addEventListener("keydown", function(event) {
      // Check if the spacebar key is pressed
      if (event.keyCode === 32) {
        rollDice();
      }
    });
  });
  