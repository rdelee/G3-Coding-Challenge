// import React from 'react'
// import { Container } from 'react-bootstrap';
// import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

// import './App.css';
// import Header from './component/common/header';
// import Stream from './component/view_data/data_stream_display'
// // import Login from './Login';

// function App() {

//   return (
//    <div className="App">

//     <Header />
//      {/* <Container className="pane">
//       <Stream />
//      </Container> */}

//     {/* <Router>
//       <Switch>
//         <Route path="/datastream">
//           <Stream />    
//         </Route>
//         <Route path="">
//          <Login />
//         </Route>
//       </Switch>
//     </Router> */}

//    </div>
//   );
// }

// export default App;


import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import { Container } from "reactstrap";
import NavBar from "./components/NavBar";
import Loading from "./components/Loading";
import Stream from './component/view_data/data_stream_display'
import Home from "./views/Home";
import { useAuth0 } from "@auth0/auth0-react";
import history from "./utils/history";

// styles
import "./App.css";

const App = () => {
  const { isLoading, error } = useAuth0();

  if (error) {
    return <div>Oops... {error.message}</div>;
  }

  if (isLoading) {
    return <Loading />;
  }

  return (
    <Router history={history}>
      <div id="app">
        <NavBar />
        <Container>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/datastream" component={Stream} />
          </Switch>
        </Container>
      </div>
    </Router>
  );
};

export default App;
