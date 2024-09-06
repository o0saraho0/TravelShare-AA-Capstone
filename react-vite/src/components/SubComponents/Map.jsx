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

const Map = ({ itinerary, showSearchField, isEditing, updateAcitivity }) => {
  const [searchPosition, setSearchPosition] = useState(null);
  const defaultCenter = { latitude: 37.7749, longitude: -122.4194 };
  const centerPosition =
    itinerary.schedules?.[0]?.activities?.[0] || defaultCenter;

  const searchMarkerRef = useRef(null);

  const handleSearchMarkerClick = () => {
    if (searchPosition) {
      updateAcitivity(searchPosition); // This updates the activity with the new search position
    }
    setSearchPosition(null); // Clear search marker after adding
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
    </MapContainer>
  );
};

export default Map;
