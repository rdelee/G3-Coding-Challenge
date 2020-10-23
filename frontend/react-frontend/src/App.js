import React from 'react'
import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import './App.css';
import Header from './component/common/header';
import Stream from './component/view_data/data_stream_display';
import Login from './Login';
import Table from './component/view_data/table_view_page';

function App() {

  return (
   <div className="App">

    <Header />
     {/* <Container className="pane">
      <Stream />
     </Container> */}

    <Router>
      <Switch>
        <Route path="/datastream">
          <Stream />    
        </Route>
        <Route path="">
         <Login />
        </Route>
        <Route path="/table">
          <Table />    
        </Route>
      </Switch>
    </Router>

   </div>
  );
}

export default App;
