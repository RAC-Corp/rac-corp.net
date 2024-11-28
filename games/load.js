const games={
    iis:"https://games.roblox.com/v1/games?universeIds=4791664217",
    iiaf:"https://games.roblox.com/v1/games?universeIds=4128847839",
    rogessr:"https://games.roblox.com/v1/games?universeIds=6743414374"
}

fetch("https://games.roblox.com/v1/games?universeIds=123069416")
    .then(data=>console.log(data))
    .catch(error=>console.error(error))