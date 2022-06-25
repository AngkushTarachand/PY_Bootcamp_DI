console.log("Exercise 2")

let body = document.body;
//Get div
//1st
console.log(document.getElementById('container'));
//2nd
console.log(body.firstElementChild);
console.log(body.getElementsByTagName('div'));
console.log(body.querySelector('div'));

//Get ul
console.log(body.querySelectorAll('ul'));
for(let elem1 of body.querySelectorAll('ul') ){
    console.log(elem1)
}

console.log(body.getElementsByClassName('list'));
for(let elem of body.getElementsByClassName('list') ){
    console.log(elem)
}

console.log(body.getElementsByTagName('li')[1]);
console.log(body.getElementsByClassName('list'));
console.log(body.querySelectorAll('ul.list > li:first-child'))

























