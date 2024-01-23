import React from "react";
import { SearchBar } from "./searchBar";
import { HomeIcon, GearIcon } from "@radix-ui/react-icons";
import { useLocation } from "react-router-dom";
import { Link } from "react-router-dom";
import { useSearch } from "../searchContext";

export function NavigationBar() {
  const locaton = useLocation();

  return (
    <>
      <header className="w-full bg-card px-[20px] p-5 flex h-[80px] justify-between items-center">
        <Link to="/">
          <HomeIcon className="w-[30px] h-[30px]" />
        </Link>
        {locaton.pathname === "/" && <SearchBar />}
        <Link to="/settings">
          <GearIcon className="w-[30px] h-[30px]" />
        </Link>
      </header>
    </>
  );
}
