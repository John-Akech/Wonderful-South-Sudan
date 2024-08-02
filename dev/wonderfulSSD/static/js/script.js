// JavaScript to initialize the biodiversity map
document.addEventListener('DOMContentLoaded', function() {
  // Example map initialization with Leaflet.js
  const map = L.map('biodiversity-map').setView([4.859, 29.639], 6); // Coordinates for South Sudan

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // Add markers or other map features here
  // Example marker
  L.marker([4.859, 29.639]).addTo(map)
      .bindPopup('South Sudan')
      .openPopup();
});
