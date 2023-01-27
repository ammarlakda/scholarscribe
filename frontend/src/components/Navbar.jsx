import React from "react";
import "../../styles/components/navbar.scss";
import Button from "./Button";

const Navbar = () => {
  return (
    <div className="navbar">
      <Button styling="navbar__item">How it works</Button>
      <Button styling="navbar__item">Try it!</Button>
    </div>
  );
};

export default Navbar;
