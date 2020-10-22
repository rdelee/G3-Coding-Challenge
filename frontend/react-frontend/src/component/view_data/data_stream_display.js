import React, { Component, useState } from "react";
import { Line } from "react-chartjs-2";
import { Button } from "react-bootstrap";

import { useObservable } from 'rxjs-hooks';
import { Observable } from 'rxjs';
import { map, withLatestFrom } from 'rxjs/operators';

// import { endpointUrls } from '../config';

const stringObservable = Observable.create(observer => {
    //const source = new EventSource(endpointUrls.dockerurlwindowsvb);
    const source = new EventSource("http://localhost:8090/deals");
    source.addEventListener("message", (messageEvent) => {
        observer.next(messageEvent.data);
    }, false);


    var isOpenOnce = false;
    source.onopen = function () {
        if (isOpenOnce) {
            source.close();
        } else {
            console.log("Connection to server opened.");
            isOpenOnce = true;
        }
    }

});

function PriceChart() {

    var data = {
        labels: [],
        datasets: [
            {
                label: 'Price in Time',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1',
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: []
            }
        ]
    };

  const [stringArray, setStringArray] = useState([]);

  useObservable(
    state =>
        stringObservable.pipe(
            withLatestFrom(state),
            map(([state]) => {
                let updatedStringArray = stringArray;
                updatedStringArray.unshift(state);
                if (updatedStringArray.length >= 50) {
                    updatedStringArray.pop();
                }

                console.log(state);
                return state;
            })
        )

    );

    var jsonData = [];
    stringArray.forEach(function (item) {
        jsonData.push(JSON.parse(item.replace(/'/g, '"')));
    });

    // <Button> Stop Stream</Button>
    


    jsonData.forEach(function (item) {
        data.labels.push(item.time);
        data.datasets[0].data.push(item.price);
    });

    return (
        <div>
            <Line data={data} />
            <Button onClick={() => fetch("http://localhost:8090/",      
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "POST"
            }).catch(console.log("exception"))}> Stop </Button>
        </div>
    
    );
}

export default PriceChart;
