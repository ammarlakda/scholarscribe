import React from "react";
import Footer from "./Footer";
import Navbar from "./Navbar";
import "../../styles/components/layout.scss"

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Navbar />
      <div className="layout__content">{children}</div>
      <Footer />
    </div>
  );
};

export default Layout;
