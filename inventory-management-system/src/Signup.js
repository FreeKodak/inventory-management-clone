import React, { Component } from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBBtn } from 'mdbreact';
import axios from 'axios';
import { Button } from 'semantic-ui-react';
import History from './History';

class Signup extends Component {
    constructor(props){
        super(props);
        this.state = {
          firstName: '',
          lastName: '',
          address: '',
          email: '',
          password: '',
          confirmPassword: '',
          complete: false,
        };
    
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handleFnameChange = this.handleFnameChange.bind(this);
        this.handleLnameChange = this.handleLnameChange.bind(this);
        this.handleAddressChange = this.handleAddressChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleCpasswordChange = this.handleCpasswordChange.bind(this);
      }

      handleEmailChange(event) {
        this.setState({email: event.target.value});
      }
    
      handleFnameChange(event){
        this.setState({firstName: event.target.value});
      }

      handleLnameChange(event){
        this.setState({lastName: event.target.value});
      }

      handleAddressChange(event){
        this.setState({address: event.target.value});
      }
      
      handlePasswordChange(event){
        this.setState({password: event.target.value});
      }
    
      handleCpasswordChange(event){
        this.setState({confirmPassword: event.target.value});
      }
    
    render() {
        return (
          <div className="Light">
          <MDBContainer>
            <MDBRow>
              <MDBCol md="6">
                <form>
                  <p className="h4 text-center mb-4">Sign up</p>
                  <label htmlFor="defaultFormRegisterNameEx" className="grey-text">
                    First Name
                  </label>
                  <input
                    type="text"
                    id="defaultFormRegisterNameEx"
                    className="form-control"
                    onChange={this.handleFnameChange}
                  />
                  <br />
                  <label htmlFor="defaultFormRegisterNameEx" className="grey-text">
                    Last Name
                  </label>
                  <input
                    type="text"
                    id="defaultFormRegisterNameEx"
                    className="form-control"
                    onChange={this.handleLnameChange}
                  />
                  <br />
                  <label htmlFor="defaultFormRegisterNameEx" className="grey-text">
                    Address
                  </label>
                  <input
                    type="text"
                    id="defaultFormRegisterNameEx"
                    className="form-control"
                    onChange={this.handleAddressChange}
                  />
                  <br />
                  <label htmlFor="defaultFormRegisterEmailEx" className="grey-text">
                    Email
                  </label>
                  <input
                    type="email"
                    id="defaultFormRegisterEmailEx"
                    className="form-control"
                    onChange={this.handleEmailChange}
                  />
                  <br />
                  <label
                    htmlFor="defaultFormRegisterPasswordEx"
                    className="grey-text"
                  >
                    Password
                  </label>
                  <input
                    type="password"
                    id="defaultFormRegisterPasswordEx"
                    className="form-control"
                    onChange={this.handlePasswordChange}
                  />
                  <br />
                  <label
                    htmlFor="defaultFormRegisterPasswordEx"
                    className="grey-text"
                  >
                    Confirm Password
                  </label>
                  <input
                    type="password"
                    id="defaultFormRegisterPasswordEx"
                    className="form-control"
                    onChange={this.handleCpasswordChange}
                  />
                  <div className="text-center mt-4">
                    {/* <Button color="unique" type="submit" onClick={() => this.signUp()}>
                      Register
                    </Button> */}
                  </div>
                </form>
              </MDBCol>
            </MDBRow>
          </MDBContainer>
          <center>
            <Button color="unique" type="submit" onClick={() => this.signUp()}>
              Register
            </Button>
          </center>
         
            <br></br><br></br><br></br><br></br><br></br><br></br>
            <br></br><br></br><br></br><br></br><br></br><br></br>
            <br></br><br></br><br></br><br></br><br></br><br></br>
            
          </div>
        );
    }

    checkFields() {
      if(this.state.firstName == '' || this.state.lastName == '' || this.state.address == '' ||
      this.state.email == '' || this.state.password == '' || this.state.confirmPassword == '') {
        return false;
      } else {
        return true;
      }
    }

    signUp() {
      if(!this.checkFields()) {
        alert("Please fill out all fields");
      } else if(this.state.password === this.state.confirmPassword) {
        let user = {
          firstName: this.state.firstName,
          lastName: this.state.lastName,
          address: this.state.address,
          email: this.state.email,
          password: this.state.password
        };

        axios.post('http://localhost:5000/validateUser', user)
        .then(res => {
          if(res.data === "success") {
            axios.post('http://localhost:5000/registerUser', user)
            .then(res =>{
                console.log(res);
            }).catch(err => {
                console.log(err);
            })
            
            History.push('/');
          } else {
              alert("User with that Email already exists!");
          }
        })
      }
    }
}

export default Signup;