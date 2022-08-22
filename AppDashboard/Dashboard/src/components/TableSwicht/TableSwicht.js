import React,{ useState }  from 'react'

import { Line } from "react-chartjs-2";

import {
  Card,
  CardHeader,
  CardBody,
  Row,
} from "reactstrap";

import {
  chartExample1,
} from "variables/charts.js";


const TableSwicht = ({vaga}) => {
  
  function preperData(vaga){
    return {
      labels: ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],
      datasets: [
        {
          label: "Performance",
          data: vaga.tempoPorMes,
        },
      ],
    };
}
  
  return (
    <div>
            <Card>
              <CardHeader className="bg-transparent">
                <Row className="align-items-center">
                  <div className="col">
                    <h6 className="text-uppercase text-muted ls-1 mb-1">
                      Numero Vaga
                    </h6>
                    <h2 className="mb-0">Uso nos ultimos meses</h2>
                  </div>
                </Row>
              </CardHeader>
              <CardBody>
                <div className="chart">
                  <Line
                    data={preperData(vaga)}
                    options={chartExample1.options}
                    getDatasetAtEvent={(e) => console.log(e)}
                  />
                </div>
              </CardBody>
            </Card>
    </div>
  )
}

export default TableSwicht