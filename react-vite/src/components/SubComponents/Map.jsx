import { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import "leaflet-geosearch/dist/geosearch.css";
import "leaflet/dist/leaflet.css";

function SearchField({ setPosition }) {
  const map = useMap();

  useEffect(() => {
    const provider = new OpenStreetMapProvider();

    const searchControl = new GeoSearchControl({
      provider,
      style: "bar",
      autoClose: true,
      keepResult: true,
    });

    map.addControl(searchControl);

    map.on("geosearch/showlocation", (result) => {
      const { x, y } = result.location;
      setPosition([y, x]);
      map.setView([y, x], 13);
    });

    return () => {
      map.removeControl(searchControl);
    };
  }, [map, setPosition]);

  return null;
}

const Map = (itinerary) => {
  const [position, setPosition] = useState(null);

  const handleMarkerClick = () => {
    console.log("Marker clicked", position);
  };
  const centerPosition = itinerary.itinerary.schedules[0].activities[0];

  return (
    <MapContainer
      center={[centerPosition.latitude, centerPosition.longitude]}
      zoom={13}
      style={{ height: "100vh", width: "40%", position: "fixed", botton: 0, right: 0}}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <SearchField setPosition={setPosition} />
      {itinerary.itinerary.schedules.map((schedule, index) =>
        schedule.activities.map((activity, idx) => (
          <Marker
            key={`${index}-${idx}`}
            position={[activity.latitude, activity.longitude]}
            eventHandlers={{ click: () => handleMarkerClick(activity) }}
          >
            <Popup>
              <div><img src={activity.place_image_url} alt={activity.id} style={{ width: "300px", height: "auto", aspectRatio: "4 / 3" }}/></div>
              <div>{activity.place} ({schedule.day})</div>
              
            </Popup>
          </Marker>
        ))
      )}

    </MapContainer>
  );
};

export default Map;