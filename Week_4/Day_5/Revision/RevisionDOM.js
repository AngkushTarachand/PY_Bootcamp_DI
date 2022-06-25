console.log("Revision on DOM");

let elem = document.body;
console.log(elem);

//Accessing DOM elements
elem = document.getElementById('title');
console.log(elem);

elem.style.color = 'red';
elem.innerText = 'Welcome to DOM';
elem.style.backgroundColor = 'blue';


let body = document.body;
console.log(body);

console.log(body.firstChild);   //first node
console.log(body.firstElementChild); //first element

console.log(body.firstElementChild.textContent);
//childNote returns nodes: Element nodes, text nodes and comment nodes
//Whitespace between elements are also text nodes.

console.log(body.childNodes);  //retrieve all nodes
console.log(body.children);    //retrieve elements only

console.log(body.children[0]);
console.log(body.childNodes[1]);


//retrieve div1-p1
console.log(body.children[1].firstElementChild);

//Using Id
let div1p1 = document.getElementById('div1-p1');
console.log(div1p1);

//Using tag
let divs = document.getElementsByTagName('div');
for (let div of divs){
    console.log(div)
}
console.log(divs);


divs = document.getElementsByTagName('h1');
console.log(divs[0]);

//Using  class
let reds = document.getElementsByClassName('red');
for (let red of reds){
    console.log(red);
}

//Query Selector
let h1 = document.querySelector('h1');
console.log(h1);

 h1 = document.querySelector('div');
console.log(h1);

let div_query = document.querySelectorAll('div');
for (let div of div_query){
    console.log(div)
}

div_query = document.querySelectorAll('div p');
//'h1 + div', 'h1 ~ div', 'div', 'div p', 'div > p'
for (let div of div_query){
    console.log(div)
}
















