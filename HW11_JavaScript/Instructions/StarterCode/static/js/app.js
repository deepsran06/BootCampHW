// from data.js
var tableData = data;

// YOUR CODE HERE!

// create a table variable tbody
var tbody = d3.select("tbody");

// function then clear the table
// using arrow and forEach go through the data
// append values for the table by each row and cell

function buildTable(data) {
    tbody.html("");
    data.forEach((tableRow) => {
        var row = tbody.append("tr");
        Object.values(tableRow).forEach((value) => {
            var tableCell = row.append("td");
                tableCell.text(value);
        };
    );
 });
};


function handleClick() {
    d3.event.preventDefault();
    var date = d3.select("#datetime").property("value");
    let filteredData = tableData;
    if (date) {
      filteredData = filteredData.filter(row => row.datetime === date);
    }
    buildTable(filteredData);
  };


d3.selectAll("#filter-btn").on("click", handleClick);
  
buildTable(tableData);
