import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";

import { NavigationBar } from "./components/navigation-bar";
import { HashRouter, Route, Routes } from "react-router-dom";
import Home from "./components/pages/home";
import Settings from "./components/pages/settings";

function App() {
  return (
    <>
      <BrowserRouter>
        <SearchProvider>
          <NavigationBar />
          <Separator className="w-9/10 bg-primary sticky top-[80px]" />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="/*" element={<Home />} />
          </Routes>
        </SearchProvider>
      </BrowserRouter>
    </>
  );
}

export default App;
