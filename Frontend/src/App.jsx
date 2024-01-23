import { NavigationBar } from "./components/navigation-bar";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./components/pages/home";
import Settings from "./components/pages/settings";
import { Separator } from "./components/ui/separator";
import { SearchProvider } from "./searchContext";

function App() {
  return (
    <>
      <BrowserRouter>
        <SearchProvider>
          <NavigationBar />
          <Separator className="w-9/10 bg-primary" />
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
