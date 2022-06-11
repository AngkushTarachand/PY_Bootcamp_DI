console.log("Loops");

//Loops
let arr = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'j',
]

console.log(arr[0]);
console.log(arr[1]);
console.log(arr[2]);
console.log(arr[3]);

//For Loops

// Starting conditions (e.g. i = 0 )
// condition to be evaluated (loop until the condition is no longer)
// increment (e.g i += 1, i++)

for (let i = 0; i< 10; i++){
    console.log(i);
}

for (let i = 3; i <= 10; i += 2){
    console.log(i);
}


for(let i = 0 ; i< arr.length; i++){
    console.log(i , arr[i]);
}


let obj = {
        user: "damien",
        email: "damien@developers.institute",
        phone: 5509123
}

for(let key in obj){
        console.log(key, obj[key]);
}

// For of - only for arrays
 for ( let val of arr){
    console.log(val);
 }


//For Each - array method
arr.forEach( i => console.log(i));

//While
//while (condition){
//        //STATEMENTS
//}

let count = 0 ;

while( count < arr.length){
    console.log(arr.length);
    if (arr[count] === 'f'){
        break;
    }
    count++;
}

//Infinite loops  - while(1) or while(true)

//let val = o;

//while(value<10){
//    console.log(val);
//}

for(let i in arr){
        if( arr[i] === 'e'){
            continue;
        }
        console.log(i, arr[i]);
}

//Do - While Loop
//Codes will be executed at least once

let day = 0;

do {
    console.log("Today is a great evening");
    day++;
}while(day>5)

//Check password example
let pw = '';
let pw_len = pw.length;

do {
    pw = prompt ("Please enter password with at least 8 characters:")
    pw_len = pw.length ;
}while(pw_len < 8 )

console.log("THank You");




for (let i = 0; i< 16; i++){
    let remainder = i%2
    if(remainder === 0 ){
        console.log(i + " is even");
    }
    else{
        console.log( i + " is odd");
    }
}


