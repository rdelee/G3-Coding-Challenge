import React, { Component } from 'react';
import { Container } from 'react-bootstrap';
import axios from 'axios';

import Table from './table';

export default class TableView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            deals: []
        }
    }

    componentDidMount() {
        axios
            .get("http://localhost:8090/get_test_data")
            .then((result) => {
                this.setState({
                    isLoaded: true,
                    deals: result.data,
                });
            })
            .catch((error) => {
                this.setState({
                    isLoaded: true,
                    error,
                });
            });
    }

    render() {
        const { error, isLoaded, deals } = this.state;

        return (
            <Container>
                {console.log(deals)}
                {error && <div>Error: {error.message}</div>}
                {!isLoaded && <div>Loading...</div>}
                {!error && isLoaded && (
                    <div>
                        <h1>Deals:</h1>
                        <Table deals_data={deals} />
                    </div>
                )}
            </Container>
        )
    }

}