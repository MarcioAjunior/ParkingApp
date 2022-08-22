import React from 'react'

import { Bar } from "react-chartjs-2";

import {
  Card,
  CardHeader,
  CardBody,
  Row,
} from "reactstrap";

// core components
import {
  chartExample2,
} from "variables/charts.js";


export default function TableBar({vaga}) {


function preperData(vaga){
  return  {
    labels: ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
    datasets: [
      {
        label: "Uso por dias da semana",
        data: vaga.tempoPorSemana,
        maxBarThickness: 10,
      },
    ],
  }
}

return (
<div>
    <Card className="shadow">
            <CardHeader className="bg-transparent">
            <Row className="align-items-center">
                <div className="col">
                <h6 className="text-uppercase text-muted ls-1 mb-1">
                  Numero da vaga
                </h6>
                <h3 className="mb-0">Horas usadas nos ultimos dias</h3>
                </div>
            </Row>
            </CardHeader>
            <CardBody>
            <div className="chart">
                <Bar
                data={preperData(vaga)}
                options={chartExample2.options}
                />
            </div>
            </CardBody>
        </Card>
</div>
)
}
