import React from 'react'

import { Table } from 'react-bootstrap'

const dataTable = ({deals_data}) => {
    return (
        <Table striped bordered hover responsive>
            <thead>
                <tr>
                    <th scope="col">Instrument Name</th>
                    <th scope="col">Cpty</th>
                    <th scope="col">price</th>
                    <th scope="col">type</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Time</th>
                </tr>
            </thead>
            <tbody>
                {deals_data.map((deals_data) => (
                    <tr>
                        <td>{deals_data.instrumentName}</td>
                        <td>{deals_data.cpty}</td>
                        <td>{deals_data.price}</td>
                        <td>{deals_data.type}</td>
                        <td>{deals_data.quantity}</td>
                        <td>{deals_data.time}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default dataTable;