//----------------Exercise 1: Your Favourite Food ---------------------//
let favourite_food = "bread" ;
let favourite_meal = "breakfast" ;
console.log("I eat "+ favourite_food + " " +"at every " + favourite_meal);


//-----------------Exercise 2: Series (Part 1)---------------------------------//
let myWatchedSeries=[
        "black mirror",
        "money heist",
        "the big bang theory"
];

let myWatchedSeriesLength = myWatchedSeries.length ;

let myWatchedSeriesSentence = "black mirror, money heist, amd the big bang theory."

console.log("I watched" + " " + myWatchedSeriesLength + " " + "series: " + myWatchedSeriesSentence)

//------------------Exercise 2: Series (Part 2) -------------------------------//
console.log(myWatchedSeries.indexOf('the big bang theory')) ;

myWatchedSeries[2] = "friends" ;
console.log(myWatchedSeries);

myWatchedSeries.push(" 2 broke girls ")
console.log(myWatchedSeries);

console.log(myWatchedSeries.unshift("13 reasons why"))


//cant delete black mirror while using pop
/*Method 1*/
        let IndexOfSeries = myWatchedSeries.indexOf('black mirror');
        console.log(IndexOfSeries);

        console.log(IndexOfSeries) ; //string
        IndexOfSeries = Number(IndexOfSeries) ;
        console.log(IndexOfSeries) ;  //number

        console.log(myWatchedSeries.pop(IndexOfSeries));
        //--------------------------------------------------------//
/*Method 2*/
        myWatchedSeries.pop(myWatchedSeries.indexOf('black mirror"'));
        console.log(myWatchedSeries);
        //----------------------------------------------------------//


        let locationMoneyHeist = myWatchedSeries.indexOf("money heist") ;
        console.log(locationMoneyHeist)
      //  console.log(locationMoneyHeist.substring[1, 2]) ;
      console.log(myWatchedSeries[locationMoneyHeist].substring[1, 2]);
        console.log(myWatchedSeries)

//-----------------------exercise 3: The temperature Converter-----------------//

let TemperatureInCelsius = 20 ;
console.log(TemperatureInCelsius);

let conversion1 = TemperatureInCelsius/5 ;
console.log(conversion1) ;

let conversion2 = conversion1*9 ;
console.log(conversion2) ;

let conversion3 = conversion2 + 32 ;
console.log(conversion3);

let TemperatureInFahrenheit = conversion3 ;

//console.log(TemperatureInFahrenheit} ;

//--------------------Exercise 4: Guess The Answers #1------------------------//
 let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: It will output 55, because a = 34 and b = 21 are numbers
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: It will output 23 because because a =2 and b = 21 amd are number
    // Actual: 23

 //Prediction: c is undefined as the variable, c is not assigned.

console.log(3 + 4 + '5')
/*Prediction:
    It will output 75 because 3 and 4 are numbers whereas 5 is defined as a string
    Hence 3 and 4 will be added up to give the sum of 7 and 5 will be placed next to 7
  Actual: 75
*/

//----------------------Exercise 5: Guess the Answers #2----------------------//
/*
typeof(15)
// Prediction: 15 is a number
// Actual:Number

typeof(5.5)
// Prediction: 5.5 is a number
// Actual:Number

typeof(NaN)
// Prediction: NaN is not a number.
// Actual: Number

typeof("hello")
// Prediction: It is a string
// Actual:String

typeof(true)
// Prediction: Boolean because it has only 2 output true or false and in not between""
// Actual: Boolean

typeof(1 != 2)
// Prediction:
// Actual:

"hamburger" + "s"
// Prediction: hamburgers because hamburger and s are string, thus concatenation occurs
// Actual: hamburgers

"hamburgers" - "s"
// Prediction: NaN as hamburgers and s are not numbers assigned as string, no arithmetic operation is carried out
// Actual: NaN

"1" + "3"
// Prediction: 13 as 1 and 3 are strings so concatenation occurs
// Actual: 13

"1" - "3"
// Prediction: -2 as numbers because 1 and 3 are numbers declared as string
// Actual: -2

"johnny" + 5
// Prediction: johnny5 because johnny is a string and 5 is a number
// Actual: johnny5

"johnny" - 5
// Prediction: NaN because johnny is not a number assigned as a string
// Actual:NaN

99 * "hello"
// Prediction: NaN: because hello is not a number declared as a string
// Actual:
NaN

1 != 1
// Prediction: false because one equals to one
// Actual: false

1 == "1"
// Prediction: == means requesting a boolean; they have the same value
// Actual: True

1 === "1"
 Prediction: Despite the value is the same but the data types are different, Boolean : false
 Actual: false
*/

console.log(typeof(15))
console.log(typeof(5.5))
console.log(typeof(NaN))
console.log(typeof("hello"))
console.log(typeof(true))
console.log(typeof(1 != 2))
console.log("hamburger" + "s");
console.log("hamburger" - "s");
console.log("1" + "3");
console.log("1" - "3");
console.log("jonny" + 5);
console.log("johnny" - 5);
console.log(99 * "hello");
console.log(1 != 1);
console.log(1 == "1");
console.log(1 === "1");


//-----------------------Exercise 6: Guess The Answers-------------------------//

//5 + "34"
// Prediction: 534
// Actual:

//5 - "4"
// Prediction: 1
// Actual: 1

//10 % 5   //10 divided by 5 is 2 the remainder is 0
// Prediction:
// Actual:

//5 % 10 //5 divided by is 0 and remainder is 5 thus
// Prediction:
// Actual:

//"Java" + "Script"
// Prediction: JavaScript
// Actual:

//" " + " "
// Prediction: There will be two spaces
// Actual: two spaces

//" " + 0
// Prediction: 0
// Actual: space followed by 0

//true + true
// Prediction: true is converted to number 1, so it will output 2
// Actual:2

//true + false
// Prediction:true is converted to a number that is 1 and false into 0
// Actual: 1

//false + true
// Prediction: true is converted to 1 and false to zero
// Actual: 1

//false - true
// Prediction: -1 because false is converted into 0 and true is converted into 1.
// Actual:-1

//!true
// Prediction: false because true is not equals to false
// Actual: false

//3 - 4
// Prediction: -1
// Actual: -1

//"Bob" - "bill"
// Prediction: NaN
// Actual: NaN

console.log(5 + "34") ;
console.log(5 - "4") ;
console.log(10 % 5) ;
console.log(5 % 10) ;
console.log("JavaScript") ;
console.log(" " + " ") ;
console.log(" " + 0 ) ;
console.log(true + true) ;
console.log(true + false) ;
console.log(false + true) ;
console.log(false - true) ;
console.log(!true) ;
console.log(3 -4 ) ;
console.log("Bob"- " bill") ;
