sumkcal=0
sumfat=0
amm=parseInt(document.getElementById("ammount").value)

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '74917ec3d3msh73c898df7ed9c9cp16283ajsn073ef96f9b41',
		'X-RapidAPI-Host': 'edamam-food-and-grocery-database.p.rapidapi.com'
	}
};
    


function add(){
    food=document.getElementById("food").value
    amm=document.getElementById("ammount").value
    fetch('https://edamam-food-and-grocery-database.p.rapidapi.com/parser?ingr='+food, options)
        .then(response => response.json())
        .then(response => {
            console.log(response)
            sumkcal += (response.parsed[0].food.nutrients.ENERC_KCAL/100*amm)
            document.getElementById("kcall").innerHTML = Math.round(sumkcal)
            kcal = (response.parsed[0].food.nutrients.ENERC_KCAL/100*amm)
            document.getElementById("onekcall").innerHTML = Math.round(kcal)
            sumfat += (response.parsed[0].food.nutrients.FAT/100*amm)
            document.getElementById("fat").innerHTML = Math.round(sumfat)
            fat = (response.parsed[0].food.nutrients.FAT/100*amm)
            document.getElementById("onefat").innerHTML = Math.round(fat)

            table = document.getElementById("table")

            row = document.createElement('tr')

            td1 = document.createElement('td')
            td1.innerHTML = food
            td2 = document.createElement('td')
            td2.innerHTML = Math.round(kcal/100*amm)
            td3 = document.createElement('td')
            td3.innerHTML = Math.round(fat/100*amm)
            td4 = document.createElement('td')
            td4.innerHTML = amm
            

            
            row.append(td1)
            row.append(td2)
            row.append(td3)
            row.append(td4)
            var poga=document.createElement("td")
            poga.innerHTML="<button class=\"initt\" onclick=\"removeRow(this)\">Remove</button>"
            row.append(poga)
            table.append(row)

        })
        .catch(err => console.error(err));
}


const form = document.querySelector('form');
		const genderSelect = document.getElementById('gender');
		const ageInput = document.getElementById('age');
		const heightInput = document.getElementById('height');
		const weightInput = document.getElementById('weight');
		const activitySelect = document.getElementById('activity-level');
		const caloriesOutput = document.getElementById('calories');

		form.addEventListener('submit', (event) => {
			event.preventDefault(); 

			let bmr = 0;
			if (genderSelect.value === 'male') {
				bmr = 88.36 + (13.4 * weightInput.value) + (4.8 * heightInput.value) - (5.7 * ageInput.value);
			} else {
				bmr = 447.6 + (9.2 * weightInput.value) + (3.1 * heightInput.value) - (4.3 * ageInput.value);
			}

			const activityFactors = {
				'sedentary': 1.2,
				'lightly-active': 1.375,
				'moderately-active': 1.55,
				'very-active': 1.725,
				'extra-active': 1.9
			};
			const activityFactor = activityFactors[activitySelect.value];
			const calories = Math.round(bmr * activityFactor);

			caloriesOutput.textContent = calories;
		});

        function removeRow(button) {
			var row = button.parentNode.parentNode;
			row.parentNode.removeChild(row);
            cal=parseInt(row.children.item(1).innerHTML);
            fatt=parseInt(row.children.item(2).innerHTML);

            console.log("cal:",cal) 
            console.log("sumkcal:",sumkcal)

            sumkcal -= kcal/100*amm
            document.getElementById("kcall").innerHTML = Math.round(sumkcal)
            console.log("fatt:",fatt)
            console.log("fat:",fat)
            fat=fat-fatt
            document.getElementById("fat").innerHTML = Math.round(fat)
		}
