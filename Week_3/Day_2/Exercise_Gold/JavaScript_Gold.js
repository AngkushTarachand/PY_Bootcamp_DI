console.log("hello");

let Language = prompt("Which language do you speak");
console.log(Language)
Language = Language.ToLowerCase

switch(Language){
        case("french"):
            alert("Bonjour");
            break;
        case("english"):
            alert("Hello");
            break;
        case("hebrew"):
            alert("sholom");
            break;
//        case():
//           alert("01110011 01101111 01110010 01110010 01111001")
}


let grade = prompt("Enter your grade");

console.log(grade) ; //string
grade = Number(grade) ;
console.log(grade)

if ( grade > 90){
            console.log("A");
}
else if ( 80 < grade <= 90 ){
            console.log("B");
}
else if ( 70 <= grade <= 80 ){
            console.log("C");
}
else ( 70 > grade )
            console.log("D");




