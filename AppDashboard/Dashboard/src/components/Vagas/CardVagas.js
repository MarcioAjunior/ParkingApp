import { Card, CardBody, Container, Row, Col } from "reactstrap";


function CardVagas(props) {
return (
    <Container>
  <div className='mb-1'>
                <Card className="card-stats mb-4 mb-xl-0">
                  <CardBody>
                    <Row>
                      <div className="col">
                        <span className="h3 font-weight-bold mb-0">
                          Numero da vaga
                        </span>
                      </div>
                      <Col className="col-auto">
                        <div className="icon icon-shape bg-success text-white rounded-circle shadow">
                          <i className="fas fa-car" />  
                        </div>
                      </Col>
                    </Row>
                  </CardBody>
                </Card>
                </div>
                </Container>
)
}
export default CardVagas