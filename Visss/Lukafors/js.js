
const colorSet = [["red","black","black"],
["black","orange","black"],
["black","black","green"],
["black","orange","black"]]
let selected = 0;
setState(selected)
function changeColor(){
    if(selected === 3){
        selected =0;
    }else{
        selected+=1;
    }
    setState(selected);
}


function setState(selected){
    for(let i =0 ; i<3;i++){
        const luks =document.getElementById('a'+(i+1))
        luks.style.backgroundColor=colorSet[selected][i]
    }
}

