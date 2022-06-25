console.log("Exercise XP Week 4 Day 5");

//----------Exercise 1 ------------//

console.log(document.body.firstElementChild);
console.log(document.getElementById("container"));

console.log(document.getElementsByTagName("li")[0].innerHTML = "Richard");

console.log(document.getElementsByTagName("li")[0].innerHTML = "Angkush");

console.log(document.querySelectorAll(".list")[1].firstElementChild.innerHTML = "Angkush");

let parentElem = document.querySelectorAll('.list')[1] ;
let childElem = document.querySelectorAll('.list')[1].children[1] ;
parentElem.removeChild(childElem);

let parentElem1 = document.querySelectorAll(".list");
let addClass = parentElem1.classList.add('add');
console.log(addClass)




//----------Exercise 2 ------------//
let div0 = document.body.children[5]
let div1 = document.body.getElementsByTagName('div')[0];
div0.style.backgroundColor = 'lightblue';
div0.style.padding = '10px'

let body = document.body
console.log(body.getElementsByTagName('li')[5]);
let style1 = body.getElementsByTagName('li')[5] ;
style1.style.border = '1px solid black';

body.style.fontSize = '20px';

//------------------Exercise 3-----------------//
let SetAttribute0 = document.getElementById('navBar');
SetAttribute0.setAttribute("id", "socialNetworkNavigation");
console.log(document.getElementById('socialNetworkNavigation'));

console.log(document.getElementById('socialNetworkNavigation').children[0]) ;
let div2 = document.getElementById('socialNetworkNavigation').children[0] ;
let NewLi = document.createElement("li");
let NewContent = document.createTextNode("Log out");
div2.appendChild(NewLi) ;
div2.lastChild.appendChild(NewContent);

console.log(div2.firstElementChild.textContent);
console.log(div2.lastChild.textContent);

//------------------Exercise 4------------------//
let div3 = document.createElement("div");
//let div3.classList.add("BookLists");

document.body.appendChild(div3);

allBooks = [
    {title:"The Secret Circle", author:"L. J, Smith",  image:' ', alreadyRead:''},
    {title:"The Secret",        author:"Rhonda Byrne", image:' ', alreadyRead:''}
]
let rowcount = 0

for (i=0; i<allBooks.length; i++){
let CreateTable = document.createElement("table");
document.body.appendChild(CreateTable);
CreateTable.style.width = '100px'

let row = document.createElement("tr");
CreateTable.appendChild(row);

let cell1 = document.createElement("td");
cell1.textContext = allBooks[i][0] + " written by " + allBooks[i][1];
row.appendChild(cell1)
}

let alreadyRead = confirm("Have you read " + allBooks[0][0])

if (allBooks=true){
//    Cell1.style.color = 'red' ;
}




















