
function playTheGame(){


    let answer = confirm("Would you like to play the game");
    console.log(typeof(answer));
    console.log(answer);

    if(answer === false){
        alert("No problem, Goodbye!");
    }
    else if (answer){
        //Continue with the game
//        let NumEnter = prompt("Please enter a number between 0 and 10");
//        NumEnter = Number(NumEnter) ;
//        console.log(NumEnter);
//        if (isNaN(answer)){
//            alert("Sorry Not a number, Goodbye!")
//        }
//        else if (NumEnter < 0 || NumEnter > 10){
//             alert("Sorry it's not a good number")
//        }

        let userNumber = askUserNumber();
        if (isNaN(userNumber)){


//        else{
            let computerNumber = randNum(10) ;
            console.log("The Computer Number: " + computerNumber);
            compareNumbers(userNumber, computerNumber) ;
}
    }

}

function randNum(max)  {
     return Math.round(Math.random() * max)

    //with min max:
    //console.log(Math.round(Math.random() * (max-mid) + min )) ;

}

function compareNumbers(userNumber, computerNumber){

        let win = false

        for (let i= 0; i < 3 ; i++){
            if (userNumber === computerNumber){
                alert("WINNER");
                win = true;
                break;
            }
            else if (userNumber > computerNumber && i < 3){
                alert("Your number is bigger than computer number, guess again");
                userNumber = askUserNumber()
            }
            else if (userNumber < computerNumber && i < 3){
                alert("Your number is smaller than the computer's, guess again")
                userNumber = askUserNumber()
            }
        }
        if (!win){
            alert("Out of chances!")
        }
}

function askUserNumber(){


        // bonus part

        while (isNaN(NumEnter) || NumEnter < 0 || NumEnter > 10 ){
            alert("Sorry Not a number, out of range, try Again")

            let NumEnter = prompt("Please enter a number between 0 and 10");
             NumEnter = Number(NumEnter) ;
            console.log(NumEnter);
        }

//        if (isNaN(NumEnter)){
//          alert("SOrry Not a Number, Goodbye");
//          return NaN;
//          }
//          else if ( num < 0 || num. 10){
//              alert("Sorry it's not a good number, Goodbye");
//              return naN;
//          }




}



