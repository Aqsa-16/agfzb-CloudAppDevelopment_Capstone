import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const gohome = () => {
    window.location.href = window.location.origin;
  };

  const register = async (e) => {
    e.preventDefault();

    let register_url = window.location.origin + "/djangoapp/register";

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email,
      }),
    });

    const json = await res.json();
    if (json.status) {
      sessionStorage.setItem("username", json.userName);
      window.location.href = window.location.origin;
    } else if (json.error === "Already Registered") {
      alert("The user with same username is already registered");
    }
  };

  return (
    <div className="register_container" style={{ width: "50%", margin: "auto", paddingTop: "50px" }}>
      <div className="header" style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
        <h2 style={{ color: "black", paddingBottom: "0px" }}>Sign-up</h2>
        <a href="/" onClick={() => gohome()} style={{ cursor: "pointer" }}>
          <img style={{ width: "1cm" }} src="/static/cancel.png" alt="X" />
        </a>
      </div>
      <hr />
      <form onSubmit={register}>
        <div className="inputs">
          <div className="input">
            <span className="details">Username</span>
            <input
              type="text"
              name="username"
              placeholder="Username"
              className="input_field form-control"
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
          <div className="input mt-3">
            <span className="details">First Name</span>
            <input
              type="text"
              name="first_name"
              placeholder="First Name"
              className="input_field form-control"
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </div>
          <div className="input mt-3">
            <span className="details">Last Name</span>
            <input
              type="text"
              name="last_name"
              placeholder="Last Name"
              className="input_field form-control"
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </div>
          <div className="input mt-3">
            <span className="details">Email</span>
            <input
              type="email"
              name="email"
              placeholder="Email"
              className="input_field form-control"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input mt-3">
            <span className="details">Password</span>
            <input
              name="psw"
              type="password"
              placeholder="Password"
              className="input_field form-control"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
        </div>
        <div className="submit_panel mt-4">
          <input className="btn btn-primary" type="submit" value="Register" />
        </div>
      </form>
    </div>
  );
};

export default Register;
