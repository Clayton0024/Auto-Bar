import * as React from "react";
import { DrinkCard } from "../drinkCard";
const drinks = require("../../../../drinks.json");
import { useSearch } from "../../searchContext";

function getDrinks() {
  return drinks;
}

function normalizeString(str) {
  return str.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
}

function smartSearch(drinks, query) {
  const normalizedQuery = normalizeString(query);

  if (!normalizedQuery) {
    return drinks;
  }

  return drinks.filter((drink) =>
    normalizeString(drink.strDrink).includes(normalizedQuery)
  );
}

function RenderDrinks({ searchQuery }) {
  const allDrinks = getDrinks();
  const [drinksToShow, setDrinksToShow] = React.useState(allDrinks);

  React.useEffect(() => {
    const filteredDrinks = searchQuery
      ? smartSearch(allDrinks, searchQuery)
      : allDrinks;
    setDrinksToShow(filteredDrinks);
  }, [searchQuery]);

  return drinksToShow.map((drink) => (
    <DrinkCard
      key={drink.idDrink}
      titleText={drink.strDrink}
      imgSrc={drink.strDrinkThumb}
      imgAlt={drink.strDrink}
    />
  ));
}

function Home() {
  const { searchQuery } = useSearch();

  return (
    <div className="grid grid-cols-4 gap-4 m-5">
      <RenderDrinks searchQuery={searchQuery} />
    </div>
  );
}

export default Home;
