import { useEffect, useState, useMemo } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import Loading from "../SubComponents/Loading";
import { FaSearch } from "react-icons/fa";
import { FaCalendarDays } from "react-icons/fa6";
import "./ItinerariesListPage.css";

function ItinerariesList() {
  const dispatch = useDispatch();
  const itinerariesObj = useSelector(
    (state) => state.itineraries.allItineraries
  );
  const itineraries = useMemo(
    () => (itinerariesObj ? Object.values(itinerariesObj) : []),
    [itinerariesObj]
  );
  const [searchInput, setSearchInput] = useState("");
  const [filteredItineraries, setFilteredItineraries] = useState(itineraries);
  const [durationFilter, setDurationFilter] = useState("");

  useEffect(() => {
    if (!itinerariesObj) {
      dispatch(thunkAllItineraries());
    }
  }, [dispatch, itinerariesObj]);

  const applyFilters = () => {
    let filtered = itineraries;

    // Apply search filter if there's any input
    if (searchInput) {
      filtered = filtered.filter(
        (itinerary) =>
          itinerary.title.toLowerCase().includes(searchInput.toLowerCase()) ||
          itinerary.description
            .toLowerCase()
            .includes(searchInput.toLowerCase())
      );
    }

    // Apply duration filter after search filter
    if (durationFilter) {
      filtered = filtered.filter((itinerary) => {
        const days = itinerary.duration;
        switch (durationFilter) {
          case "1-2":
            return days >= 1 && days <= 2;
          case "3-5":
            return days > 2 && days <= 5;
          case "6-9":
            return days > 5 && days <= 9;
          case "10+":
            return days > 10;
          default:
            return true;
        }
      });
    }
    setFilteredItineraries(filtered);
  };

  // Search and filter function triggered when search input or duration changes
  useEffect(() => {
    applyFilters();
  }, [searchInput, durationFilter, itineraries]);

  // Duration filter handler
  const handleDurationFilterChange = (e) => {
    setDurationFilter(e.target.value);
  };

  // Search input handler
  const handleSearchInputChange = (e) => {
    setSearchInput(e.target.value);
  };

  if (!itinerariesObj) return <Loading />;

  return (
    <main>
      <div className="landing-explore">
        <h1>Explore</h1>

        <div className="search">
          <div className="search-bar">
            <label className="search-icon">
              <FaSearch />
            </label>
            <input
              type="text"
              placeholder="Search for a destination"
              value={searchInput}
              onChange={handleSearchInputChange}
            />
          </div>

          <div className="filter">
            <label className="search-icon">
              <FaCalendarDays />
            </label>

            <select
              onChange={handleDurationFilterChange}
              value={durationFilter}
            >
              <option value="">All Durations</option>
              <option value="1-2">1-2 Days</option>
              <option value="3-5">3-5 Days</option>
              <option value="6-9">6-9 Days</option>
              <option value="10+">10+ Days</option>
            </select>
          </div>
        </div>

        <h2>Popular destinations</h2>
        <div className="grid-container">
          {filteredItineraries.length ? (
            filteredItineraries.map((itinerary) => (
              <div key={itinerary.id} className="grid-item">
                <Link to={`/itineraries/${itinerary.id}`}>
                  <div className="image-container">
                    <img
                      src={itinerary.preview_image_url}
                      alt={itinerary.title}
                    />
                  </div>
                  <div className="one-line-title">
                    <h3>{itinerary.title}</h3>
                  </div>
                  <div className="list-page-duration">
                    <p>Duration: {itinerary.duration} days</p>
                  </div>
                  <div className="list-page-description">
                    <p>{itinerary.description}</p>
                  </div>
                </Link>
                <Link to={`/itineraries/traveler/${itinerary.traveler.id}`}>
                  <div className="user-profile">
                    <img
                      className="profile-image"
                      src={itinerary.traveler.profile_url}
                      alt={itinerary.traveler_id}
                    />
                    <span>{itinerary.traveler.username}</span>
                  </div>
                </Link>
              </div>
            ))
          ) : (
            <div>
              Oops, no itineraries found at the moment. Try clearing your search
              or filters and continue exploring for other adventures!
            </div>
          )}
        </div>
      </div>
    </main>
  );
}

export default ItinerariesList;
