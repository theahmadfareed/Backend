import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const LineChart = (props) => {

  const d = props.line_data.Dates;
  const p = props.line_data.Positive;
  const n = props.line_data.Negative;
  const ne = props.line_data.Neutral;

  // console.log(d)
  // console.log(p)
  // console.log(n)
  // console.log(ne)

  const chartRef = useRef(null);

  useEffect(() => {
    const canvas = chartRef.current;
    const ctx = canvas.getContext("2d");

    const data = [
      {
        label: "Positive",
        data: p,
        backgroundColor: "rgba(0, 128, 0, 0.2)",
        borderColor: "rgba(0, 128, 0, 1)",
      },
      {
        label: "Negative",
        data: n,
        backgroundColor: "rgba(255, 0, 0, 0.2)",
        borderColor: "rgba(255, 0, 0, 1)",
      },
      {
        label: "Neutral",
        data: ne,
        backgroundColor: "rgba(0, 0, 255, 0.2)",
        borderColor: "rgba(0, 0, 255, 1)",
      },
    ];

    const options = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    };

    const chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: d,
        datasets: data,
      },
      options: options,
    });

    chart.resize(650, 600);
    return () => {
      chart.destroy();
    };
  }, [d,n,ne,p]);

  return (
    <div className="chart">
      <canvas ref={chartRef} />
    </div>
  );
};

export default LineChart;
