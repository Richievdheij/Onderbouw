var btn = document.createElement('button'); // Make button
btn.style.margin = '10px'; // Button size
btn.innerHTML = "Light switch on" // Button text
document.body.appendChild(btn); // Add the button to the browser
console.log("Light is off")
document.body.style.backgroundColor = "black"


// Changes the browser with the users input
btn.onclick = function(){
    if (btn.innerHTML == "Light switch on") {
        btn.innerHTML = "Light switch off";
        document.body.style.backgroundColor = "yellow"
        console.log("Light is on")
    }
    
    else {
        btn.innerHTML = "Light switch on";
        document.body.style.backgroundColor = "black"
        console.log("Light is off")
    }
}