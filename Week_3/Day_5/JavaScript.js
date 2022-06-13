//Declare Object

let obj = {};

let students = {
        student_1: 'Joeri',
        student_2: 'Ally',
        student_3: 'Shivastav',
        student_4: 'Kadeer',
        student_5: 'Laurent',
        student_6: 'Angkush',
        student_7: 'Bruno'
}

console.log(students);

//Access value of a key inside an object
console.log(students.student_1);

console.log(students['student_1']);

let a = 'student_2' ;
console.log(students[a]);
console.log(students.student_2);


let database = {
        student_1: {
            name: 'Joeri',
            surname: 'Smissaert',
            age: 35
        },
        student_2: {
            name: 'Ally',
            surname: 'Baubooa',
            age: 24
        },
        student_3: {
            name:'Shivastav',
            surname: ' Juggoo',
            age: 24
        },
        student_5: {
            name: 'Laurent',
            surname:'Hannelas',


        },
        student_6: {
            name:'Angkush',
            surname: 'Tarachand',
            age: 19
        },
        student_7:  {
            name: 'Bruno',
            surname: 'Beche',
            age:50
        },
}
 console.log(database.student_2.age);

//Add/change object properties
database.student_2.age = 21
console.log(database);

database.student_2.laptop = 'Asus Vivobook'
console.log(database);

//delete object property
delete database.student_2.laptop ;
console.log(database);






//Exercise
let obj_credentials = {
        username: 'bruno',
        password: '123'
}

let database_2 = [obj_credentials]

console.log(database_2);

//--------------------------------//

let database_3 = [
        {
            username: 'Bruno' ,
            password: '123'
        }
]
console.log(database_3);

let newsfeed = [
        {
            username: 'username1' ,
            timeline: 'timeline1'
        },
        {
            username: 'username2' ,
            timeline: 'timeline2'
        },
        {
            username: 'username3' ,
            timeline: 'timeline3'
        }
]
 console.log(newsfeed);










