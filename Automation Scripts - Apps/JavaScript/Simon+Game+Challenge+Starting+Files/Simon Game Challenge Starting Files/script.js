var buttonsList = ["green", "red", "yellow", "blue"];

var patternList = [];
var userPattern = [];

started = false;
var level = 1;

function playSound(color) {
    var audio = new Audio("sounds/" + color + ".mp3");
    audio.play();
} 

function startOver() {
    level = 0;
    patternList = [];
    started = false;
}

function newPattern() {
    // Making the pattern
    $("#level-title").text("Level " + level);
    var randomButtonNumber = Math.floor(Math.random() * 4);
    var randomButton = buttonsList[randomButtonNumber];

    playSound(randomButton);

    $("#" + randomButton).addClass("pressed");
    setTimeout(function() {
        $("#" + randomButton).removeClass("pressed");
    }, 250)

    patternList.push(randomButton);
    userPattern = [];
}    
    
function checkResult(currentLevel) {
    // Checking if pattern list is equal to user's pattern
    if (patternList[currentLevel] === userPattern[currentLevel]) {
        if (patternList.toString() === userPattern.toString()) {
            setTimeout(function() {
                level ++;
                newPattern();
                }, 1000);
        }
    } else {
        $("#level-title").text("Game Over, Press Any Key to Restart");
        $("body").addClass("game-over")
        setTimeout(function(){
            $("body").removeClass("game-over")
        }, 250)
        startOver();
    }
}

$(document).keypress(function(event) { 
    if (!started) {
        level = 1;
        $("#level-title").text("Level " + level);
        patternList = []
        newPattern();
        started = true;
    }
});

$(".btn").click(function(event) { 
    // Getting user pattern
    var userButton = this.id;
    userPattern.push(userButton);    

    playSound(userButton);

    $("#" + userButton).addClass("pressed");
    setTimeout(function() {
        $("#" + userButton).removeClass("pressed")
    }, 150);
    
    checkResult(userPattern.length - 1)
});