//test
const games={
    iis:"https://games-roblox-com.translate.goog/v1/games?universeIds=4791664217&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp",
    iiaf:"https://games-roblox-com.translate.goog/v1/games?universeIds=4128847839&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp",
    rogessr:"https://games-roblox-com.translate.goog/v1/games?universeIds=6743414374&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp"
}

for (game in games){
    fetch(games[game])
    .then(data=>console.log(data))
    .catch(error=>console.error(error))
}
