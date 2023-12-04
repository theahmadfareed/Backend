import React, { useState, useEffect, useRef } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import ReportData from "./MyDocument";
import html2canvas from "html2canvas";
import jsPDF from "jspdf";

const Reports = () => {
  const [searches, setSearches] = useState([]);
  const [selectedProjects, setSelectedProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const ref = useRef();

  const handleCheckboxChange = (projectId) => {
    // Check if the project is already in the selectedProjects array
    if (selectedProjects.includes(projectId)) {
      // If it is, remove it
      setSelectedProjects((prevSelected) => prevSelected.filter((id) => id !== projectId));
    } else {
      // If it's not, check if there is already one selected
      if (selectedProjects.length === 0) {
        // If no project is selected, add the current one
        setSelectedProjects((prevSelected) => [...prevSelected, projectId]);
      } else {
        // If one project is already selected, show an alert
        alert("You can only select 1 project for a report.");
      }
    }
  };

  const handleDownloadPdf = () => {
    // Get the HTML element to be captured as a PDF
    const targetElement = ref.current;

    // Use html2canvas to capture the target element as an image with higher quality
    html2canvas(targetElement, { scale: 2 }).then((canvas) => { // Increase the scale for higher quality
      // Convert the canvas to a data URL
      const dataURL = canvas.toDataURL();

      // Create a PDF document using jsPDF
      const pdf = new jsPDF("p", "mm", "a0");

      // Add the captured image to the PDF
      pdf.addImage(dataURL, "JPEG", 0, 0, pdf.internal.pageSize.getWidth(), pdf.internal.pageSize.getHeight());

      // Save or open the PDF file
      pdf.save("report.pdf");
    });
  };

  useEffect(() => {
    async function getAllSearches() {
      try {
        const searches_response = await axios.get("http://127.0.0.1:8000/api/usersearch/");
        setSearches(searches_response.data);
        setLoading(false);
      } catch (error) {
        console.log(error);
      }
    }

    getAllSearches();
  }, []);

  return (
    <div style={{ backgroundColor: "pink" }}>
      <div style={{ textAlign: "center" }}>
        {searches.map((search, i) => (
          <div key={search.id}>
            <input
              type="checkbox"
              checked={selectedProjects.includes(search.id)}
              onChange={() => handleCheckboxChange(search.id)}
            />
            <Link to={`/project-details/${search.id}`}>
              <b style={{ marginTop: "10px" }}>
                <b>{search.id}:</b>&emsp;
                {search.search_terms}&emsp;
                (
                <span>Positive: {search.total_sentiments[0].total_positive} &nbsp; </span>
                <span>Negative: {search.total_sentiments[0].total_negative} &nbsp; </span>
                <span>Neutral: {search.total_sentiments[0].total_neutral}</span>
                )
                &emsp;
                {search.created_at}
              </b>
            </Link>
          </div>
        ))}
      </div>

      <button disabled={loading} onClick={handleDownloadPdf}>
        Download PDF
      </button>

      <div ref={ref} style={{ marginTop: "30px" }}>
        {selectedProjects.length === 1 && !loading && <ReportData data={selectedProjects[0]} />}
      </div>
    </div>
  );
};

export default Reports;