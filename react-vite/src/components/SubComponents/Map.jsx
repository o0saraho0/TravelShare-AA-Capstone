import { useState, useEffect, useRef } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-geosearch/dist/geosearch.css";

const defaultMarkerIcon = new L.Icon({
  iconUrl: "/images/marker-icon-blue.png",
  shadowUrl: "/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const searchMarkerIcon = new L.Icon({
  iconUrl: "/images/marker-icon-orange.png",
  shadowUrl: "/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

function SearchField({ setPosition }) {
  const map = useMap();

  useEffect(() => {
    const provider = new OpenStreetMapProvider();

    const searchControl = new GeoSearchControl({
      provider,
      style: "bar",
      autoClose: true,
      keepResult: true,
      showMarker: false,
    });

    map.addControl(searchControl);

    map.on("geosearch/showlocation", (result) => {
      const { x, y } = result.location;
      setPosition({ latitude: y, longitude: x, label: result.location.label });
      map.setView([y, x], 13);
    });

    return () => {
      map.removeControl(searchControl);
    };
  }, [map, setPosition]);

  return null;
}

function MapViewController({ hoveredActivity, markersRef, itinerary }) {
  const map = useMap();

  useEffect(() => {
    if (
      hoveredActivity &&
      markersRef.current &&
      markersRef.current[hoveredActivity.id]
    ) {
      const marker = markersRef.current[hoveredActivity.id];
      marker.openPopup();
      map.setView([hoveredActivity.latitude, hoveredActivity.longitude], 13);
    }
  }, [hoveredActivity, markersRef, map]);

  // Fit the map to show all markers
  useEffect(() => {
    if (itinerary.schedules) {
      const bounds = L.latLngBounds(); // Create an empty bounds object

      itinerary.schedules.forEach((schedule) => {
        schedule.activities.forEach((activity) => {
          if (activity.latitude && activity.longitude) {
            bounds.extend([activity.latitude, activity.longitude]); // Extend the bounds to include this activity
          }
        });
      });

      if (bounds.isValid()) {
        map.fitBounds(bounds); // Fit the map to the bounds containing all markers
      }
    }
  }, [itinerary, map]);

  return null;
}

const Map = ({
  itinerary,
  showSearchField,
  isEditing,
  updateActivity,
  hoveredActivity,
}) => {
  const [searchPosition, setSearchPosition] = useState(null);
  const defaultCenter = { latitude: 37.7749, longitude: -122.4194 };

  const centerPosition =
    hoveredActivity ||
    itinerary.schedules?.[0]?.activities?.[0] ||
    defaultCenter;

  const searchMarkerRef = useRef(null);
  const markersRef = useRef({}); // Ref to store markers

  const handleSearchMarkerClick = () => {
    if (searchPosition) {
      // Update the activity using the passed `updateActivity` function
      const placeName = searchPosition.label.split(",")[0];
      updateActivity({
        ...searchPosition,
        place: placeName, // Add the extracted place name to the searchPosition object
      });
      setSearchPosition(null); // Clear the search position after adding it to the activity
    }
  };

  useEffect(() => {
    if (searchMarkerRef.current) {
      searchMarkerRef.current.openPopup();
    }
  }, [searchPosition]);

  return (
    <MapContainer
      center={[centerPosition.latitude, centerPosition.longitude]}
      zoom={10}
      style={{
        height: "100vh",
        width: "40%",
        position: "fixed",
        bottom: 0,
        right: 0,
      }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />

      {/* Render existing activities' markers */}
      {itinerary.schedules?.map((schedule, index) =>
        schedule?.activities?.map((activity, idx) => (
          <Marker
            key={`${index}-${idx}`}
            position={[activity.latitude, activity.longitude]}
            icon={defaultMarkerIcon}
            ref={(el) => {
              if (el) {
                markersRef.current[activity.id] = el; // Store reference to each marker
              }
            }}
          >
            <Popup>
              <div>
                {activity.place_image_url && (
                  <img
                    src={activity.place_image_url}
                    alt={activity.id}
                    style={{
                      width: "300px",
                      height: "auto",
                      aspectRatio: "3 / 2",
                    }}
                  />
                )}
              </div>
              <div>
                {activity.place} ({schedule.day})
              </div>
            </Popup>
          </Marker>
        ))
      )}

      {/* Show search field if search is enabled */}
      {(showSearchField || isEditing) && (
        <SearchField setPosition={setSearchPosition} />
      )}

      {/* Render search marker if available */}
      {searchPosition && (
        <Marker
          position={[searchPosition.latitude, searchPosition.longitude]}
          icon={searchMarkerIcon}
          ref={searchMarkerRef}
        >
          <Popup>
            <h3>Search result:</h3> <br />
            <h4>Label:</h4> {searchPosition.label} <br />
            <br />
            Latitude: {searchPosition.latitude} <br />
            Longitude: {searchPosition.longitude} <br /> <br />
            <div className="itinerary-content">
              <button type="button" onClick={handleSearchMarkerClick}>
                {isEditing ? "Update activity" : "+ Add to activity"}
              </button>
            </div>
          </Popup>
        </Marker>
      )}

      {/* Use MapViewController to update map center on hover */}
      <MapViewController
        hoveredActivity={hoveredActivity}
        markersRef={markersRef}
        itinerary={itinerary} // Pass itinerary to fitBounds
      />
    </MapContainer>
  );
};

export default Map;
