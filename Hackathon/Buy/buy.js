console.log("Product");


console.log(document.getElementById("AddButton"));
let element = document.getElementById("AddButton");
//element.addEventListener("click", Add);


let plus= document.querySelector(".plus"),
    minus = document.querySelector(".minus")

    num = document.querySelector(".num");
   let a = 0;
   let SumTicket = 0 ;
   plus.addEventListener("click", ()=>{
        a++;
        a = (a < 10 ) ? "0" + a : a ;
        num.innerText = a ;
        console.log(a);
         SumTicket = a*100 ;
         console.log(document.getElementById("total")) ;
         let element1 =  document.getElementById("total") ;
         element1.innerText = SumTicket ;
         console.log(SumTicket);
   });

   minus.addEventListener("click", ()=>{
        a--;
        a = (a < 10 ) ? "0" + a : a ;

        if (a > 0 ){
            num.innerText = a ;
            console.log(a);
        }else {
                a=0;
        }
         SumTicket = a*100 ;
         console.log(document.getElementById("total")) ;
         let element1 =  document.getElementById("total") ;
         element1.innerText = SumTicket ;
         console.log(SumTicket);
   });

   SumTicket = a*100 ;
   console.log(document.getElementById("total")) ;
   let element1 =  document.getElementById("total") ;
   element1.innerText = SumTicket ;

let cart = document.querySelector(".cart");
    cart.addEventListener("click", ()=> {
    console.log("adding to cart");
    let table = document.createElement("table");
    let tr = document.createElement("tr");
    let td = document.createElement("td");

    table.appendChild(tr);
    table.appendChild(td);
    td.innerText = "Phone" ;

    console.log(table);

    });


    let table = document.createElement("table");
    let tableBody = document.createElement("tbody");
    let tr = document.createElement("tr");
    let td = document.createElement("td");

    document.appendChild(table);
    table.appendChild(tableBody);
    tableBody.appendChild(tr) ;
    tr.appendChild(td);

    td.innerText = "Phone";

//    let Product[
//            {id: 1, name: , numOfTicket: a ,sum: SumTicket },
//            {id: 2, name:}
//      ];
//

