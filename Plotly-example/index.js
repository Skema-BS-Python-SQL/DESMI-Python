var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'markers'
};

var trace2 = {
  x: [2, 3, 4, 5],
  y: [16, 5, 11, 10],
  mode: 'lines'
};

var trace3 = {
  x: [1, 2, 3, 4],
  y: [12, 9, 15, 12],
  mode: 'lines+markers'
};

var trace4 = {
  x: [1, 2, 3, 4],
  y: [15, 12, 12, 18],
  mode: 'lines+markers'
};

var data = [ trace1, trace2, trace3, trace4 ];

var layout = {};

Plotly.newPlot('myDiv', data, layout);