import React, { useState } from 'react';
import Loader from '../Components/Loader/Loader';
import "./style.css"; // Import your CSS file

export default function CreateProject() {
  const [keywords, setKeywords] = useState(''); // Use state to manage the keyword input
  const [isLoading, setIsLoading] = useState(false); // Use state to manage the loading state

  // Function to handle keyword input changes
  const handleInputChange = (event) => {
    setKeywords(event.target.value);
  };

  // Function to submit the form
  const handleSubmit = async (event) => {
    event.preventDefault();

    // Set the loading state to true
    setIsLoading(true);

    // Split the keywords into an array using the comma delimiter
    const keywordsArray = keywords.split(', ');
    console.log(keywordsArray)
    
    // Create the request body
    const body = JSON.stringify({ keywords: keywordsArray });
    console.log(body)

    // Send the POST request
    const response = await fetch('http://localhost:8000/fetch_save_data/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body,
    });

    // Set the loading state to false
    setIsLoading(false);

    // Handle the response from the backend
    if (response.ok) {
      // Success!
      // Get the project ID from the response
      const responseData = await response.json();
      const projectId = responseData.project_id;
      console.log('Project ID:', projectId);

      // Navigate to the project details page
      window.location.href = `/project-details/${projectId}`;
    } else {
      // Error!
    }
  };

  return (
    <div className="create-project-container">
    <form onSubmit={handleSubmit} className="create-project-form">
      <input
        type="text"
        placeholder="Enter 3 comma-separated keywords"
        value={keywords}
        onChange={handleInputChange}
        className="create-project-input"
      />
      <button type="submit" className="create-project-button">
        Create Project
      </button>
    </form>

    {isLoading && <Loader />}
  </div>
  );
}
