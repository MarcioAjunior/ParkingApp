import React, { useEffect } from "react";

// reactstrap components
import {Card, Container, Row, CardHeader, CardBody, Table } from "reactstrap";

import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import VagaReducer from '../../store/reducer/vagaReducer'
import Header from "components/Headers/Header.js";
import CardVagas from "components/Vagas/CardVagas";
import { Link } from "react-router-dom";

const MapWrapper = ({vagas}) => {
  return (
    <>
      <div
        style={{ height: `600px` }}
        className="map-canvas"
        id="map-canvas"
      >
         <Card>
          <CardHeader>Todas as suas vagas</CardHeader>
          <CardBody>
            <div style={{
              maxHeight: '500px',
              overflowY: 'auto',
            }}>
                  {vagas.map((item) => (
                      <Link to={`/admin/vagas/${item.id}`} key={item.id}> 
                        <CardVagas /> 
                      </Link>
                  ))}
            </div>
          </CardBody>
        </Card>
      </div>
    </>
  );
};

const Maps = (props) => {

  useEffect(() => props.fetch(), [])

  return (
    <>
      <Header />
      <Container className="mt--7" fluid>
        <Row>
          <div className="col">
            <Card className="shadow border-0">
              <MapWrapper vagas={props.vagas} />
            </Card>
          </div>
        </Row>
      </Container>
    </>
  );
};

const mapStateToProps = state => ({
    vagas : state.vagas.data
})

const mapDispatchToProps = dispatch => bindActionCreators({
  fetch : () => VagaReducer.fetch(),
},dispatch)


export default connect(mapStateToProps,mapDispatchToProps)(Maps);
