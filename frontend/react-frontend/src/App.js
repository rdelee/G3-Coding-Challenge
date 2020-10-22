import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import './App.css';

import Stream from './component/view_data/data_stream_display'
import Login from './Login';

function App() {

  return (
   <div className="App">
    <Router>
      <Switch>
        <Route path="">
         <Login />
        </Route>

        <Route path="dataStream">
          <Stream />    
        </Route>
      </Switch>
    </Router>
    
   
    
   </div>
  );
}

export default App;
