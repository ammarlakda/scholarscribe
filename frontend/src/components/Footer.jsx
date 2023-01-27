import React from "react";
import { FaGithub } from "react-icons/fa";
import "../../styles/components/footer.scss"

const Footer = () => {
  return (
    <div className="footer">
      <div>This project is made for QHacks 2023</div>
      <div>
        <a href="https://github.com/ammarlakda/scholarscribe" target="_blank">
          <FaGithub className="footer__gh-icon"/>
        </a>
      </div>
    </div>
  );
};

export default Footer;
