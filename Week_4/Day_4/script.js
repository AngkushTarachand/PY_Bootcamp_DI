console.log("Day 4");

let arr  = ["e", "n", "t", "h", "r", "a", "l", "l", "i", "n", "g"];
let arr2 = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"] ;

console.log(arr);

function GuessLetter(){
        let Player1 = "" ;
        do
         Player1 = prompt('Enter a letter') ;

        while (!isNaN(Player1))

        console.log(Player1);

        for(let item of arr){

            if(Player1 === arr[item]){
                let Player1 = arr.indexOf[item];
                arr2.splice(item, 1, LetterEnter);
                console.log(arr2)
            }
            else
                 Player2 = prompt('Enter a letter') ;


        }
        return arr2

}
console.log(GuessLetter());