console.log("Welcome to Moonguard!");

const playButton = document.querySelector(".play-btn");

playButton.addEventListener("click", function() {
    document.querySelector("#mainMenu").style.display = "none";

    document.querySelector("#gameScreen").style.display = "block";
});

//adding button logic
const baseButton = document.querySelector("#baseButton");

baseButton.addEventListener("click", function() {
    document.querySelector("#gameScreen").style.display = "none";

    document.querySelector("#baseScreen").style.display = "block";
});
