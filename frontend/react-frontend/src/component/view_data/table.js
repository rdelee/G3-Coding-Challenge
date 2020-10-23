import React from 'react'

import { Table } from 'react-bootstrap'

const dataTable = ({deals_data}) => {
    return (
        <Table striped bordered hover responsive>
            <thead>
                <tr>
                    <th scope="col">Instrument ID</th>
                    <th scope="col">Instrument Name</th>
                    <th scope="col">Deal ID</th>
                    <th scope="col">Counter ID</th>
                    <th scope="col">Counter Party Name</th>
                    <th scope="col">Price</th>
                    <th scope="col">Type</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Time</th>
                </tr>
            </thead>
            <tbody>
                {deals_data.map((deals_data) => (
                    <tr>
                        <td>{deals_data.instrument.instrument_id}</td>
                        <td>{deals_data.instrument.Instrument_Name}</td>
                        <td>{deals_data.deal.Deal_Id}</td>
                        <td>{deals_data.counter_party.counterparty_id}</td>
                        <td>{deals_data.counter_party.counterparty_name}</td>
                        <td>{deals_data.deal.Price}</td>
                        <td>{deals_data.deal.Type}</td>
                        <td>{deals_data.deal.Quantity}</td>
                        <td>{deals_data.deal.Time}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default dataTable;