


var londonMarker = new H.map.Marker({lat:51.5008, lng:-0.1224});


/**
 * Boilerplate map initialization code starts below:
 */

//Step 1: initialize communication with the platform
// In your own code, replace variable window.apikey with your own apikey
var platform = new H.service.Platform({
  'apikey': 'DtJVtn7QFdd_HIRdt3wmFFJwEy46sR4atealbUb8mMY'
});
var defaultLayers = platform.createDefaultLayers();

//Step 2: initialize a map - this map is centered over Europe
var map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map,{
  center: {lat:55.350336, lng:50.911013},
  zoom: 8,
  pixelRatio: window.devicePixelRatio || 1
});
// add a resize listener to make sure that the map occupies the whole container
window.addEventListener('resize', () => map.getViewPort().resize());

//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);
map.addObject(londonMarker);
// Now use the map as required...

var onResult = function(result) {
  var locations = result.Response.View[0].Result,
    position,
    marker;

  var lat_g = locations[0].Location.DisplayPosition.Latitude
  var lng_g = locations[0].Location.DisplayPosition.Longitude
  map.setCenter({lat:lat_g, lng:lng_g});
  map.setZoom(14);
  // Add a marker for each location found
  /*for (i = 0;  i < locations.length; i++) {
  position = {
    lat: locations[i].Location.DisplayPosition.Latitude,
    lng: locations[i].Location.DisplayPosition.Longitude
  };
  map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map,{
  center: {lat:position[lat], lng:position[lng]},
  zoom: 6,
  pixelRatio: window.devicePixelRatio || 1
  });*/
  //var ui = H.ui.UI.createDefault(map, defaultLayers);
};

// Get an instance of the geocoding service:
var geocoder = platform.getGeocodingService();

// Call the geocode method with the geocoding parameters,
// the callback and an error callback function (called if a
// communication error occurs):

sub.onclick = function() {
    var val = document.getElementById('inp').value;
    geocoder.geocode({searchText:val}, onResult, function(e) {
    });
};
        