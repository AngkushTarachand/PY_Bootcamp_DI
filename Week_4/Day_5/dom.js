console.log("Intro to DOM");

let elem = document.getElementById('title');
//console.log(elem);
//
//elem.style.color

let body  = document.body ;
console.log(body);

console.log(body.firstChild);
console.log(body.firstElementChild.textContent);


//Using id
let div1p1 = document.getElementById('div1p1')


//Query Selector
let h1 = document.querySelector('div');
console.log(h1);

let div_query = document.querySelectorAll('div')




for (let div of div_query){
        console.log(div);
}

//Exercise 1(John and Pete)
//Get div
console.log(document.body.firstElementChild);
console.log(document.body.children[0]);
console.log(document.getElementsByTagName('div')[0]);
console.log(document.querySelector('div'));
console.log(document.querySelectorAll('div')[0]);

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

//Create Element
let elem_h2 = document.createElement('h2');
elem_h2.textContent = "It is very cold at night lately.";
console.log(elem_h2);

//Add to html page, we eed to append it to an existing element.

//div1p1.appendChild(elem_h2);
//document.appendChild(elem_h2) ;

//for (let i=0 ; i,5 ; i++){
//    let new_div = document.createElement('div');
//    new_div.style.height = '100px' ;
//    new_div.style.width = '100px' ;
//    new_div.style.border = '1px solid black';
//    new_div.style.borderRadius = '5px' ;
//    new_div.style.margin = '5px';
//    new_div.style.backgroundColor = 'yellow' ;
//    new_div.setAttribute('class', 'yellow_box') ;
//    body.appendChild(new_div)
//}

//innerText and innerHTML

let elem_txt = document.querySelector('#div2');
console.log(elem_txt);
//careful when using these teo, they override existing HTML code
//elem_txt.innerText = "<h3> Inner Text </h3>";
//elem_txt.innerHTML = "Hello there";


//Attributes
console.log(elem_txt.hasAttribute('id')) ;
console.log(elem_txt_getAttribute('id')) ;
elem_txt.setAttribute('id', 'div2-2')
console.log(elem_txt.id)
elem_txt.id = 'Damien'

elem_txt.setAttribute('username', 'admin');
elem_txt.removeAttribute('id');

//style
elem_txt.style.color = 'blue' ;
elem_txt.style.backgroundColor = 'yellow' ;

//Class
elem_txt.setAttribute('class', 'class_1');
elem_txt.setAttribute('class', 'class_2 class_3');
console.log(elem_txt.class)
elem_txt.className = 'class-0';
elem_txt.classList.add('class_4', 'class_5');


