const allowedInWord = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-";
let bericht = document.getElementById("bericht");
let button = document.getElementById("submit");

// Opdracht 1
function getNumberOfCharacters(text){
    let aantalCharacters = 0;

    for (let i = 0; i < text.length; i++){
        if (i in allowedInWord){
            aantalCharacters += 1;
        }
    }

    return aantalCharacters;
}

// Opdracht 2
function getNumberOfSentences(text){
    let lst = [".", "!", "?"];
    let zinnen = 0;

    for (i = 0; i < text.length; i++){
        if (i in lst){
            zinnen += 1;
        }
    }

    return zinnen;
}

// Opdracht 3
function getNumberOfWords(text){
    return text.split().length;
}

// Opdracht 5
function getAVIScore(text){
    score = getNumberOfSentences(text) / getNumberOfWords(text);
    let aviscore;

    if (score <= 7){
        aviscore = 5;
    } else if (score > 7 && score <= 8){
        aviscore = 6;
    } else if (score > 8 && score <= 9){
        aviscore = 7;
    } else if (score > 9 && score <= 10){
        aviscore = 8;
    } else if (score > 10 && score <= 11){
        aviscore = 11;
    } else if (score > 11){
        aviscore = 12;
    }

    return aviscore;
}
