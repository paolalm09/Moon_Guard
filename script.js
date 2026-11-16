console.log("Welcome to Moonguard!");

//Game Resources
let water = 100;
let oxygen = 100;
let power = 100;
let day = 1;
let missionCompleted = false;
let equipmentChosen = false;
let equipmentSetUp = 0;
let day2ChoiceMade = false;
let day3ChoiceMade = false;
let day4ChoiceMade = false;
let day5ChoiceMade = false;
let cmeShown = false;

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
    document.querySelector("#exploreScreen").style.display = "block";
});

//adding button logic
const baseButton = document.querySelector("#baseButton");

baseButton.addEventListener("click", function() {
    document.querySelector("#gameScreen").style.display = "none";
    document.querySelector("#exploreScreen").style.display = "block";

    updateDay();
    updateMission();
    updateResources();

    document.querySelector("#hudDay").textContent = "DAY " + day + " / 5";

    if (day === 1 && !cmeShown) {
        document.querySelector("#cmeEmergency").style.display = "block";
        cmeShown = true;
    }
});

function updateResources() {
    // Original mission dashboard
    document.querySelector("#waterDisplay").textContent = water;
    document.querySelector("#oxygenDisplay").textContent = oxygen;
    document.querySelector("#powerDisplay").textContent = power;

    // Exploration screen HUD
    document.querySelector("#exploreWaterDisplay").textContent = water;
    document.querySelector("#exploreOxygenDisplay").textContent = oxygen;
    document.querySelector("#explorePowerDisplay").textContent = power;
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

    document.querySelector("#day2Tasks").style.display =
    day === 2 ? "block" : "none";

    document.querySelector("#day3Tasks").style.display =
    day === 3 ? "block" : "none";

    document.querySelector("#day4Tasks").style.display =
    day === 4 ? "block" : "none";

    document.querySelector("#day5Tasks").style.display =
    day === 5 ? "block" : "none";
}


//
const bunkerChoice = document.querySelector("#bunkerChoice");
const waterWallChoice = document.querySelector("#waterWallChoice");

bunkerChoice.addEventListener("click", function() {
    water = Math.max(0, water - 10);
    power = Math.max(0, power - 20);

    document.querySelector("#resultTitle").textContent =
        "You chose the bunker!";

    document.querySelector("#resultMessage").textContent =
        "Your crew is protected from radiation. However, power and supplies are being conserved, and the base must manage rising CO2 levels.";

    document.querySelector("#cmeResult").style.display = "block";
    bunkerChoice.disabled = true;
    waterWallChoice.disabled = true;

    updateResources();
});

