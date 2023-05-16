const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'cac018b0f0mshfb0de045d8543dap144acejsn39e1183e038e',
		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
	}
};

let data=[]

function load_data(response_data){
    data=response_data
    let dropdown=document.getElementById("players")
    console.log(response_data)
    response_data.forEach(player=>{
        let options_element=document.createElement("option")
        options_element.innerHTML=player.first_name+" "+player.last_name
        options_element.value=player.id
        dropdown.append(option_element)
    })
}


fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=25', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));