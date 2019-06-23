// Some of this code I got from our 17-Mapping-Web/GeoJSON-and-Plugins

// API key
const API_KEY = "pk.eyJ1IjoiYmFsYXJ6NGxpZmUiLCJhIjoiY2p3c2wyY2RsMDVtcTQycWs3eG96YTZvcyJ9.qLv_1bPBgNFsyztEAvxrpA";

// Creating map object
var myMap = L.map("mapid", {
  center: [40.7128, -74.0059],
  zoom: 4
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Link to the data I want to collet and plot
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"

// Grabbing our GeoJSON data..
d3.json(link, function(data) {

  // 
  
  // Creating a GeoJSON layer with the retrieved data from 'link' above
  L.geoJson(data).addTo(myMap); {
  
    // Binding a pop-up to each layer
  // look at geojson to add our popup including magnitude and location
  onEachFeature: function(feature, layer) {
    layer.bindPopup("Magnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place);
  }.addTo(map);
  
  // create a legend for the bottom right corner
  var legend = L.control({
    position: "bottomright"
  });
  }
});