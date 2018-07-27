

var Marker = function(data) {

  this.title =  data.title;
  this.location = data.location;
  
}


var ViewModel = function(map, bounds, largeInfowindow) {

  self = this;

  self.titleFilter = ko.observable("");

  self.locations = ko.observableArray([]);
  self.markers = [];

  self.map = map;
  self.bounds = bounds;
  self.largeInfowindow = largeInfowindow;
  
  self.updateMarkers = function (arrayData){

    // Style the markers a bit. This will be our listing marker icon.
    var defaultIcon = makeMarkerIcon('4B8994');

    // Create a "highlighted location" marker color for when the user
    // mouses over the marker.
    var highlightedIcon = makeMarkerIcon('FFFF24');

    // The following group uses the location array to create an array of markers on initialize.
    for (var i = 0; i < arrayData.length; i++) {
      // Get the position from the location array.
      var position = arrayData[i].location;
      var title = arrayData[i].title;
      // Create a marker per location, and put into markers array.
      var marker = new google.maps.Marker({
        map: this.map,
        position: position,
        title: title,
        animation: google.maps.Animation.DROP,
        id: i
      });
      // Push the marker to our array of markers.
      self.locations.push(marker);       
      // Create an onclick event to open an infowindow at each marker.
      marker.addListener('click', function() {
        populateInfoWindow(this, self.largeInfowindow);
      });
      marker.setIcon(defaultIcon);
      // Two event listeners - one for mouseover, one for mouseout,
      // to change the colors back and forth.
      marker.addListener('mouseover', function() {
        this.setIcon(highlightedIcon);
      });
      marker.addListener('mouseout', function() {
        this.setIcon(defaultIcon);
      });
      this.bounds.extend(self.locations()[i].position);
    }
  }


  self.showMarkerInfo = function(data) {
    populateInfoWindow(data, self.largeInfowindow)
  }


  // everytime query/placeList changes, this gets computed again
  self.filteredPlaces = ko.computed(function() {
    if (!self.titleFilter()) {
      for (let index = 0; index < self.locations().length; index++) {
        self.locations()[index].setMap(map);
      }
      return self.locations();
    } else {

      return self.locations()
        .filter(function(location) {
          var boolTit = location.title.toUpperCase().indexOf(self.titleFilter().toUpperCase()) > -1;
          if (boolTit) {
            location.setMap(map);
          } else {
            location.setMap(null);
          }

          return boolTit});
    }
  });


}


function initMap() {

  var map;
  //info to put on markers
  var largeInfowindow = new google.maps.InfoWindow();
  //bound markers on map
  var bounds = new google.maps.LatLngBounds();

  // Constructor creates a new map - only center and zoom are required.
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -7.229424, lng:  -35.898343},
    zoom: 14
  });

  //defatult data to load
  var locations = [
    new Marker({title: 'Lanchonete mia', location: {lat: -7.232765, lng:  -35.903655}}),
    new Marker({title: 'Lanchonete do elano', location: {lat: -7.223078, lng: -35.906854}}),
    new Marker({title: 'Panquecaria da liberdade', location: {lat: -7.235501, lng: -35.893141}}),
    new Marker({title: 'Forno de pizza', location: {lat: -7.227508, lng: -35.891262}}),
    new Marker({title: 'Realeza pizza', location: {lat: -7.232404, lng: -35.886155}}),
    new Marker({title: 'Pizzaria do danda', location: {lat: -7.240748, lng: -35.900961}}),
  ];

  controller = new ViewModel(map, bounds, largeInfowindow);
  controller.updateMarkers(locations);
  ko.applyBindings(controller);
  // Extend the boundaries of the map for each marker
  map.fitBounds(controller.bounds);

  	
  // $( ".map" ).append( "<span style='font-size:30px;cursor:pointer' onclick='openNav()'>&#9776; open</span>" );
}

// This function takes in a COLOR, and then creates a new marker
// icon of that color. The icon will be 21 px wide by 34 high, have an origin
// of 0, 0 and be anchored at 10, 34).
function makeMarkerIcon(markerColor) {
  var markerImage = new google.maps.MarkerImage(
    'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|'+ markerColor +
    '|40|_|%E2%80%A2',
    new google.maps.Size(21, 34),
    new google.maps.Point(0, 0),
    new google.maps.Point(10, 34),
    new google.maps.Size(21,34));
  return markerImage;
}



// This function populates the infowindow when the marker is clicked. We'll only allow
// one infowindow which will open at the marker that is clicked, and populate based
// on that markers position.
function populateInfoWindow(marker, infowindow) {
  // Check to make sure the infowindow is not already opened on this marker.
  if (infowindow.marker != marker) {
    // infowindow.marker = marker;
    // infowindow.setContent('<div>' + marker.title + '</div>');
    // infowindow.open(map, marker);
    // // Make sure the marker property is cleared if the infowindow is closed.
    // infowindow.addListener('closeclick',function(){
    //   infowindow.setMarker = null;
    // });

    infowindow.setContent('');
    infowindow.marker = marker;
    // Make sure the marker property is cleared if the infowindow is closed.
    infowindow.addListener('closeclick', function() {
      infowindow.marker = null;
    });
    var streetViewService = new google.maps.StreetViewService();
    var radius = 50;
    // In case the status is OK, which means the pano was found, compute the
    // position of the streetview image, then calculate the heading, then get a
    // panorama from that and set the options
    function getStreetView(data, status) {
      if (status == google.maps.StreetViewStatus.OK) {
        var nearStreetViewLocation = data.location.latLng;
        var heading = google.maps.geometry.spherical.computeHeading(
          nearStreetViewLocation, marker.position);
          infowindow.setContent('<div>' + marker.title + '</div><div id="pano"></div>');
          var panoramaOptions = {
            position: nearStreetViewLocation,
            pov: {
              heading: heading,
              pitch: 30
            }
          };
        var panorama = new google.maps.StreetViewPanorama(
          document.getElementById('pano'), panoramaOptions);
      } else {
        infowindow.setContent('<div>' + marker.title + '</div>' +
          '<div>No Street View Found</div>');
      }
    }
    // Use streetview service to get the closest streetview image within
    // 50 meters of the markers position
    streetViewService.getPanoramaByLocation(marker.position, radius, getStreetView);
    // Open the infowindow on the correct marker.
    infowindow.open(map, marker);
  }
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

