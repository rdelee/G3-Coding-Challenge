import React from 'react';
import { Container } from 'react-bootstrap';
import './App.css';

import Header from './component/common/header';

import Stream from './component/view_data/data_stream_display';

function App() {

  return (
   <div className="App">
     <Header />
     <Container>
        <Stream />
     </Container>
   </div>
  );
}

export default App;
