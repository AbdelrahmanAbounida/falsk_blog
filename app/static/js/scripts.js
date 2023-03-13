
function startGame(){
    var counter = 0;
    document.querySelector('.play').addEventListener('click',()=>{
        counter++;
    })

    return new Promise((resolve, reject)=>{

        setTimeout(()=>{
            if (counter>5){
                resolve();
            }
            else{
                reject()
            }
        },2000)

    })
}


function restart(){
    startGame()
    .then(()=>{alert("you win")})
    .catch(()=>{alert("You lost")
})

}

document.querySelector('.restart').addEventListener('click',()=>{
    restart();
})