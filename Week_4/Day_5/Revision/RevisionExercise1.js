console.log("Revision");

let body = document.body

//Get div
console.log(document.body.firstElementChild);
console.log(document.body.children[0]);
console.log(document.getElementsByTagName('div')[0]);
console.log(document.querySelector('div'));
console.log(document.querySelectorAll('div')[0]);

//Get ul
//ul
console.log(document.body.firstElementChild.nextElementSibling);
console.log(document.body.children[1]);
console.log(document.getElementsByTagName('ul')[0]);
console.log(document.querySelector('ul'));
console.log(document.querySelectorAll('ul')[0]);

//2nd ul

console.log(document.body.children[1].lastElementChild);
console.log(document.getElementsByTagName('li')[1]);
console.log(document.querySelectorAll('li')[1]);

















