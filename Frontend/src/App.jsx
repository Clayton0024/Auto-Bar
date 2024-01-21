import { NavigationBar } from "./components/navigation-bar";
import { HashRouter, Route, Routes } from "react-router-dom";
import Home from "./components/pages/home";
import Settings from "./components/pages/settings";

function App() {
  return (
    <>
      <NavigationBar />
      <HashRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/*" element={<Home />} />
        </Routes>
      </HashRouter>
    </>
  );
}

export default App;
