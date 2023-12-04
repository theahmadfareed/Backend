import React, { useState } from "react";

const SignIn = () => {
  const [username, setUsername] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {
      u_name: username
    };

    try {
      // Send a POST request to your backend server
      const response = await fetch("http://localhost:8000/signIn", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        // If the user is successfully created, navigate to the login page
        window.location.href = `/create-project`;
      } else {
        // Handle errors or show a message if the user creation fails
        console.error("User login failed");
      }
    } catch (error) {
      // Handle any network or other errors here
      console.error("An error occurred:", error);
    }
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
      <h1>SignIn Page</h1>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleUsernameChange}
        />
        <button type="submit">Sign-In</button>
      </form>
    </div>
  );
};

export default SignIn;
