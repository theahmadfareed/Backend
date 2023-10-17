import { useParams } from 'react-router-dom';
import { useState, useEffect } from "react";
import axios from "axios";
import LineChart from "../Components/Chart/LineChart";
import BarChart from "../Components/Chart/BarChart";
import Card from "../Components/Card/Card";

export default function ProjectDetails() {
  const { projectId } = useParams();
  const [projectData, setProjectData] = useState(null);

  useEffect(() => {
    async function fetchProjectData() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/usersearch/${projectId}/`);
        setProjectData(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    fetchProjectData();
  }, [projectId]);

  return (
    <div>
      <h1 className="App">Django Connected to React.Js</h1>
      {projectData && (
        <div>
          <h2 style={{ textAlign: 'center' }}>{projectData.search_terms}</h2>
          <LineChart line_data={projectData.graph_data} />
          <BarChart total_sentiments={projectData.total_sentiments[0]} />
          <Card keywordData={projectData.each_keyword_combine_data} />
        </div>
      )}
    </div>
  );
}
