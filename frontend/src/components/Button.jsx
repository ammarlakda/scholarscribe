import React from "react";
import "../../styles/components/button.scss"
const Button = ({children, styling}) => {
  return <div className={`button ${styling}`}>{children}</div>;
};

export default Button;
