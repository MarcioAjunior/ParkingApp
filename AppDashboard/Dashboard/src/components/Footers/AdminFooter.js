/*!

=========================================================
* Argon Dashboard React - v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
/*eslint-disable*/

// reactstrap components
import { Container, Row, Col, Nav, NavItem, NavLink } from "reactstrap";

const Footer = () => {
  return (
    <footer className="footer">
      <Row className="align-items-center justify-content-xl-between">
        <Col md="10" lg="10" xl="10">
          <div className="copyright text-center text-xl-left text-muted">
          </div>
        </Col>

        <Col md="2" lg="2" xl="2">
        <div className="copyright text-center text-xl-left text-muted">
          <span>
            By Marcinho '-'
          </span>
        </div>
        </Col>
      </Row>
    </footer>
  );
};

export default Footer;
