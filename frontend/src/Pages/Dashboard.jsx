import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from 'react-router-dom';


export default function Dashboard() {
  const [searches, setSearches] = useState([])
  useEffect(() => {
    async function getAllSearches() {
      try { 
        const searches_response = await axios.get("http://127.0.0.1:8000/api/usersearch/");        
        setSearches(searches_response.data);
      }
      catch (error) {
        console.log(error);
      }
    }
    getAllSearches();
  }, []);
  return (
    <div>
      <h1 style={{ textAlign: 'center' }}>Dashboard Page</h1>
      {searches.map((search, i) => {
        return (
          <div style={{ textAlign: 'center' }} key={search.id}>
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
        )
      })
      }
    </div>
  )
}