console.log("cart");

    let checkOut = document.querySelector("#checkOut");
    checkOut.addEventListener("click", ()=> {
        console.log("Proceeding to payment");
        let Proceed = confirm("Proceed to Payment");
        if (Proceed === true){
            alert("Thank you ");
        }
    });
        // -- == -- == --  Table  -- == -- == --//
        let ProductName = localStorage.getItem('ProductNameKey');
        console.log(ProductName);
        let NumTicket = localStorage.getItem('NumTicketKey');
        let SumTicket = localStorage.getItem('SumTicketKey');
        NumTicket = Number(NumTicket);
        SumTicket = Number(SumTicket);

//    let table = document.querySelector('sampleTable');
//    let row = document.createElement('tr');
//
//            //Table
//    let table1 = document.getElementById('sampleTable');
//    let row1 = document.createElement('tr');

//

    function displayData () {
            console.log(localStorage.getItem('CartData'));
            if(localStorage.getItem('CartData')){
                let {NameOfProduct,
                    NumOfTicket,
                    SumOfTicket} = JSON.parse(localStorage.getItem('CartData'));


                    JSON.parse(localStorage.getItem('CartData')).forEach(data =>{

                        //Create a row
                        let table = document.querySelector('sampleTable');
                         let row = document.createElement('tr');

                        //Table
                        let table1 = document.getElementById('sampleTable');
                        let row1 = document.createElement('tr');

                        let ticketItem = document.createElement('td');
                        ticketItem.textContent = ProductName;
                        row.appendChild(ticketItem);
                        //console.log(ticketItem);

                        let quantity = document.createElement('td');
                        quantity.textContent = NumTicket;
                        row.appendChild(quantity);
                        //console.log(quantity)

                        let price = document.createElement('td');
                        price.textContent = SumTicket;
                        row.appendChild(price);
                        //console.log(price)

                        let cancel = document.createElement('td');
                        cancel.textContent = "cancel";
                        row.appendChild(cancel);
                        table1.appendChild(row);

                    });

            }
    }
    displayData()



    let rowLength = document.getElementById('sampleTable').rows.length;

    //UpdatingSummary

    console.log(document.getElementById("NumItems")) ;
    let NumItems =  document.getElementById("NumItems") ;
    NumItems.innerText = rowLength - 1 ;

    console.log(document.getElementById("TotalCart")) ;
    let TotalCart =  document.getElementById("TotalCart") ;
    TotalCart.innerText = rowLength - 1 ;











