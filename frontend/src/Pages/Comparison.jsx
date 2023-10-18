import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import ComparisonChart from "../Components/Chart/ComparisonChart";

export default function Dashboard() {
  const [searches, setSearches] = useState([]);
  const [selectedProjects, setSelectedProjects] = useState([]);
  const [projectSentiments1, setProjectSentiments1] = useState(null);
  const [projectSentiments2, setProjectSentiments2] = useState(null);
  
  const [projectSearchTerms1, setProjectSearchTerms1] = useState(null);
  const [projectSearchTerms2, setProjectSearchTerms2] = useState(null);

  useEffect(() => {
    async function getAllSearches() {
      try {
        const searches_response = await axios.get("http://127.0.0.1:8000/api/usersearch/");
        setSearches(searches_response.data);
      } catch (error) {
        console.log(error);
      }
    }
    getAllSearches();
  }, []);

  const handleCheckboxChange = (projectId) => {
    setSelectedProjects((prevSelected) => {
      if (prevSelected.includes(projectId)) {
        return prevSelected.filter((id) => id !== projectId);
      } else {
        return [...prevSelected, projectId];
      }
    });
  };

  const handleCompareProjects = async () => {
    if (selectedProjects.length !== 2) {
      console.log("Please select exactly 2 projects for comparison.");
      return;
    }

    try {
      const [projectId1, projectId2] = selectedProjects;

      const [response1, response2] = await Promise.all([
        axios.get(`http://127.0.0.1:8000/api/usersearch/${projectId1}/`),
        axios.get(`http://127.0.0.1:8000/api/usersearch/${projectId2}/`),
      ]);

      const totalSentiments1 = response1.data.total_sentiments[0];
      const totalSentiments2 = response2.data.total_sentiments[0];
  
      const searchTerms1 = response1.data.search_terms;
      const searchTerms2 = response2.data.search_terms;

      setProjectSentiments1(totalSentiments1);
      setProjectSentiments2(totalSentiments2);
      setProjectSearchTerms1(searchTerms1);
      setProjectSearchTerms2(searchTerms2);
    } catch (error) {
      console.error("Error fetching project data:", error);
    }
  };

  return (
    <div>
      <h1 style={{ textAlign: 'center' }}>Compare your Projects!</h1>
      {searches.map((search, i) => {
        return (
          <div style={{ textAlign: 'center' }} key={search.id}>
            <input
              type="checkbox"
              checked={selectedProjects.includes(search.id)}
              onChange={() => handleCheckboxChange(search.id)}
            />
            <Link to={`/project-details/${search.id}`}>
              <b>
                <span>{search.id}:</span>&emsp;
                <span>{search.search_terms}</span>&emsp;
                <span>(
                  <span>Positive: {search.total_sentiments[0].total_positive} &nbsp; </span>
                  <span>Negative: {search.total_sentiments[0].total_negative} &nbsp; </span>
                  <span>Neutral: {search.total_sentiments[0].total_neutral}</span>)
                </span>&emsp;
                <span>{search.created_at}</span>
              </b>
            </Link>
          </div>
        );
      })}
      <button onClick={handleCompareProjects}>Compare Selected Projects</button>
      {selectedProjects.length === 2 && (
        <ComparisonChart
          total_sentiments1={projectSentiments1}
          total_sentiments2={projectSentiments2}
          searchTerms1={projectSearchTerms1}
          searchTerms2={projectSearchTerms2}
        />
      )}
    </div>
  );
}
