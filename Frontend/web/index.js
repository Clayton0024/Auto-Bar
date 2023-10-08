const jsonData = {
    "drinks": [
      {
        "name": "Drink 1",
        "image": "https://www.thecocktaildb.com/images/media/drink/vu8l7t1582475673.jpg"
      },
      {
        "name": "Drink 1",
        "image": "https://www.thecocktaildb.com/images/media/drink/vu8l7t1582475673.jpg"
      },
      {
        "name": "Drink 1",
        "image": "https://www.thecocktaildb.com/images/media/drink/vu8l7t1582475673.jpg"
      },
      {
        "name": "Drink 1",
        "image": "https://www.thecocktaildb.com/images/media/drink/vu8l7t1582475673.jpg"
      }
    ]
  };

  renderCards(jsonData)

  eel.expose(renderCards)
  function renderCards(cardJsonData){
  
      drinksData = parseData(cardJsonData);
  
      const container = document.getElementById('card-container');
  
      // Iterate over each drink in the JSON data
      drinksData.drinks.forEach(drink => {
        // Create a col div
        const col = document.createElement('div');
        col.className = 'col';
    
        // Create the card div
        const card = document.createElement('div');
        card.className = 'card';
        card.style.width = '18rem';
        card.style.marginTop = '30px';
    
        // Create the img element
        const img = document.createElement('img');
        img.className = 'card-img-top';
        img.style.padding = '10px';
        img.style.borderRadius = '20px';
        img.src = drink.image;
        img.alt = drink.name;
    
        // Create the card-body div
        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';
    
        // Create the h5 element
        const h5 = document.createElement('h5');
        h5.className = 'card-title';
        h5.innerText = drink.name;
    
        // Append elements to their respective parents
        cardBody.appendChild(h5);
        card.appendChild(img);
        card.appendChild(cardBody);
        col.appendChild(card);
        container.appendChild(col);
      });
  }

function parseData(data){
    return data
}

function search(searchTerm){

}

function filterDrinks(filterParams){

}

function mixDrink(drinkID){

}

