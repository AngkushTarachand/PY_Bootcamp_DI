console.log("Events");

let body = document.body ;

function button_click(){
    console.log('Button click');
    let h1 = document.createElement('h1');
    h1.textContent = "Button Clicked";
    body.appendChild(h1);
}



let btn2 = document.getElementById('btn-2');

//Add an event to a button
//btn2.setAttribute(online, button_click());

//btn2.onclick = button_click;

//Create Profile

let btnProfiles = document.getElementById('btn-3');
btnProfiles.onclick = createProfiles;

function createProfiles () {
    console.log('Creating profiles...');

    let py_pt_class = [
        {id: 1, user: 'Bruno', email:'bruno@coolascode.com'},
        {id: 2, user: 'Joeri', email:'joeri@coolascode.com'},
        {id: 3, user: 'Laurent', email: 'laurent@westtech.com'},
        {id: 4, user: 'Angkush', email: 'angkush@westtech.com'},
        {id: 5, user: 'Ally', email: 'ally@web.com'},
        {id: 6, user: 'Shivastav', email: 'shivastav@saweb.com'},
        {id: 7, user: 'Kadeer', email: 'kadeer@ghost.com'},
        {id: 8, user: 'Damien', email: 'damien@developers.institute'},
    ]

    let main_div = document.createElement('div');
    main_div.className = 'main';

    for (let person of py_pt_class){
        console.log(person);

        let div = document.createElement('div');
        div.className = "profiles";

        let img = document.createElement('img')
        img.setAttribute('src', `https://robohash.org/${person.id}?size=200x200`);
        div.appendChild(img);

        let h3 = document.createElement('h3');
        h3.textContent = person.user;
        div.appendChild(h3)

        let h4 = document.createElement('h4');
        h4.textContent = person.email;
        div.appendChild(h4)

        main_div.appendChild(div);
    }

    body.appendChild(main_div);
}


//Add an event Listener
btn2.addEventListener('click', function(ev){
    console.log("Button 2 has been clicked");
    ev.stopPropagation() ;

})

let row_count = 2;

function insertRow(){
    console.log('Inserting row...');
    row_count++

    let table = document.getElementById('sampleTable');
    let row = document.createElement('tr');

    let cell1 = document.createElement('td');
    cell1.textContent = `Row${row_count}cell1`;
    row.appendChild(cell1)

    let cell2 = document.createElement('td');
    cell2.textContent = `Row${row_count}cell2`;
    row.appendChild(cell2)

    table.appendChild(row);
}




