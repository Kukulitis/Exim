const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'cac018b0f0mshfb0de045d8543dap144acejsn39e1183e038e',
		'X-RapidAPI-Host': 'instagram-profile1.p.rapidapi.com'
	}
};
function getUserData(){
    username=document.getElementById("name").value
}
fetch('https://instagram-profile1.p.rapidapi.com/getprofile/therock', options)
.then(response => response.json())
.then(response => console.log(response))
.catch(err => console.error(err));