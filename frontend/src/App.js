import './App.css';
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [searches, setSearches] = useState([])
  const [news, setNews] = useState([])
  const [reddit, setReddit] = useState([])

  useEffect(() => {
    async function getAllSearches() {
      try { 
        const searches_response = await axios.get("http://127.0.0.1:8000/api/usersearch/");
        const news_response = await axios.get("http://127.0.0.1:8000/api/newsarticles/");
        const reddit_response = await axios.get("http://127.0.0.1:8000/api/redditcomments/");
        
        console.log(searches_response.data);
        console.log(news_response.data);
        console.log(reddit_response.data);
        
        setSearches(searches_response.data);
        setSearches(news_response.data);
        setSearches(reddit_response.data);
      }
      catch (error) {
        console.log(error);
      }
    }
    
    getAllSearches();
  }, []);
  
  return (
    <div className="App">
      <h1>Connect React.js to Django</h1>
      {searches.map((search, i) => {
        return (<>
        <h2 key={search.id}>{ search.search_terms }</h2>
        </>
        )
      })
      }
    </div>
  );
}

export default App;
