var numOfDrumButtons = document.querySelectorAll(".drum").length;

// Making the sound function

function makeSound(event) {
    switch (event) {
        case "w":
            var tom1Sound = new Audio("sounds/tom-1.mp3");
            tom1Sound.play();
            break;
        case "a":
            var tom2Sound = new Audio("sounds/tom-2.mp3");
            tom2Sound.play();
            break;
        case "s":
            var tom3Sound = new Audio("sounds/tom-3.mp3");
            tom3Sound.play();
            break;
        case "d":
            var tom4Sound = new Audio("sounds/tom-4.mp3");
            tom4Sound.play();
            break;
        case "j":
            var snareSound = new Audio("sounds/snare.mp3");
            snareSound.play();
            break;
        case "k":
            var kickSound = new Audio("sounds/kick-bass.mp3");
            kickSound.play();
            break; 
        case "l":
            var crashSound = new Audio("sounds/crash.mp3");
            crashSound.play();
            break;   
        default:
            break;
    }
}

// Making Animation

function buttonAnimation(key) {
    var currentKey = document.querySelector("." + key);
    currentKey.classList.add("pressed");
    setTimeout(function() {
        currentKey.classList.remove("pressed");
    }, 100);
}

// Detecting button click

for (let i=0; i<numOfDrumButtons; i++) {
    document.querySelectorAll(".drum")[i].addEventListener("click", function() {
        var buttonInnerHtml = this.innerHTML;
        makeSound(buttonInnerHtml);
        buttonAnimation(buttonInnerHtml)
    });
}

// Detecting keyboard click

document.addEventListener("keydown", function(event) {
    makeSound(event.key);
    buttonAnimation(event.key);
})