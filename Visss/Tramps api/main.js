const options = {
	method: 'GET',
	headers: {
		Accept: 'application/hal+json',
		'X-RapidAPI-Key': 'cac018b0f0mshfb0de045d8543dap144acejsn39e1183e038e',
		'X-RapidAPI-Host': 'matchilling-tronald-dump-v1.p.rapidapi.com'
	}
};

    function display_quote(){
        fetch('https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote', options)
	.then(response => response.json())
	.then(response => {
        document.getElementById("text").innerHTML = response["value"]
    })
	.catch(err => console.error(err));

    }