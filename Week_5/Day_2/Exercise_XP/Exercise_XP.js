console.log("Exercise XP Week 5 Day 2")

let Retrieve = document.body.children[0].firstChild;
console.log(Retrieve);

console.log(document.getElementsByTagName('h1'));
console.log(document.body.firstElementChild.children[0]);


//let parentElem = document.querySelectorAll('article');
//parentElem = document.getElementsByTagName('article');
parentElem = document.body.firstElementChild;
console.log(parentElem);

let childElem = document.querySelectorAll('p')[3]
console.log(childElem);

parentElem.removeChild(childElem);

let h1 = document.body.firstElementChild.children[0];
h1.addEventListener('click', function(ev){
    h1.style.color = 'red';
    ev.stopPropagation();
})

//let btn = document.createElement('button');
//document.appendChild(btn);

let form = document.createElement('form');
document.body.appendChild(form)

let btn = document.createElement('button');
form.appendChild(btn)

