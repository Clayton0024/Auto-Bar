import { NavigationBar } from "./components/navigation-bar";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./components/pages/home";
import Settings from "./components/pages/settings";

function App() {
  return (
    <>
      <BrowserRouter>
        <NavigationBar />
        <Separator className="w-9/10 bg-primary" />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/*" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
