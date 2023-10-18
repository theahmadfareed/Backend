import { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import "./style.css"; // Import your CSS file


export default function Dashboard() {
  const [searches, setSearches] = useState([])
  useEffect(() => {
    async function getAllSearches() {
      try { 
        const searches_response = await axios.get("http://127.0.0.1:8000/api/usersearch/");
        console.log(searches_response)
        setSearches(searches_response.data);
      }
      catch (error) {
        console.log(error);
      }
    }
    getAllSearches();
  }, []);
  return (
    <div className="dashboard-container">
      <h1 className="dashboard-heading">Dashboard</h1>
      {searches.map((search, i) => (
        <div className="search-item" key={search.id}>
          <Link to={`/project-details/${search.id}`}>
            <b>
              <span>{search.id}:</span>&emsp;
              <span>{search.search_terms}</span>&emsp;
              <span>
                (
                <span>Positive: {search.total_sentiments[0].total_positive} &nbsp; </span>
                <span>Negative: {search.total_sentiments[0].total_negative} &nbsp; </span>
                <span>Neutral: {search.total_sentiments[0].total_neutral}</span>
                )
              </span>&emsp;
              <span>{search.created_at}</span>
            </b>
          </Link>
        </div>
      ))}
    </div>
  )
}