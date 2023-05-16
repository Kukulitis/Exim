const title = document.getElementById("virsraksts")

title.innerHTML = "Sup"
title.style.color="purple"
title.style.backgroundColor="green"



const pelem= document.createElement("p")
pelem.innerHTML= "LGHDTV"
document.body.append(pelem)

const saraksts = document.createElement("ul")
const elem1 =document.createElement("li")
elem1.innerHTML= "esss"
const elem2 =document.createElement("li")
elem1.innerHTML= "tu"

saraksts.append(elem1)
saraksts.append(elem2)
document.body.append(saraksts)


var skaits = 0
const count = document.getElementById("count")
count.innerHTML = skaits

function plusOne(){
    skaits +=1
    count.innerHTML =skaits
}