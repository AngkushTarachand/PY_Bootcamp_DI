console.log("Forms");

let login_form = document.forms.login ;
console.log(login_form);

//Other ways of accessing forms
console.log(document.forms[0]);
console.log(document.getElementsByTagName('form')[0]);
console.log(document.querySelector('form'));
console.log(document.querySelectorAll('form')[0]);

//Get the first element of the form
console.log(login_form.firstElementChild);
console.log(login_form.children[0]);
console.log(login_form.elements.username);
console.log(login_form.elements[0]);
console.log(login_form.elements['username']);

//change the name attribute in form
login_form.elements['username'].setAttribute('name', 'Damien');

//Get element by id
let user_name = document.getElementById('username');
console.log(user_name);

//Set tge value of the input
user_name.value = "Damien";

//Stop the page from refreshing - prevent the default behaviour
login_form.addEventListener('submit', (ev)=>{
        ev.preventDefault();
})

//function to retrieve data
function getData(){
        let user = document.getElementById('username').value;
        let pw = document.getElementById('password').value;
        console.log(user, pw);
}

//Event Listener for input (when typing)

user_name.addEventListener('input', function(ev:Event){
        console.log(user_name.value);
})