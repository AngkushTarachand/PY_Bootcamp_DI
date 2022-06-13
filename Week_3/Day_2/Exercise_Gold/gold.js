//----------Exercise 1 - Favourite color---------//
let sentence = ["my","favorite","color","is","blue"];

        console.log(sentence[0] + " " + sentence[1] + " " + sentence[2] + " " + sentence[3] + " " + sentence[4]  )

//-----------Exercise 2 - Mix up ------------------//
let str1 = "mix";
let str2 = "pod";

let NewWord1 = str1.substring(0, 1) + str2.substring(1,3) ;
        console.log(NewWord1) ;

let NewWord2 = str2.substring(0, 1) + str1.substring(1,3) ;
        console.log(NewWord2) ;

let NewWord3 = NewWord1 + " " + NewWord2
        console.log(NewWord3)


//-----------Exercise 2 - Calculator ------------------//
Num1 = prompt('Enter the first number') ;
        console.log(Num1) ;
Num1 = Number(Num1) ;
        console.log(Num1) ;

Num2 = prompt("Enter the second number") ;
        console.log(Num2) ;
Num2 = Number(Num2) ;
        console.log(Num2) ;

Add = Num1 + Num2 ;
        alert('Addition of First Number and Second Number is ' + Add)

Subtract = Num1 - Num2 ;
        alert('Subtraction of First Number and Second Number is ' + Subtract)

Multiply = Num1 * Num2 ;
        alert('Multiplication of First Number and Second Number is ' + Multiply)

Divide = Num1/Num2
        alert('Division of First Number by Second Number is ' + Divide)
