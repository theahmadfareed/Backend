import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import "./style.css";

const ComparisonChart = ({ total_sentiments1, total_sentiments2, searchTerms1, searchTerms2 }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    const ctx = chartRef.current?.getContext("2d"); // Use optional chaining

    if (!ctx || !total_sentiments1 || !total_sentiments2) {
      return; // Return early if any required data is missing
    }

    const chartData = {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [
        {
          label: searchTerms1,
          data: [
            total_sentiments1.total_positive,
            total_sentiments1.total_negative,
            total_sentiments1.total_neutral,
          ],
          backgroundColor: ["green"],
        },
        {
          label: searchTerms2,
          data: [
            total_sentiments2.total_positive,
            total_sentiments2.total_negative,
            total_sentiments2.total_neutral,
          ],
          backgroundColor: ["yellow"],
        },
      ],
    };

    const chartOptions = {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    };

    // Check if the chart instance already exists and destroy it
    if (window.sentimentChart) {
      window.sentimentChart.destroy();
    }

    window.sentimentChart = new Chart(ctx, {
      type: "bar",
      data: chartData,
      options: chartOptions,
    });
    window.sentimentChart.resize(600, 600);
  }, [total_sentiments1, total_sentiments2, searchTerms1, searchTerms2]);

  return (
    <div className="chart">
      <canvas ref={chartRef}></canvas>
    </div>
  );
};

export default ComparisonChart;
