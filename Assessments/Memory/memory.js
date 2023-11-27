plaatjeslijst = ['']
plaatjeslijst = shuffle(array) 

function shuffle(array){
    let currentindex = array.length, randomIndex;

    while (currentindex != 0) {

    randomIndex = Math.floor(Math.random() * currentindex);
    currentindex --;

    [array[currentindex], array[randomIndex]] = [array[randomIndex], array[currentindex]];
    }

    return array;
}

let button = createElement("button");
