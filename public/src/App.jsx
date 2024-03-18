import "./App.css";
import { Provider } from "react-redux";
import store from "./store/store";
import { Route, Routes } from "react-router-dom";
import Home from "./routes/Home";

function App() {
  return (
    <>
      <Provider store={store}>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Provider>
    </>
  );
}

export default App;
