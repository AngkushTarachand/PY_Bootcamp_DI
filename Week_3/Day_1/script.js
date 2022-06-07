console.log("This is from JS script")

// Declare a variable
let a = 5 ;
let b = 3 ;
let first_bane = "Damien" ; //Snake_case style
let firstName = "Damien" ; //camelCase style

console.log(a);
console.log(b);
console.log(a+b);
console.log(a-b);

let sum = a + b ;
console.log(sum);

//Update the value of the variable

a = 2
console.log(a) ;
console.log(b) ;
console.log(sum) ;

sum= a + b ;
console.log(sum);

b=4 ;
console.log(sum) ;


sum= a + b ;
console.log(sum);

//Primitive Data Types
//Numbers - digits 0-9
// Strings - "" or '' or ``
// Booleans - True or False (1 or 0)
// Undefined - no value assigned
// null - special value that does not belong to any of the above


//undefined
let c;
console.log(c) ;

//null
let d = null ;
console.log(d) ;

//string
let str= "Today is a great day" ;
console.log(str) ;

let str1= "Hello"  ;
let str2 = "World" ;

//Concatenation
console.log(str1  + "" + str2) ;
console.log(`${str1} ${str2}`) ;


let str3 = "1" ;
let str4 = "3" ;
let str5 = "five" ;

console.log(str3 + str4) ;
console.log(str3 + 4) ;
console.log(str3 - str4) ;
console.log(str3 - 4) ;

console.log(str3 + str5) ;
console.log(str3 - str5) ;

//Convert a string into a number
console.log(str3) ;  //number
str3 = Number(str3) ;
console.log(str3) ; //number

console.log(str4) ; //string
str4 = Number(str4) ;
console.log(str4) ;  //number

console.log(str3 + str4) ;

//string methods - in-built functions to manipulate the type
//let str1="Hello" ;

console.log(str1.length) ; //length property
console.log(str1.indexOf('o')) ; // starts from zero
console.log(str1.indexOf('l')) ; // returns the first match
console.log(str1.indexOf('w')) ; //returns -1 means no match
console.log(str1.indexOf('w'));
console.log(str1.substring(1, 3)) ; //return characters from start index up to but not including value of end index
console.log(str1.substring(1)) ; //from start index till end of string

console.log(str1.substring(str1.indexOf('e'))) ;

console.log(str1.substring(
    str1.indexOf('e'), //1
    str1.indexOf('o') + 1 // 4+ 1
    )) ;

console.log(str1.toLowerCase()) ;
console.log(str1.toUpperCase()) ;

console.log(str1.replaceALL('l', 't')) ;
console.log(str1.concat(str2)) ;
//remove blank spaces - at the end and at the beginning
console.log(str2.trim()) ;
//console,log(str2.trimStart()) ;
console.log(str2.trimEnd()) ;

//Number Methods
let num1=4; //positive
let num2= -3 //negative
let pi=3.14159265358973239 //decimal
let num3 = 10000000000
//can do arithmetic operations: + - * /
//convert to string

console.log(num1) ;
console.log(num1.toString()) ;
//console.log(1000000.toLocalString())

//Decimal places
console.log(pi.toFixed(3));
console.log(pi.toFixed(0));

//Check If a variable is not a number
console.log(isNaN(pi)) ;
//console.log(isNaN(number:"number")) ;

//Boolean - True (1) or False (2)
let status = true ;
console.log(status) ;
console.log(Number(status));

//let expression = Boolean(value: 10 > 9 );
//console.log(expression) ;

//Comparisons

/*
= means assign
== means compare value only
=== means compare and data type
*/

let var1=5; ;

let var2="5";
console.log(Boolean(var1 === var2)) ;
console.log(Boolean(var1 == var2)) ;
console.log(Boolean(var1 != var2)) ;
console.log(Boolean(var1 == var2)) ;

/*
! - Not
|| - OR
&& - AND
*/

// OR: At least one has to be true for the expression to be true
//console.log(Boolean(value:(var1<10)||(var1 === var2))) ;

// ANd: All conditions have to be true for the expression to be true
//console.log(boolean(value: (var>0) && (var == var2)));

//User Interface functions
//Alert

alert( " Please wake up guys" ) ;

//Prompt - ask user for an input
//let input = prompt(message: " Please enter your name") ;
//console.log(input) ;

//let num=prompt(message: " Please enter a number")
//num = Number(num) ;
//console.log("num") ;
//
////confirm - Ask a question ( true or false)
//let isOK= confirm("Are you confused with JavaScript?") ;
//console.log(isOK) ;






