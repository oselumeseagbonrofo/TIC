function getRandomInt(min, max) 
{
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}
  
let minNumber = 1;
let maxNumber = 10;
let randomNumber = getRandomInt(minNumber, maxNumber);
let guessCount = 0;
let maxGuess = 3;
let guessButton = document.getElementById("guessButton");
function guessChecker() 
{
    let userGuess = document.getElementById("guess").value;
    if (userGuess == ""){
        document.getElementById("gameStatusMessage").innerHTML = "Please input a number"
    }
    else if  (userGuess > 10 || userGuess < 1)
    {
        document.getElementById("gameStatusMessage").innerHTML = "Please input a number between 1 and 10"
    }
    else 
    {
        if (userGuess == randomNumber)
        {
            document.getElementById("gameStatusMessage").innerHTML = "Well done!! You guessed the number";
            document.getElementById("guess").value = "";
            guessCount = 0;
            randomNumber = getRandomInt(minNumber, maxNumber);
        }
        else if (userGuess > randomNumber)
        {
            guessCount ++;
            document.getElementById("gameStatusMessage").innerHTML = `Try again. Your answer is too high. You have ${maxGuess-guessCount} attempts left`;
            document.getElementById("guess").value = "";
        }
        else
        {
            guessCount ++;
            document.getElementById("gameStatusMessage").innerHTML = `Try again. Your answer is too low. You have ${maxGuess-guessCount} attempts left`;
            document.getElementById("guess").value = "";

        }
        
        if (guessCount == maxGuess)
        {
            document.getElementById("gameStatusMessage").innerHTML = `Sorry. Your attempts have been exhausted. The final answer is ${randomNumber}`;
            guessButton.setAttribute("disabled","Try your luck");
            guessButton.style.backgroundColor="grey";
        }
    }
}

function restartGame() 
{
    guessCount = 0;
    document.getElementById("gameStatusMessage").innerHTML = "";
    document.getElementById("guess").value = "";
    guessButton.removeAttribute("disabled","Try your luck");
    randomNumber = getRandomInt(minNumber, maxNumber);
    guessButton.style.backgroundColor="rgb(94, 0, 0)";
}
