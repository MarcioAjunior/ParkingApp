import React, { useEffect, useState } from "react";

// core components
import Header from "components/Headers/Header.js";

import {
    Container,
    Row,
    Col,
    Card,
    CardHeader,
  } from "reactstrap";
  
  import {
    chartOptions,
    parseOptions,
  } from "variables/charts.js";

  import Chart from "chart.js";

  import TableSwicht from "components/TableSwicht/TableSwicht";
  
  import {bindActionCreators} from 'redux'

  import {connect} from 'react-redux'

  import VagaReducer from '../../store/reducer/vagaReducer'

  import TableBar from "components/TableBar/TableBar";

const VagasId = ({fetchId, match, vaga, data}) => {

  // props.fetchId()
  const [colorTxt, setColorTxt] = useState({});
  
  useEffect(() => {
    fetchId(match.params.id)
    vaga.emUso ? setColorTxt({cor: '#CD5C5C',txt: 'Em uso'}) : setColorTxt({cor : '#98FB98', txt :'livre'})
  },[])


  if (window.Chart) {
    parseOptions(Chart, chartOptions());
  }
  return (
    <>
        <Header />
        <Container className="mt--7" fluid>
        <Row className="mb-2">
            <Col xl="4">
              <Card>
                <CardHeader>
                  Vaga Nº {vaga.id}
                </CardHeader>
              </Card>
            </Col>

            <Col xl="2">
              <Card color="" >
                <CardHeader style={{backgroundColor:colorTxt.cor}}> {/* A porra do backfground */}
                  {colorTxt.txt}
                </CardHeader>
              </Card>
            </Col>
        </Row>
        <Row>
          <Col className="mb-5 mb-xl-0" xl="6">
          <TableSwicht vaga={vaga} />
          </Col>
          <Col xl="6">
          <TableBar vaga={vaga}/>
          </Col>
        </Row>
      </Container>
    </>
  );
};

const mapDispatchToProps = dispatch => bindActionCreators({
  fetchId : (id) => VagaReducer.fetchId(id),
},dispatch)

const mapStateToProps = state => ({
  vaga : state.vagas.vaga,
  data : state.vagas.data
})

export default connect(mapStateToProps,mapDispatchToProps)(VagasId);
