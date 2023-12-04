import React, { useState } from "react";
// import "./signup.css";

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Create a data object with the user's input
    const data = {
      u_name: username,
      u_email: email,
    };

    try {
      // Send a POST request to your backend server
      const response = await fetch("http://localhost:8000/signUp", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        // If the user is successfully created, navigate to the login page
        window.location.href = `/sign-in`;
      } else {
        // Handle errors or show a message if the user creation fails
        console.error("User creation failed");
      }
    } catch (error) {
      // Handle any network or other errors here
      console.error("An error occurred:", error);
    }
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <h1>SignUp Page</h1>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleUsernameChange}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={handleEmailChange}
        />
        <button type="submit">SignUp</button>
      </form>
    </div>
  );
};

export default SignUp;
