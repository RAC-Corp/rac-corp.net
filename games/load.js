const games={
    iis:"https://games.roproxy.com/v1/games?universeIds=4791664217",
    iiaf:"https://games.roproxy.com/v1/games?universeIds=4128847839",
    rogessr:"https://games.roproxy.com/v1/games?universeIds=6743414374"
}

for (const game in games){
    fetch(games[game])
    .then(data=>console.log(data))
    .catch(error=>console.error(error))
}
