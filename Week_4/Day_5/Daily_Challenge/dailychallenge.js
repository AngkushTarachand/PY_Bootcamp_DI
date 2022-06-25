console.log("DailyChallenge");

//
//planets = [
//    'Mercury',
//    'Venus',
//    'Earth',
//    'Mars',
//    'Jupiter',
//    'Saturn',
//    'Uranus',
//    'Neptune',
//]
//
//let section=document.getElementsByTagName('section')
//for (let planet of planets){
//    let div = document.createElement('div');
//    div.className = 'planet' ;
//    div.classList.add(planet)
//    div.textContent = planet ;
//
//
//    section.appendChild(div);
//
//}


planets_2 = {
    Mercury: [moon,moon],
    Venus:  [moon],
    Earth: [moon],
    Mars: [moon],
    Jupiter: [moon],
    Saturn: [moon],
    Uranus: [moon],
    Neptune: [moon],
}

let section = document.getElementsByTagName('section')
for (let key in planets_2){
    let div = document.createElement('div');
    div.className = 'planet' ;
    div.classList.add(key)
    div.textContent = key ;

//    ADD THE MOONS FOR EACH PLANETS
        let count = 3
        for (let moon of planets_2[key]){
            let moon_div = document.createElement('div')
            moon_div.className= "moon";
            moon_div.style.left = (50*count).toString() + 'px';
            planet_div.appendChild(moon_div)
            count++;
        }
    section.appendChild(planet_div);

}






































