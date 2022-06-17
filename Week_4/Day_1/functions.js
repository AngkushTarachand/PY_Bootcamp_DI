console.log(" functions ") ;

function name_of_function(parameters){
        //Codes
}

let a = 1 ;
let b = 2 ;

let sum = a + b ;
console.log(sum) ;

// Normal functions
function find_sum(num1, num2) {
    let sum = num1 + num2 ;
    console.log(sum) ;
}

// Calling / Invoking a function
find_sum(a, b) ;
find_sum(2, 4) ;
find_sum(a, 5) ;

//function with a return value
function find_sum_return(num1, num2) {
    let sum = num1 + num2;
    return sum ;
}

let result = find_sum_return(a , b) ;
console.log(result) ;
console.log(find_sum_return(a, 6))

// function without any parameters
function piece_of_code () {
    console.log(a) ;
    console.log("Today is a great Monday") ;
}

piece_of_code();

//Custom function
// Take an array as parameters, return the first letter
// from each element.

let arr = [
        "Joeri",
        "Ally",
        "Shivastav",
        "Kadeer",
        "Angkush",
        "Bruno",
]

function custom_function(input) {
    //console.log(input) ;
    let output = '' ;
    for (let name of input){ //for sorted at .sort()
        //console.log(name) ;
        output += name.charAt(0) ;
    }
    return output
}

//console.log(custom_function1(arr));



//for ( i = 0 ; i < arr.length; i ++){
//        console.log(arr[i].substring(1,0))
//        let firstCharacter = arr[i].substring(1,0)
//    }


//function  MomMeGap (MomAge,  age) {
//        //ratio of my age and mom age
//        let MomAgeGap = MomAge/ age ;
//        MomAgeGap = MomAgeGap.toFixed(1) ;
//        return MomAgeGap
//}
//
//console.log(myAge(50, 19));

function parent_age(myAge) {
    let mum_age = myAge*2.6 ;
    let dad_age = mum_age*1.0;
    console.log(`My mum age is ${mum_age} and my dad age is ${dad_age}`)
}

parent_age(19) ;

function find_sum_return_missing(num1,num2){
        if(num2 === undefined){
            console.log("Error - Number missing")
            return(NaN);
        }
        let sum = num1 + num2 ;
        return sum;
}

find_sum_return_missing(10);


//function with a default parameter

function find_sum_return_default (num1 = null, num2 = null){
    let sum = NaN;
    if(num1 === null){
        console.log("No parameter passed!");

    }
    else if (num2 === null) {
        console.log("Second parameter is missing!");

    }

    else{
        sum = num1 + num2;
    }
    return sum
}

console.log(find_sum_return_default (5, 9)) ;

//Arrow Functions

sum_arrow_func = (num1, num2) => {
    let sum = num1 + num2 ;
    console.log(sum) ;
}

console.log(sum_arrow_func = (a, b)) ;


sum_arrow_func2 = (num1, num2) => console.log(num1 + num2 );

console.log(sum_arrow_func2 = ( a, b)) ;

//Object Methods

let students = {
        student_1: 'Joeri',
        student_2: 'Ally',
        student_3: 'Shivastav',
        student_4: 'Kadeer',
        student_5: 'Laurent',
        student_6: 'Angkush',
        student_7: 'Bruno',

        exercise: function() {
            console.log(`${this.student_1} has forget to complete exercise on loops:`) ;
        }
}

students.exercise();

let rectangle = {
        width: 100,
        height: 100,
        area: function (){
                return this.width * this.length ;
        }
}

console.log(rectangle.area());













