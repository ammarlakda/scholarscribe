import React from "react";
import { FaGithub } from "react-icons/fa";

const Footer = () => {
  return (
    <div>
      <div>This project is made for QHacks 2023</div>
      <div>
        <a href="https://github.com/ammarlakda/scholarscribe" target="_blank">
          <FaGithub />
        </a>
      </div>
    </div>
  );
};

export default Footer;
