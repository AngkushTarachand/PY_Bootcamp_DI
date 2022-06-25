console.log("animation");

//let timeout; //Id for the timeout function
//function set_timeout(){
//      console.log('setting timeout...');
//
//      timeout = setTimeout(function(){
////    CODES TO BE EXECUTED AFTER TIMEOUT
//      alert("Today is a bit cold!");
//      }, 5000) //timeout in ms
//}
//
//function clear_timeout(){
//    console.log('Clearing timeout...');
//    clearTimeout(timeout);
//}
//
//
//let interval;
//
//function set_interval(){
//    console.log('setting interval...')
//    //Run repeatedly at specific interval
//
//    setInterval(function (){
//        console.log("Please do not forget to send me your project proposal")
//    }, 5000);
//}
//    //STOP THE FUNCTION AFTER A SPECIFIC TIME
//    setTimeout(function(){
//        console.log('Stopping interval');
//        clearInterval(interval);
//    }, 15000);
//
//
//function clear_interval(){
//    console.log('Clearing out');
//    clearInterval(interval);
//}


function move_it(){
    console.log('Moving the box...');

    let blue_box = document.getElementById('outer');
    let orange_box = document.getElementById('inner');

    let blue_width = blue_box.getBoundingClientRect().width;
    let orange_width = orange_box.getBoundingClientRect().width;

    let pos = 0;
    let move = setInterval(function(){
        if (pos > (blue_box-orange_box)){
            clearInterval(move)
        }
        else{
            orange_box.style.left = pos + 'px';
            orange_box.style.top = pos + 'px';
        }
        pos++;

    }, 500);
}

























