var player1RandomNum = Math.floor(Math.random() * 6) + 1;
var player2RandomNum = Math.floor(Math.random() * 6) + 1;

var player1DiceImg = "images/dice" + player1RandomNum + ".png";
var player2DiceImg = "images/dice" + player2RandomNum + ".png";

document.querySelector(".img1").setAttribute("src", player1DiceImg);
document.querySelector(".img2").setAttribute("src", player2DiceImg);

if (player1RandomNum > player2RandomNum) {
    document.querySelector("h1").textContent = "Player 1 Won!"
}   else if (player2RandomNum > player1RandomNum) {
    document.querySelector("h1").textContent = "Player 2 Won!"
}   else {
    document.querySelector("h1").textContent = "Draw!"
}