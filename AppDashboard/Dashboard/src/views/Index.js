import {
  Container,
  Row,
  Card,
  CardHeader,
  Col
} from "reactstrap";

import Header from "components/Headers/Header.js";

import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import VagaReducer from '../store/reducer/vagaReducer'
import { useEffect } from "react";

const Index = (props) => {

  useEffect(() => {
    setInterval(() => {
      props.fetch()
    },1000)
  }
  ,[])

  const MapWrapper = () => {
    return (
      <>
        <div
          style={{ height: `450px` }}
          className="map-canvas"
          id="map-canvas"
        >
             <img
                style={{
                  height : '450px',
                  width : '100%'
                }}
                src="http://localhost:5001/video_feed"
                alt="Video"
              />
        </div>
      </>
    );
  };

  return (
    <>
    {console.log(props)}
      <Header />
      <Container className="mt--7" fluid>
        <Row className="mb-2">
          <Col xl="12">
              <Card>
                <CardHeader>
                  <Row className="justify-content-center">
                    <Col xl="1">
                    <div className="icon icon-shape bg-info text-white rounded-circle shadow">
                      <i className="fas fa-video" />  
                    </div>
                    </Col>
                    <Col className="align-self-center" xl="11">
                       <span>
                        Video Feed
                       </span>
                    </Col>
                  </Row>
                </CardHeader>
              </Card>
          </Col>
        </Row>
        <Row>
          <div className="col">
            <Card className="shadow border-0">
              <MapWrapper />
            </Card>
          </div>
        </Row>
      </Container>
    </>
  );
};

const mapDispatchToProps = dispatch => bindActionCreators({
  fetch : () => VagaReducer.fetch(),
},dispatch)

const mapStateToProps = state => ({
  vagas : state.vagas.data
})

export default connect(mapStateToProps, mapDispatchToProps)(Index);
