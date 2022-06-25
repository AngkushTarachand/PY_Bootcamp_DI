function playTheGame(){
     let answer = confirm("Would you like to play the game");

     if (answer === false){
        alert("No problem, Goodbye!")
     }
     else if (answer){
            let NumEnter = prompt("Enter a number between 0 and 10");

            NumEnter = Number.NumEnter

            if (isNaN(NumEnter)){
                alert("Sorry Not a Number, Goodbye");
            }
            else if (NumEnter < 0 || NumEnter > 10 ){
                alert("Sorry, it's not a good number ")
            }
            else {
                let computerNumber = randNum(10) ;
                console.log("Computer Number: " + computerNumber);
            }
     }
}

function randNumBetween(max){
    console.log(Math.round(Math.random() * max))
    //with min max;

    //console.log(Math.round(Math.random() * (max-min) + min))
}

function compareNumbers(userNumber, computerNumber){
        if ( userNumber === computerNumber){
            alert("Winner.")

        }
        else {
            do
                if(userNumber > computerNumber){
                    alert: ("Your number is bigger then the computer’s, guess again ");
                    NumEnter = prompt("Enter a new number")
                    NumEnter = Number.NumEnter
                    break;
                }

                else if(userNumber < computerNumber){
                    alert("our number is smaller then the computer’s, guess again");
                    NumEnter = prompt("Enter a new number")
                    NumEnter = Number.NumEnter
                    break;

                }

            while(i=0 ; i<3 ; i++);
            alert("Out of chances" );
        }
}

