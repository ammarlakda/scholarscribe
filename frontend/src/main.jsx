import React from "react";
import ReactDOM from "react-dom/client";
import "../styles/pages/global.scss";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "./pages/Home";
import TryIt from "./pages/TryIt";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  }, {
    path: "/try-it",
    element: <TryIt/> 
  }
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
