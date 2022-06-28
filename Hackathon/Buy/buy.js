console.log("Product");


console.log(document.getElementById("AddButton"));
let element = document.getElementById("AddButton");
element.addEventListener("click", Add);


function Add(){
    let sum++
    return sum
}