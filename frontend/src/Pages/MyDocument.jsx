import React, { useState, useEffect } from "react";
import axios from "axios";
import LineChart from "../Components/Chart/LineChart";
import BarChart from "../Components/Chart/BarChart";

export default function ReportData(props) {
  const p_id = props.data;
  const [projectData, setProjectData] = useState(null);
  const [barChartDataNews, setBarChartDataNews] = useState(null);
  const [barChartDataReddit, setBarChartDataReddit] = useState(null);
  useEffect(() => {
    async function handleReportData() {
      try {
        const response = await axios.get(`/api/fetchData/${p_id}/`);
        setProjectData(response.data);
        console.log(response.data);
        setBarChartDataNews(response.data.each_keyword_sentiments_from_news)
        setBarChartDataReddit(response.data.each_keyword_sentiments_from_reddit)
      } catch (error) {
        console.log(error);
      }
    }
    handleReportData();
  }, [p_id]);

  // Check if projectData is not null before accessing its properties
  if (projectData === null) {
    return <div>Loading...</div>;
  }
  // // News API data
  const n1 = projectData.k1_news_graph_data;
  const n2 = projectData.k2_news_graph_data;
  const n3 = projectData.k3_news_graph_data;

  // Reddit API data
  const r1 = projectData.k1_reddit_graph_data;
  const r2 = projectData.k2_reddit_graph_data;
  const r3 = projectData.k3_reddit_graph_data;



  return (
    <div className="report-data" style={{ display: "flex", flexDirection: "column" }}>
      <h1 style={{ background: "white" }}>News Report</h1>
      <div>
        <div className="news" style={{ display: "flex", justifyContent: "space-evenly", textAlign: "center" }}>
          {n1 && (
            <div style={{ width: "400px" }}>
              <h1>{n1.Keyword}</h1>
              <LineChart line_data={n1} />
            </div>
          )}
          {n2 && (
            <div style={{ width: "400px" }}>
              <h1>{n2.Keyword}</h1>
              <LineChart line_data={n2} />
            </div>
          )}
          {n3 && (
            <div style={{ width: "400px" }}>
              <h1>{n3.Keyword}</h1>
              <LineChart line_data={n3} />
            </div>
          )}
        </div>
        <div className="news" style={{ display: "flex", justifyContent: "space-evenly", textAlign: "center" }}>
          {
            barChartDataNews.map((x) => {
              return (
                <div style={{ width: "400px" }}>
                  <BarChart total_sentiments={x} />
                </div>
              )
            })
          }
        </div>
      </div>
      <h1 style={{ background: "white" }}>Reddit Report</h1>
      <div>
        <div className="reddit" style={{ display: "flex", justifyContent: "space-evenly", textAlign: "center" }}>
          {r1 && (
            <div style={{ width: "400px" }}>
              <h1>{r1.Keyword}</h1>
              <LineChart line_data={r1} />
            </div>
          )}
          {r2 && (
            <div style={{ width: "400px" }}>
              <h1>{r2.Keyword}</h1>
              <LineChart line_data={r2} />
            </div>
          )}
          {r3 && (
            <div style={{ width: "400px" }}>
              <h1>{r3.Keyword}</h1>
              <LineChart line_data={r3} />
            </div>
          )}
        </div>
        <div className="reddit" style={{ display: "flex", justifyContent: "space-evenly", textAlign: "center" }}>
          {
            barChartDataReddit.map((x) => {
              return (
                <div style={{ width: "400px" }}>
                  <BarChart total_sentiments={x} />
                </div>
              )
            })
          }
        </div>
      </div>
    </div>
  );
}
