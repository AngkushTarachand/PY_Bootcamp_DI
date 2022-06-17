//------Exercise 1 - The World Translator -------//

let Language = prompt("Which language do you speak");
console.log(Language)
Language = Language.ToLowerCase

if (Language == "french"){
        alert("Bonjour");
}
else if(Language == "english"){
        alert("Hello");
}
else if(Language == "hebrew"){
        alert("Sholom");
}
else{
        alert("01110011 01101111 01110010 01110010 01111001")
}

//-----------Exercise 2 - Grade Assigner-----------//
let grade = prompt("Enter your grade");

console.log(grade) ; //string
grade = Number(grade) ;
console.log(grade)

if ( grade > 90){
            console.log("A");
}
else if (90>= grade > 80 ){
            console.log("B");
}
else if ( 80 >= grade >= 70 ){
            console.log("C");
}
else{
            console.log("D");
}

//---------------Exercise 3 - Verbing ------------//

let Verb = prompt('Please enter a verb');
console.log(Verb);

VerbLength = Verb.length;
console.log(VerbLength)

PositionOfG = VerbLength - 1 ;
console.log(PositionOfG)
console.log(Verb.indexOf('g'))

PositionOfN = VerbLength - 2 ;
console.log(PositionOfN)
console.log(Verb.indexOf('n'))

PositionOfI = VerbLength - 3 ;
console.log(PositionOfI)
console.log(Verb.indexOf('i'))

console.log(Boolean( Verb.indexOf('g') == PositionOfG)) ;
console.log(Boolean( Verb.indexOf('n') == PositionOfN)) ;
console.log(Boolean( Verb.indexOf('i', PositionOfI) == PositionOfI)) ;

if (VerbLength >= 3){
        if (Verb.indexOf('g') == PositionOfG && Verb.indexOf('n') == PositionOfN && Verb.indexOf('i', PositionOfI) == PositionOfI  ){
                    console.log(Verb + "ly");
        }
        else{
                    console.log(Verb + "ing");
        }
}
else{
        console.log(Verb);
}
