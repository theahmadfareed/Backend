import React from "react";
import "./style.css";

const Card = ({ keywordData }) => {
  return (
    <div className="card">
      {keywordData.map((data, index) => (
        <div className="ref" key={index}>
          <a href={data.data.url} target="_blank" rel="noopener noreferrer">
            <p>Keyword: {data.keyword}</p>
            <img src={data.data.url_to_image} alt="dp" style={{ width: '50px', height: '50px' }}/>
            <p>Author: {data.data.author}</p>
            <p>Title: {data.data.title}</p>
            <p>Content: {data.data.content}</p>
            <p>Published-At: {data.data.published_at}</p>
            <p>Sentiment-Label: {data.data.sentiment_label}</p>
          </a>
        </div>
      ))}
    </div>
  );
};

export default Card;
