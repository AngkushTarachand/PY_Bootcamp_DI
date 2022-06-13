console.log("This is a JavaScript");

//Declare a variable
let a = 5 ;
let b =  3 ;
let even_num = 6 ;
let first_name = "Damien" ;  //snake_case style
let firstName = "Damien" ;  //camelCase style

console.log( a ) ;
console.log( b ) ;
console.log( a + b ) ;
console.log( a - b ) ;

let sum = a + b ;
console.log(sum) ;

//Update the value of the variable

a = 2 ;

console.log( a ) ;
console.log( b ) ;

console.log( sum ) ;

sum = a + b ;
console.log ( sum ) ;

b = 4 ;
console.log( sum ) ;

sum = a + b ;
console.log ( a + b ) ;

//Primitive data type
// Numbers - digits 0 - 9
// Strings - " " or ' ' or ` `
// Booleans - True or False ( 1 or 0 )
// Undefined - no value assigned
// null- speacial value that does not belong to any of the above

// Undefined
let c ;
console.log( c ) ;

// null
let d = null ;
console.log ( d ) ;

//Strings
let str = "Today is a great day!" ;

let str1 = "Hello" ;
let str2 = "World" ;

//Concatenation
 console.log( str1 + str2 ) ;

 console.log( str1 + " " + str2) ;

 console.log(`${str1} ${str2}`) ;

let str3 = "1" ;
let str4 = "3" ;
let str5 = "five" ;

// concatenation occurs
console.log( str3 + str4 ) ;
console.log( str3 + 4 )

// if the string are numbers. an arithmetic operation will occur
console.log( str3 - str4 ) ;
console.log(str3 - 4)

console.log(str3 + str5) //concatenation
console.log(str3 - str5) //NaN: not a number

// Convert a string to a number
console.log(str3) ; //string
str3 = Number(str3);
console.log( str3 ) ; //Number

 console.log(str4) ; //string
str4 = Number(str4);
console.log(str4) ; //Number

console.log(str3 + str4) ;

// String methods - in-built functions to manipulate the type
//let str1 = "Hello" ;

console.log(str1.length) ; //length property
console.log(console.log(str1.substring(1))) ; // index starts from zero
console.log(str1.indexOf('l')) ; // returns the first match
console.log(str1.indexOf('w')) ; //returns -1 means no match

console.log(str1.charAt(1)) ;



//return characters from start index up to not including value at the end index
console.log(str1.substring(1, 3)) ;
console.log(str1.substring(1, 4)) ;

console.log(str1.substring(1)) ;
//from start index till end of the string

console.log(str1.substring(5)) ;
console.log(str1.substring(6)) ;
console.log(str1.substring(4)) ;

console.log(str1.substring(
        str1.indexOf('l')
)) ;
/*
    console.log(str1.substring('index') = return characters
    if the start index of the character is unknown
    index = str1.indexOf('character')
    Hence
        console.log(str1.substring(
            str1.indexOf('e')
        ));
*/

console.log(str1.substring(
    str1.indexOf('e'), //1
    str1.indexOf('o') + 1   //4+1
     )) ;

/*
    console.log(str1.substring(
    str1.indexOf('e'),
    str1.indexOf('o')
     )) ;
    It will return - ell

    If one wants to return - ello
    either
        console.log(str1.substring(
            str1.indexOf('e')
        )) ;
    or
        console.log(str1.substring(
            str1.indexOf('e'),
            str1.indexOf('o') + 1
        )) ;
*/

console.log(str1.toLowerCase()) ;
console.log(str1.toUpperCase()) ;

//console.log(str1.replace(searchValue:'o', replaceValue:'a')) ;
//console.log(str1.replace(searchValue:'l', replaceValue:'t')) ;



console.log(str1.concat(str2)) ;
//remove blank spaces - at the end and beginning of string ;

str1 = "Hello " ;
str2 = " World " ;

console.log(str2.trim()) ;
console.log(str2.trimStart()) ;
console.log(str2.trimEnd()) ;

//Numbers

let num1 = 4 ;        //positive
let num2 = -3  ;      //negative
let pi = 3.141592653689793238; //decimal
let num3 = 100000000 ;
//Can do arithmetic operation: + - * /

console.log(num1) ;

//Convert number to string
console.log(num1.toString()) ;
//console.log(num3.toLocalString()) ;

//Decimal places
//console.log(pi.toFixed(fractionDigits: 3)) ; //begin a string in the process
//console.log(pi.toFixed(fractionDigits: 0)) ; //no decimal pl

//Check if a variable is Not a Number
console.log(isNaN(pi)) ;
//console.log(isNaN(number:"number")) ;

// Boolean - True or False
let status = true ;

console.log(status) ;
console.log(Number(status)) ;

//let expression=Boolean(value: 8>9);
//console.log(expression) ;









