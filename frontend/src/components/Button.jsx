import React from "react";
import "../../styles/components/button.scss";

const Button = ({ children, styling, disabled = false , onClick}) => {
  return (
    <button disabled={disabled} className={`button ${styling}`} onClick={onClick}>
      {children}
    </button>
  );
};

export default Button;
