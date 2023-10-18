import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const LineChart = (props) => {

  const d = props.line_data.Dates; //["2020-11-12","2023-01-05","2023-07-29","2023-09-17","2023-09-18"]
  const p = props.line_data.Positive; //[1,0,1,1,0]
  const n = props.line_data.Negative; //[1,4,1,6,0]
  const ne = props.line_data.Neutral; //[9,7,1,9,0]

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
        fill: true,
      },
      {
        label: "Negative",
        data: n,
        backgroundColor: "rgba(255, 0, 0, 0.2)",
        borderColor: "rgba(255, 0, 0, 1)",
        fill: true,
      },
      {
        label: "Neutral",
        data: ne,
        backgroundColor: "rgba(0, 0, 255, 0.2)",
        borderColor: "rgba(0, 0, 255, 1)",
        fill: true,
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

    chart.resize(1000, 600);
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
