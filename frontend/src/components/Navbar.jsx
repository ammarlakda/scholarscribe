import React from "react";
import { Link } from "react-router-dom";
import "../../styles/components/navbar.scss";
import Button from "./Button";

const Navbar = () => {
  return (
    <div className="navbar">
      <Link to="/">
        <Button styling="navbar__item">How it works</Button>
      </Link>
      <Link to="/try-it">
        <Button styling="navbar__item">Try it!</Button>
      </Link>
    </div>
  );
};

export default Navbar;
