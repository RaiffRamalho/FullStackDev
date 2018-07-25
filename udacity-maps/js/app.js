
var map;
function initMap() {
  // Constructor creates a new map - only center and zoom are required.
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -7.2427512, lng: -35.9366696},
    zoom: 14
  });
}
