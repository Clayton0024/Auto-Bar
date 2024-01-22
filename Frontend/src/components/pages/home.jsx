//import react
import * as React from "react";
//import requre module

import { DrinkCard } from "../drinkCard";
const drinks = require("../../../../drinks.json");

function getDrinks(numReturn) {
  return drinks.slice(0, numReturn);
}

function RenderDrinks() {
  const drinks = getDrinks(10);
  return drinks.map((drink) => {
    return (
      <DrinkCard
        key={drink.idDrink}
        titleText={drink.strDrink}
        imgSrc={drink.strDrinkThumb}
        imgAlt={""}
      />
    );
  });
}

function Home() {
  return (
    <div className="grid grid-cols-4 gap-4 m-5">
      <RenderDrinks />
    </div>
  );
}

export default Home;
