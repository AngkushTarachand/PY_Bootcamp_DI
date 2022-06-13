let people = [
        "Greg",
        "Mary",
        "Devon",
        "James"];

let first_elem = people.shift() ;
console.log(first_elem) ;
console.log(people);

people.splice( people.indexOf('James'), 1, 'Jason' ) ;

people.push("Angkush") ;
console.log(people) ;

console.log(people.indexOf('Mary')) ;

let people2 = people.slice( 0 , people.indexOf('Angkush'));
console.log(people2) ;

console.log(people.indexOf('Foo')) ;

//It returns -1 because Foo is not found in the array.

let last = people.length - 1 ;
console.log(people[last]) ;

for (let i = 0; i < people.length; i++){
                console.log(people[i], i);
}


let colors = [
            "Red",
            "Lavender",
            "Vermilion",
            "Cobalt blue",
            "Purple"
];

for (let i = 0 ; i < colors.length ; i++ ){
        Position = i + 1 ;
        console.log("#" + Position + "choice is " + colors[i]);
        switch(Position){
            case(1):
                console.log(" My " + Position +"st is " + colors[i]);
                break;
            case(2):
                console.log(" My " + Position +"nd is " + colors[i]);
                break;

            case(3):
                console.log(" My " + Position +"rd is " + colors[i]);
                break;

            default:
                console.log(" My " + Position +"th is " + colors[i]);
                break;
        }

}




let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log(building.numberOfFloors);

console.log(building.numberOfAptByFloor.firstFloor + " " +
            building.numberOfAptByFloor.secondFloor + " " +
            building.numberOfAptByFloor.thirdFloor
            ) ;













