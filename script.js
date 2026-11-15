console.log("Welcome to Moonguard!");

//Game Resources
let water = 100;
let oxygen = 100;
let power = 100;
let day = 1;
let missionCompleted = false;
let equipmentChosen = false;
let equipmentSetUp = 0;


const missions ={
    1: {
        title: "SET UP YOUR EQUIPMENT",
        description:"Keep your plants healthy and make sure your crew had enough food."
    },
    2: {
    title: "COLLECT MOON SAMPLES",
    description: "Explore the lunar surface and collect samples for research."
    },
    3: {
    title:"PROTECT YOUR GREENHOUSE",
    description: "Keep your plants healthy and make sure your crew has enough food."
    },
    4: {
    title: "CHECK YOUR POWER",
    description: "Inspect  your solar panels, batteries, and backup generator."
    },
    5:{
    title: "REPAIR COMMUNICATIONS",
    description: "Check your antenna and make sure your base can contact Earth."
    },
    6: {
    title: "MISSION COMPLETE",
    description: "Congratulations! Your lunar mission is complete!"
    }
};

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
    updateDay();
    updateMission();
});

function updateResources() {
    document.querySelector("#waterDisplay").textContent = water;
    document.querySelector("#oxygenDisplay").textContent = oxygen;
    document.querySelector("#powerDisplay").textContent = power;
}

function updateDay() {
    document.querySelector("#dayDisplay").textContent = "DAY" + day;
}

function updateMission() {
    document.querySelector("#missionTitle").textContent =
        "DAY " + day + ": " + missions[day].title;

    document.querySelector("#missionDescription").textContent = 
        missions[day].description;
    
    document.querySelector("#missionTasks").style.display =
    day === 1 ? "block" : "none";
}

function useWater() {
    if (water >= 10) {
        water = water - 10;
    } else {
        alert("Not enough water!");
    }
    
    updateResources();
}

const waterButton = document.querySelector("#waterButton");

waterButton.addEventListener("click", useWater);

const cmeButton = document.querySelector("#cmeButton");

cmeButton.addEventListener("click", function(){
    document.querySelector("#cmeEmergency").style.display = "block";
});

bunkerChoice.addEventListener("click", function(){
    water = water -10;
    power = power -20;

    document.querySelector("#resultTitle").textContent =
        "You chose the bunker";

    document.querySelector("#resultMessage").textContent = 
        "Your crew is protected from the radiation. However, power and supplies are being conserved, and the base must manage rising CO2 levels.";
    
    document.querySelector("#cmeResult").style.display = "block";
    document.querySelector("#bunkerChoice").disabled = true;
    document.querySelector("#waterWallChoice").disabled = true;
    updateResources();
});

const waterWallChoice = document.querySelector("#waterWallChoice");

waterWallChoice.addEventListener("click", function() {
    water = water - 20;

    document.querySelector("#resultTitle").textContent =
        "You chose water-lined walls!";

    document.querySelector("#resultMessage").textContent =
        "The water-lined walls help shield your base from radiation. Your crew can keep working, but the lower water supply means you'll need to manage water carefully.";

    document.querySelector("#cmeResult").style.display = "block";
    document.querySelector("#bunkerChoice").disabled = true;
    document.querySelector("#waterWallChoice").disabled = true;

    updateResources();
});

const nextDayButton = document.querySelector("#nextDayButton");

nextDayButton.addEventListener("click", function() {
    if (missionCompleted === false) {
        alert("Complete your mission before moving to the next day!");
        return;
    }

    if (day < 6){
        day = day + 1;
        missionCompleted = false;

        updateDay();
        updateMission();

        document.querySelector("#missionStatus").textContent =
            "Mission not completed yet!"
        completeMissionButton.disabled = false;
    } else {
        alert("Congratulations! You completed your Moon mission!");
    }
});

const completeMissionButton = document.querySelector("#completeMissionButton");

completeMissionButton.addEventListener("click", function(){
    if (day === 1 && equipmentSetUp < 3) {
        alert("Set up all three pieces of equipment first!");
        return;
    }
    missionCompleted = true;

    document.querySelector("#missionStatus").textContent = 
        "MISSION COMPLETED! GREAT WORK, ASTRONAUT!";
    completeMissionButton.disabled = true;
});

function setupEquipment(buttonId, equipmentName) {
    const button = document.querySelector(buttonId);

    button.addEventListener("click", function() {
        button.disabled = true;
        equipmentSetUp++;

        document.querySelector("#taskResult").textContent =
            equipmentName + " SET UP! (" + equipmentSetUp + "/3)";

        if (equipmentSetUp === 3) {
            document.querySelector("#taskResult").textContent =
                "ALL EQUIPMENT SET UP! YOU'RE READY!";
        }
    });
}

setupEquipment("#detectorButton", "Radiation detector");
setupEquipment("#telescopeButton", "Radio telescope");
setupEquipment("#antennaButton", "Communication antenna");
