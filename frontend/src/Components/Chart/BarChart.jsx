import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import "./style.css";


const BarChart = ({ total_sentiments }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    const ctx = chartRef.current.getContext("2d");

    const chartData = {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [
        {
          label: "Bar-Chart",
          data: [
            total_sentiments.total_positive,
            total_sentiments.total_negative,
            total_sentiments.total_neutral,
          ],
          backgroundColor: ["green", "red", "blue"],
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
  }, [total_sentiments]);

  return (
    <div className="chart">
      <canvas ref={chartRef}></canvas>
    </div>
  );
};

export default BarChart;

