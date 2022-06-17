console.log("DAy 2")

//~~~~~~~~~~~~~~~~~~~~~~Exercise 1 : Information ~~~~~~~~~~~~~~~~~~~~//

function infoAboutMe() {
    MyName = "Angkush" ;
    MyAge = 19 ;
    MyHobbies = "singing" ;
    console.log("I am " + MyName + ", " + MyAge +
    " teenager who loves " + MyHobbies)
}

console.log(infoAboutMe());

function infoAboutPerson ( personName, personAge, personFavoriteColor){
        console.log(
        "My name is " + personName + ", " +
        "You are " + personAge + ", " +
        "Your favorite color is " + personFavoriteColor
        )
}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

//------------------------Exercise 2 - Tips -----------------------//

function calculateTip() {
        AmountBill = prompt('Enter amount of bill') ;

        AmountBill = Number.AmountBill
        console.log(AmountBill);

        let Tip ['20%', '15%', '10%'];

        if (AmountBill < 50){
             return AmountBill + " + " + Tip[0]
             break;
        }
        if  ( 200 >= AmountBill >= 50)
              return AmountBill + " + " + Tip[1]
              break;

        else ( AmountBill > 200)
              return AmountBill + " + " + Tip[2]
              break;
}

console.log(calculateTip());

//----------------Finding The Number Divisible By a quotient-------//

//calculateTip()
//
//let arrNum = [] ;
//function isDivisible1() {
//
//        let Divisible = 0
//
//        for( i = 0 ; i < 500 ; i++){
//            let Remainder = i%23
//
//                if (Remainder === 0 && i>0){
//
//                    arrNum.push(i) ;
//                }
//
//        }
//}
//
//isDivisible1() ;
//console.log(arrNum) ;


let arrNum1 = [] ;
function isDivisible(divisor) {
        for(  i= 0 ; i < 10 ; i++){
            let Remainder = i%divisor
                if (Remainder === 0 && i > 0) {

                    arrNum1.push(i) ;
                }
        }
}

isDivisible(3)

//----------------------Exercise 4 : Shopping List -----------------//

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppinglist = [
        'banana' ,
        'orange' ,
        'apple'
];


function myBill() {
        let total = 0 ;

        //Loop through shopping list
        for(let item of shoppinglist){
             //console.log(item);

                //Check of item in stock
            if (stock[item] >0){
                //Add price to total
                total += prices[item];

                //update stock
                stock[item]--;
            }
        }


    console.log(stock) ;
    return total ;
}

console.log(myBill());

//------------------Exercise 6 : What's in My Wallet----------------------//

function changeEnough(itemPrice, [quart, dim, nic, pen] ){
        Total = quart*0.25 + dim*0.10 + nic*0.05 + pen*0.01 ;
    if (itemPrice <= Total){
        return true
    }
    else (itemPrice > Total)
        return false
}

console.log(changeEnough(4.25, [5, 20, 5, 0]));


//------------------------Exercise 6: Vacation Costs--------------------------//

//--------------------Hotel Cost -----------------//
function HotelCost(){
    let NumOfNight = null ;
    // let NumOfNight;
    //Declare variable to be accessible inside the whole function

    do{
        NumOfNight = prompt('Enter the number of nights you are planning to stay');
        NumOfNight = Number(NumOfNight);
        console.log(NumOfNight);
    } while (isNaN(NumOfNight) || NumOfNight<0);

    let HotelTotal = NumOfNight*140 ;

    return HotelTotal;
    //Simply use: return NumOfNights*140 ;
}

console.log(HotelCost());

//----------------------Plane Cost ---------------//
function planeRideCost() {
    let destination = "";
    //Cost of several destination
    let CostArr = [183, 220, 300];

   console.log(isNaN("Hello"));
   console.log(!isNaN("Hello"))

   //Loop to enter only string

    do
        destination = prompt('Please enter your destination');
    while (!isNaN(destination));


   //Sorting cost of different destination

    if (destination === "Paris") {
            return CostArr[0];
    }
    else if(destination === "London"){
            return CostArr[1];
    }
    else{
        return CostArr[2] ;
    }
}

console.log(planeRideCost());

//---------------------Car Cost --------------------------//
function rentalCarCost() {
    let NumOfRentDay = null;


    //Loop to enter a number
    do
        NumOfRentDay = prompt('Please enter the number of days to rent');
    while (isNaN(NumOfRentDay) || NumOfRentDay<0);

    //Discount or not
    if (NumOfRentDay<= 10){
            return  NumOfRentDay*40 ;
    }
    else (NumOfRentDay > 10)
            alert("5% discount is granted");
            return NumOfRentDay*40 - NumOfRentDay*40*0.05

}

console.log(rentalCarCost()) ;

//--------------Total Cost ---------------------------//

function totalVacationCost() {
        return console.log(
            "The hotel cost: " + HotelTotal() + " " +
            "The plane Cost: " + planeRideCost() + " " +
            "The car cost: " + rentalCarCost()
        );
}

console.log(totalVacationCost()) ;


