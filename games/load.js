const games={
    iis:"https://www.roproxy.com/games/13815437071/Innovation-Inc-Spaceship-Recreation",
    iiaf:"https://www.roproxy.com/games/11646563991/Innovation-Inc-Armament-Facility",
    rogessr:"https://www.roproxy.com/games/89871600660033/RoGuessr"
}

/*for (const game in games){
    fetch(games[game])
    .then(response=>response.json())
    .then(data=>console.log(data))
    .catch(error=>console.error(error))
}*/

fetch("https://roblox.com")
    //.then(response=>response.json())
    .then(data=>console.log(data))
    .catch(error=>console.error(error))