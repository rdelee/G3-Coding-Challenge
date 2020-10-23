import React from "react";
import { alignPropType } from "react-bootstrap/esm/DropdownMenu";
import logo from "../assets/amorcs.png";

const divStyle = {
  textAlign: "center"
}

const Hero = () => (
<div style={divStyle}>
    <img className="mb-3 app-logo" src={logo} alt="amor cs logo" width="120" />
    <h1 className="mb-4">Amor CS</h1>

    <p>Welcome to Amor CS!</p>
  </div>
);

export default Hero;
