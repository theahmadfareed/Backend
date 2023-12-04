import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const BarChart = ({ total_sentiments }) => {
  const chartRef = useRef(null);
  const chartInstanceRef = useRef(null); // Reference to the Chart.js instance

  useEffect(() => {
    const ctx = chartRef.current.getContext("2d");

    const chartData = {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [
        {
          label: "Bar-Chart",
          data: [
            total_sentiments.positive_count,
            total_sentiments.negative_count,
            total_sentiments.neutral_count,
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

    // Destroy the previous Chart.js instance (if it exists)
    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy();
    }

    // Create a new Chart.js instance
    chartInstanceRef.current = new Chart(ctx, {
      type: "bar",
      data: chartData,
      options: chartOptions,
    });
  }, [total_sentiments]);

  return (
    <div className="chart">
      <canvas ref={chartRef}></canvas>
    </div>
  );
};

export default BarChart;
