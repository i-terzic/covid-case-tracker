window.addEventListener("load", async () => {
  const ctx = document.getElementById("myChart").getContext("2d");

  const res = await fetch("http://localhost:5000/api/cases");
  const json = await res.json();
  const endDate = new Date(json[json.length - 1]["date"]);
  const firstDate = new Date();
  firstDate.setDate(endDate.getDate() - 7);
  const labels = [];
  const data = {
    labels: labels,
    datasets: [
      {
        label: "Covid-19 Cases in past 7 days",
        fill: true,
        data: [],
        borderColor: "rgb(75, 192, 192)",
        tension: 0.1,
      },
    ],
  };

  for (let i = 1; i <= 7; ++i) {
    let date = new Date();
    date.setDate(firstDate.getDate() + i);
    let dateString = date.toLocaleDateString();
    labels.push(dateString);
  }

  for (let i = 0; i < 7; ++i) {
    data["datasets"][0]["data"].push(0);
  }

  for (let line of json) {
    let countDate = new Date(line["date"]).toLocaleDateString();
    let index = data["labels"].indexOf(countDate);
    if (index >= 0) {
      data["datasets"][0]["data"][index] = line["count"];
    }
  }

  const myChart = new Chart(ctx, {
    type: "line",
    data: data,
  });
});
