//import react
import * as React from "react";
//drinks.json

import { DrinkCard } from "../drinkCard";

function getDrinks() {
  const drinks = require("../../drinks.json");
  return drinks;
}

function RenderDrinks() {
  const drinks = getDrinks();
  return drinks.map((drink) => {
    return (
      <DrinkCard
        key={drink.id}
        titleText={drink.name}
        descriptionText={drink.description}
        imgSrc={drink.image}
        imgAlt={drink.name}
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
