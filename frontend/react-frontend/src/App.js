import React from "react";
import { Router, Route, Switch } from "react-router-dom";
import { Container } from "reactstrap";
import NavBar from "./components/NavBar";
import Loading from "./components/Loading";
import Stream from './component/view_data/data_stream_display'
import Table from './component/view_data/table_view_page';
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
            <Route path="/table" component={Table} />
          </Switch>
        </Container>
      </div>
    </Router>
  );
};

export default App;
