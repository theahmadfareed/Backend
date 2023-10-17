import React from "react";
import "./style.css";

const Card = ({ keywordData }) => {
  return (
    <div className="card">
      {keywordData.map((data, index) => (
          <a href={data.data.url} target="_blank" rel="noopener noreferrer">
            <div className="ref" key={index}>
              <img src={data.data.url_to_image} alt="dp" style={{ width: '50px', height: '50px' }}/>
              <p>Author: {data.data.author}</p>
              <p>Title: {data.data.title}</p>
              <p>Content: {data.data.content}</p>
              <p>Published-At: {data.data.published_at}</p>
              <p>Sentiment-Label: {data.data.sentiment_label}</p>
            </div>
          </a>
      ))}
    </div>
  );
};

export default Card;
