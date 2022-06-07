//console.log("arrays") ;

//Array - List of Values
let students = [
    "Angkush",
    "Joeri",
    "Laurent",
    "Kadeer",
    "Shrivastav",
    "Ally",
    "Bruno",
    "Yeshna"
    ];

//console.log(student.length) ;

//get an element from an array
console.log(students[0]) ;
console.log(students[1]) ;
console.log(students[2]) ;
console.log(students[3]) ;
console.log(students[4]) ;
console.log(students[5]) ;
console.log(students[6]) ;

//Get the number of elements inside an array
console.log(students.length) ;

//update an element in array
// Joeri to Yuri

students[1]='Yuri';
console.log(students)

//Add a new element inside an array
//(at the last position
//students[7] = 'Damien' ;
students[students.length] = 'Damien';
students[students.length] = 'Abraham';
console.log(students ) ;

students[12]= 'Emilie' ;
console.log(students);
console.log(students[10])

//Nested Arrays
 let student_array = [
 ["Angkush", 19],
 ["Joeri", 35],
 ["Laurent", 34,[]],
 ["Shrivastav", 24],
 ["Kadeer", 24],
 ["Ally", 24],
 ["Bruno", 50 ],
 ]

 console.log(student_array) ;
 //console.log(student[0]) ;

 let student_0 = student_array[0] ;
 console.log(student_0[0]) ;

console.log(student_array[0][1]) ;
//console.log(student[2][2][0]) ;

//Array Methods
//Add  an element at the last position
//student.push("Ben") ;
console.log(students) ;


//Remove element at the last position
//student.pop() ;
console.log(students) ;

//Splice method
const months = ['Jan', 'March', 'April', 'June'];
months.splice(1, 0, 'Feb');
console.log(months) ;

months.splice (4, 1, 'May' )
console.log(months) ;

months.splice(2) ;
console.log(months) ;

let months_splice = months.splice(2)
console.log(months_splice)

//Slice methods
const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

console.log(animals.slice(2));

//Convert an array into a string
console.log(students.toString())

let arr=['a', 'b', 'c', 'd'] ;
console.log(arr.toString) ;
console.log(arr.join(" "))
console.log(arr.join("+"))
console.log(arr.join("-"))

//Convert string to array
let str = "Bruno" ;
console.log(str) ;

let str_arr = str.split('') ;
console.log(str_arr) ;

str = "Bruno Beche" ;
console.log(str) ;

 str_arr = str.split('') ;
console.log(str_arr.join(' ')) ;

//To delete an item from an array
console.log(arr) ;
delete arr[0];
console.log(arr) ;

//shift - Remove the first element from the array
let arr_2 = [1, 2, 3, 4, 5];

let first_elem = arr_2.shift() ;
console.log(first_elem) ;
console.log(arr_2) ;

//unshift - add element at the beginning
console.log(arr_2.unshift(0)) ; ///returns the new array length
console.log(arr_2)

