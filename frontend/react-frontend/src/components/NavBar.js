import React, { useState } from "react";
import { NavLink as RouterNavLink } from "react-router-dom";
import { Navbar, Nav } from 'react-bootstrap'
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "reactstrap";

const NavBar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const {user, isAuthenticated, loginWithRedirect, logout,} = useAuth0();
  const logoutWithRedirect = () =>
      logout({
        returnTo: window.location.origin,
      });
  
    return (
      <ul>
        <li><a href="/">Home</a></li>
        {isAuthenticated && (<a href="/datastream">Data Stream</a>)}
        {isAuthenticated && (<a href="/table">Table</a>)}
        {!isAuthenticated && (<Button onClick={() => loginWithRedirect()}>Log in</Button>)}
        {isAuthenticated && (<Button onClick={() => logoutWithRedirect()}>Log out</Button>)}
        {isAuthenticated && (<h2>Welcome {user.name}!</h2>)}
      </ul>       
    );
  };

export default NavBar;
