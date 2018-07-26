

var Marker = function(data) {

  this.title =  ko.observable(data.title);
  this.location = ko.observable(data.location);
  
}


var ViewModel = function() {
  // Create a new blank array for all the listing markers.
  this.markers = ko.observableArray([]);
}


function initMap() {

  controller = new ViewModel();
  var map;
  // Constructor creates a new map - only center and zoom are required.
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -7.229424, lng:  -35.898343},
    zoom: 14
  });

  var locations = [
    new Marker({title: 'Lanchonete mia', location: {lat: -7.232765, lng:  -35.903655}}),
    new Marker({title: 'Lanchonete do elano', location: {lat: -7.223078, lng: -35.906854}}),
    new Marker({title: 'Panquecaria da liberdade', location: {lat: -7.235501, lng: -35.893141}}),
    new Marker({title: 'Forno de pizza', location: {lat: -7.227508, lng: -35.891262}}),
    new Marker({title: 'Realeza pizza', location: {lat: -7.232404, lng: -35.886155}}),
    new Marker({title: 'Pizzaria do danda', location: {lat: -7.240748, lng: -35.900961}}),
  ];
  
  var largeInfowindow = new google.maps.InfoWindow();
  var bounds = new google.maps.LatLngBounds();
  
  // The following group uses the location array to create an array of markers on initialize.
  for (var i = 0; i < locations.length; i++) {
    // Get the position from the location array.
    var position = locations[i].location();
    var title = locations[i].title();
    // Create a marker per location, and put into markers array.
    var marker = new google.maps.Marker({
      map: map,
      position: position,
      title: title,
      animation: google.maps.Animation.DROP,
      id: i
    });
    // Push the marker to our array of markers.
    controller.markers.push(marker);
    // Create an onclick event to open an infowindow at each marker.
    marker.addListener('click', function() {
      populateInfoWindow(this, largeInfowindow);
    });
    bounds.extend(controller.markers()[i].position);
  }
  // Extend the boundaries of the map for each marker
  map.fitBounds(bounds);
}




// This function populates the infowindow when the marker is clicked. We'll only allow
// one infowindow which will open at the marker that is clicked, and populate based
// on that markers position.
function populateInfoWindow(marker, infowindow) {
  // Check to make sure the infowindow is not already opened on this marker.
  if (infowindow.marker != marker) {
    infowindow.marker = marker;
    infowindow.setContent('<div>' + marker.title + '</div>');
    infowindow.open(map, marker);
    // Make sure the marker property is cleared if the infowindow is closed.
    infowindow.addListener('closeclick',function(){
      infowindow.setMarker = null;
    });
  }
}

ko.applyBindings(new ViewModel());