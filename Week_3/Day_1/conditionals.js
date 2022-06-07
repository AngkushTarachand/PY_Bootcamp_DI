console.log("Conditionals")

let a = 1 ;

//Only the If statement
/*if (expression){
        //execute your code
};
*/

console.log("Before If statement") ;
if(a>0){
        //execute your code
        console.log("a is greater than zero");
};

console.log("After If statement")


console.log("Before If statement") ;
if(a>10){
        //execute code if expression is true
        console.log("a is greater than ten");
}
else{
        //execute code if expression is false
        console.log("a is not greater than ten")
}
console.log("After If statement")

//-------------------------------------------//
console.log("Before If statement") ;
if(a>0){
        //execute code if expression is true
        console.log("a is greater than zero");
}
else{
        //execute code if expression is false
        console.log("a is not greater than ten")
}
console.log("After If statement")
//------------------------------------------//

console.log("Before If statement") ;
a= 4
if(a > 0){
        console.log("a is greater than zero");
}
else if ( a < 0 ){
        console.log("a is not smaller than ten");
}
else if (a === 0 ){
        console.log("a is equal to zero");
}
else{
        console.log("An expected error happened")
        if (isNaN(a)){
            console.log(" 'a' is not a number. Please check the data type")
        }
}
console.log("After If statement")

//-----------------------------------//
//driving exercise

let age = prompt('How old are you?')

console.log(age) ; //string
age = Number(age) ;
console.log(age) ;  //number

if (age < 18 ){
    console.log("Powering Off") ;
}
else if ( age == 18 ) {
    console.log("Congratulations");
}
else {( age > 18)
    console.log("Powering on ");
}

//----------------------------------//
let x = 5 ;
let y = 2 ;

if (x > 2){
        console.log("x is biggest");
};


//-----------------------------------//

let c = 1 ;
switch(c){
    case 0:
        console.log(0);
        break;
    case 1:
        console.log(1);
        break;
    case 2:
        console.log(2)
        break;
    default:
        console.log("c is none of the above")
}





