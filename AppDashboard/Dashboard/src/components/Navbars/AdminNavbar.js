import {
  Navbar,
  Container,
} from "reactstrap";

const AdminNavbar = (props) => {
  return (
    <>
      <Navbar className="navbar-top navbar-dark" expand="md" id="navbar-main">
        <Container fluid>
            {/* {props.brandText} */}
        </Container>
      </Navbar>
    </>
  );
};

export default AdminNavbar;
