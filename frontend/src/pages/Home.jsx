import React from "react";
import Layout from "../components/Layout";
import "../../styles/pages/home.scss";
import Button from "../components/Button";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <Layout>
      <div className="home">
        <h1>ScholarScribe</h1>
        <p>
          Upload an mp3 or mp4 file of a lecture and transcribe it and get
          lecture notes generated!
        </p>
        <div className="home__options">
          <Link to="/try-it">
            <Button styling="home__options__buttons">Try It!</Button>
          </Link>
          <Button styling="home__options__buttons">See a Demo</Button>
        </div>
      </div>
    </Layout>
  );
};

export default Home;
