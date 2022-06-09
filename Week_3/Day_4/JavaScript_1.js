//----------------Exercise XP--------------------//

//--------------------Exercise 1-----------------//
let x = 5 ;
let y = 2 ;

if (x>y){
        console.log("x is the biggest number");
}
else {
        console.log("y is the biggest number");
}

//----------------Exercise: Chihuahua--------------//

let newDog = "Chihuahua" ;


console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog = "Chihuahua") {
            console.log("I love Chihuahua, it's my favourite dog breed");
}
else {
            console.log("I don't care. I prefer cats");
}

//-------------Exercise 3: Even or Odd--------------//

let Num = prompt('Please enter a value for x');

let DetermineIfOddEven = Num%2 ;

switch(DetermineIfOddEven){
            case(0):
                console.log("X is an even number");
                break;
            case(1):
                console.log("X is an odd number");
                break;
}


//--------------Exercise 4:Group Chat--------------//
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

let NumOfUsers = users.length ;
console.log(NumOfUsers);

switch(NumOfUsers){
            case(0):
                console.log("No one is online");
                break;
            case(1):
                console.log( users + "is online");
                break;
            case(2):
                console.log( users + " " +  +" "+ "are online");
                break;
}
 if (NumOfUsers>2){
                let RemainderOnline = NumOfUsers - 2
                console.log( users[0] + "," + " " + users[1] + " " + "and" + " " +RemainderOnline + " more are online")
}

