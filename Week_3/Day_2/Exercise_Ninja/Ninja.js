//---------------------Exercise 1 : Exercise --------------------------->
/*
    5 >= 1
Prediction: True, because 5 is greater than 1
Actual: True

       0 === 1
Prediction: false
Actual: false

    4 <= 1
Prediction: false
Actual:

    1 != 1
Prediction: false
Actual:

    "A" > "B"
Prediction: false
Actual: false

    "B" < "C"
Prediction: true
Actual: true

    "a" > "A"
Prediction: true
Actual: truw

    "b" < "A"
Prediction: false
Actual: false

    true === false
Prediction: false
Actual:false

    true != true
Prediction: false
Actual: false
*/
//let Num = prompt('Enter a string of numbers separated by commas');
//
//console.log(Num=Number.Num);
//
//sum = 0 ;
//
//console.log(sum)
//for( i=0 ; i < Num.length ; i++ ) {
//        sum  = sum + Num[i]
//}
//
//console.log(sum);

//-----------------Exercise 3 : Finding Nemo-------//
 let sentence = prompt('Enter a sentence containing the word "Nemo"')

console.log(sentence.indexOf("Nemo"));

let PositionOfNemo = sentence.indexOf("Nemo")

if (PositionOfNemo > -1 ){
    console.log("I found Nemo at " + PositionOfNemo);
}
else {
    console.log("I can't find Nemo");
}