waterWallChoice.addEventListener("click", function() {
    water = Math.max(0, water - 20);

    document.querySelector("#resultTitle").textContent =
        "You chose water-lined walls!";

    document.querySelector("#resultMessage").textContent =
        "The water-lined walls help shield your base from radiation. Your crew can keep working, but the lower water supply means you'll need to manage water carefully.";

    document.querySelector("#cmeResult").style.display = "block";
    bunkerChoice.disabled = true;
    waterWallChoice.disabled = true;

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
        // Hide the CME after Day 1
        if (day > 1) {
            document.querySelector("#cmeEmergency").style.display = "none";
        }

        if (day === 2) {
            day2ChoiceMade = false;

            document.querySelector("#compostButton").disabled = false;
            document.querySelector("#filterButton").disabled = false;

            document.querySelector("#day2Result").textContent = "";
        }
        if (day === 3) {
            day3ChoiceMade = false;

            document.querySelector("#seedButton").disabled = false;
            document.querySelector("#foodButton").disabled = false;

            document.querySelector("#day3Result").textContent = "";
        }
        if (day === 4) {
            day4ChoiceMade = false;

            document.querySelector("#waterRecycleButton").disabled = false;
            document.querySelector("#earthMessageButton").disabled = false;
            document.querySelector("#repairButton").disabled = false;

            document.querySelector("#day4Result").textContent = "";
        }
        if (day === 5) {
            day5ChoiceMade = false;

            document.querySelector("#backupAntennaButton").disabled = false;
            document.querySelector("#repairDishButton").disabled = false;
            document.querySelector("#roverButton").disabled = false;

            document.querySelector("#day5Result").textContent = "";
        }

        missionCompleted = false;

        updateDay();
        updateMission();

        document.querySelector("#missionStatus").textContent =
            "Mission not completed yet!"
        completeMissionButton.disabled = false;
    } else {
        showEnding();
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

const compostButton = document.querySelector("#compostButton");

compostButton.addEventListener("click", function() {
    if (day2ChoiceMade) return;

    day2ChoiceMade = true;
    water = Math.max(0, water - 10);

    document.querySelector("#day2Result").textContent =
        "You chose organic compost! Your soil is enriched, but the process used some water.";

    compostButton.disabled = true;
    document.querySelector("#filterButton").disabled = true;

    updateResources();
});

const filterButton = document.querySelector("#filterButton");

filterButton.addEventListener("click", function() {
    if (day2ChoiceMade) return;

    day2ChoiceMade = true;
    power = Math.max(0, power - 10);

    document.querySelector("#day2Result").textContent =
        "You chose clean CO2 filters! Your samples are processed, but the equipment used extra power.";

    filterButton.disabled = true;
    document.querySelector("#compostButton").disabled = true;

    updateResources();
});

const seedButton = document.querySelector("#seedButton");

seedButton.addEventListener("click", function() {
    if (day3ChoiceMade) return;

    day3ChoiceMade = true;
    water = Math.max(0, water - 15);
    power = Math.max(0, power - 5);

    document.querySelector("#day3Result").textContent =
        "New seeds planted! Your greenhouse has a chance to recover, but growing crops requires water and power.";

    seedButton.disabled = true;
    document.querySelector("#foodButton").disabled = true;

    updateResources();
});

const foodButton = document.querySelector("#foodButton");

foodButton.addEventListener("click", function() {
    if (day3ChoiceMade) return;

    day3ChoiceMade = true;
    power = Math.max(0, power - 5);

    document.querySelector("#day3Result").textContent =
        "Emergency food supplies used! Your crew has food for now, but your greenhouse still needs attention.";

    foodButton.disabled = true;
    document.querySelector("#seedButton").disabled = true;

    updateResources();
});

const waterRecycleButton = document.querySelector("#waterRecycleButton");

waterRecycleButton.addEventListener("click", function() {
    if (day4ChoiceMade) return;

    day4ChoiceMade = true;
    power = Math.max(0, power + 5);

    document.querySelector("#day4Result").textContent =
        "Water recycling slowed down! This saves power, but your water supply will recover more slowly.";

    updateResources();
    disableDay4Buttons();
});

const earthMessageButton = document.querySelector("#earthMessageButton");

earthMessageButton.addEventListener("click", function() {
    if (day4ChoiceMade) return;

    day4ChoiceMade = true;
    power = Math.max(0, power - 10);

    document.querySelector("#day4Result").textContent =
        "Your message has been sent to Earth! Communication is restored, but sending it used power.";

    updateResources();
    disableDay4Buttons();
});

const repairButton = document.querySelector("#repairButton");

repairButton.addEventListener("click", function() {
    if (day4ChoiceMade) return;

    day4ChoiceMade = true;
    oxygen = Math.max(0, oxygen - 15);

    document.querySelector("#day4Result").textContent =
        "The generator has been repaired! However, the repair mission used some oxygen.";

    updateResources();
    disableDay4Buttons();
});

function disableDay4Buttons() {
    document.querySelector("#waterRecycleButton").disabled = true;
    document.querySelector("#earthMessageButton").disabled = true;
    document.querySelector("#repairButton").disabled = true;
}
//step 1
const backupAntennaButton = document.querySelector("#backupAntennaButton");

backupAntennaButton.addEventListener("click", function() {
    if (day5ChoiceMade) return;

    day5ChoiceMade = true;
    power = Math.max(0, power - 10);

    document.querySelector("#day5Result").textContent =
        "Backup antenna activated! Your base can communicate with Earth again, but the signal uses extra power.";

    updateResources();
    disableDay5Buttons();
});
//step 2
const repairDishButton = document.querySelector("#repairDishButton");

repairDishButton.addEventListener("click", function() {
    if (day5ChoiceMade) return;

    day5ChoiceMade = true;
    oxygen = Math.max(0, oxygen - 15);

    document.querySelector("#day5Result").textContent =
        "The antenna dish has been repaired! However, the astronaut used oxygen while working outside.";

    updateResources();
    disableDay5Buttons();
});

//3
const roverButton = document.querySelector("#roverButton");

roverButton.addEventListener("click", function() {
    if (day5ChoiceMade) return;

    day5ChoiceMade = true;
    power = Math.max(0, power - 5);

    document.querySelector("#day5Result").textContent =
        "The rover relay is working! Your base has restored communication using the rover.";

    updateResources();
    disableDay5Buttons();
});


function disableDay5Buttons() {
    document.querySelector("#backupAntennaButton").disabled = true;
    document.querySelector("#repairDishButton").disabled = true;
    document.querySelector("#roverButton").disabled = true;
}

function showEnding() {
    document.querySelector("#baseScreen").style.display = "none";
    document.querySelector("#endingScreen").style.display = "block";
}



// MOONGUARD - MOVEMENT & ROOM INTERACTIONS

const astronaut = document.querySelector("#astronaut");
const gameWorld = document.querySelector("#gameWorld");
const movementKeys = {};

let astronautX = null;
let astronautY = null;

const movementSpeed = 3.5;
const interactionDistance = 75;

const rooms = gameWorld.querySelectorAll(".base-room");

function getRoomName(room) {
    if (room.classList.contains("living-room")) return "Living Quarters";
    if (room.classList.contains("science-room")) return "Science Lab";
    if (room.classList.contains("greenhouse-room")) return "Greenhouse";
    if (room.classList.contains("control-room")) return "Control Room";
    return "Moon Base Room";
}

function findNearbyRoom() {
    const astronautRect = astronaut.getBoundingClientRect();
    const playerX = astronautRect.left + astronautRect.width / 2;
    const playerY = astronautRect.top + astronautRect.height / 2;

    let closestRoom = null;
    let closestDistance = Infinity;

    rooms.forEach(room => {
        const rect = room.getBoundingClientRect();

        const nearestX = Math.max(rect.left, Math.min(playerX, rect.right));
        const nearestY = Math.max(rect.top, Math.min(playerY, rect.bottom));

        const distance = Math.hypot(
            playerX - nearestX,
            playerY - nearestY
        );

        if (distance < closestDistance) {
            closestDistance = distance;
            closestRoom = room;
        }
    });

    return closestDistance <= interactionDistance ? closestRoom : null;
}


function interactWithRoom() {
    if (!nearbyRoom) {
        document.querySelector("#interactionMessage").textContent =
            "Move closer to a room to interact!";
        return;
    }

    const roomName = getRoomName(nearbyRoom);

    if (nearbyRoom.classList.contains("control-room")) {
        const panel = document.querySelector("#computerPanel");
        panel.style.display = "block";

        let missionInfo = document.querySelector("#computerMissionInfo");

        if (!missionInfo) {
            missionInfo = document.createElement("p");
            missionInfo.id = "computerMissionInfo";
            panel.appendChild(missionInfo);
        }

        missionInfo.textContent =
            "DAY " + day + ": " + missions[day].title +
            " — " + missions[day].description;

        let missionButton = document.querySelector("#openMissionDashboard");

        if (!missionButton) {
            missionButton = document.createElement("button");
            missionButton.id = "openMissionDashboard";
            missionButton.textContent = "OPEN MISSION DASHBOARD";
            panel.appendChild(missionButton);

            missionButton.addEventListener("click", function() {
                document.querySelector("#exploreScreen").style.display = "none";
                panel.style.display = "none";
                document.querySelector("#baseScreen").style.display = "block";

                updateDay();
                updateMission();
                updateResources();

                if (day === 1 && !cmeShown) {
                    document.querySelector("#cmeEmergency").style.display = "block";
                    cmeShown = true;
                }
            });
        }

        return;
    }

    const messages = {
        "Living Quarters": "Check on your crew and make sure everyone is comfortable.",
        "Science Lab": "Study lunar samples and make discoveries!",
        "Greenhouse": "Check on your plants and help them grow!"
    };

    document.querySelector("#interactionMessage").textContent =
        messages[roomName] || "You explored the " + roomName + "!";
}

document.addEventListener("keydown", function(event) {
    const key = event.key.toLowerCase();

    if (["arrowup", "arrowdown", "arrowleft", "arrowright",
         "w", "a", "s", "d"].includes(key)) {
        event.preventDefault();
        movementKeys[key] = true;
    }

    if (key === "e" && !event.repeat) {
        interactWithRoom();
    }
});

document.addEventListener("keyup", function(event) {
    movementKeys[event.key.toLowerCase()] = false;
});

window.addEventListener("blur", function() {
    for (const key in movementKeys) {
        movementKeys[key] = false;
    }
});

const closeComputer = document.querySelector("#closeComputer");

if (closeComputer) {
    closeComputer.addEventListener("click", function() {
        document.querySelector("#computerPanel").style.display = "none";
    });
}

function moveAstronaut() {
    if (gameWorld.clientWidth > 0) {
        if (astronautX === null) {
            astronautX = astronaut.offsetLeft;
            astronautY = astronaut.offsetTop;
        }

        let dx = 0;
        let dy = 0;

        if (movementKeys["arrowup"] || movementKeys["w"]) dy--;
        if (movementKeys["arrowdown"] || movementKeys["s"]) dy++;
        if (movementKeys["arrowleft"] || movementKeys["a"]) dx--;
        if (movementKeys["arrowright"] || movementKeys["d"]) dx++;

        if (dx !== 0 && dy !== 0) {
            dx *= 0.707;
            dy *= 0.707;
        }

        astronautX += dx * movementSpeed;
        astronautY += dy * movementSpeed;

        const maxX = gameWorld.clientWidth - astronaut.offsetWidth;
        const maxY = gameWorld.clientHeight - astronaut.offsetHeight;

        astronautX = Math.max(0, Math.min(astronautX, maxX));
        astronautY = Math.max(0, Math.min(astronautY, maxY));

        astronaut.style.left = astronautX + "px";
        astronaut.style.top = astronautY + "px";

        nearbyRoom = findNearbyRoom();

        const message = document.querySelector("#interactionMessage");

        if (nearbyRoom && message) {
            message.textContent =
                "Nearby: " + getRoomName(nearbyRoom) + " — Press E to interact!";
        }
    }

    requestAnimationFrame(moveAstronaut);
}

moveAstronaut();
