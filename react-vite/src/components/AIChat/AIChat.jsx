import { useState, useEffect, useRef } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { FaWandMagicSparkles } from "react-icons/fa6";
import { IoIosCloseCircleOutline } from "react-icons/io";
import "./AIChat.css";

function AIChat() {
  const [query, setQuery] = useState("");
  const [isVisible, setIsVisible] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState(null);

  const itinerariesObj = useSelector(
    (state) => state.itineraries.allItineraries
  );
  const itineraries = itinerariesObj ? Object.values(itinerariesObj) : [];

  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [chatHistory]);

  const handleSubmit = async () => {
    if (!query) return;
    setLoading(true);

    const lowerQuery = query.toLowerCase();

    // Match country
    const matchedCountry = Object.keys(destinationMap).find((country) =>
      lowerQuery.includes(country.toLowerCase())
    );

    // Match city
    let matchedCity = null;
    for (const country of Object.keys(destinationMap)) {
      matchedCity = destinationMap[country].find((city) =>
        lowerQuery.includes(city.toLowerCase())
      );
      if (matchedCity) {
        break;
      }
    }

    // Either city or country match found
    if (matchedCity || matchedCountry) {
      const cities = matchedCity
        ? [matchedCity]
        : destinationMap[matchedCountry];
      const matchedItineraries = itineraries.filter((itinerary) =>
        cities.some(
          (city) =>
            itinerary.title.toLowerCase().includes(city.toLowerCase()) ||
            itinerary.description.toLowerCase().includes(city.toLowerCase())
        )
      );

      const topMatches = matchedItineraries.slice(0, 3).map((itinerary) => (
        <Link to={`/itineraries/${itinerary.id}`} key={itinerary.id}>
          <div className="chat_recommendation_preview bot-message">
            <img src={itinerary.preview_image_url} alt={itinerary.title} />
            <div className="chat_recommendation_desc">
              <h3>{itinerary.title}</h3>
              <div>Duration: {itinerary.duration} days</div>
            </div>
          </div>
        </Link>
      ));

      setChatHistory((prev) => [
        ...prev,
        { type: "user", content: query },
        {
          type: "bot",
          content:
            topMatches.length > 0
              ? topMatches
              : `No recommendations found for ${
                  matchedCity || matchedCountry
                }.`,
        },
      ]);

      setQuery("");
      setLoading(false);
      return;
    }

    // No match? Use AI
    const res = await fetch("/api/ai/recommendations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();

    setChatHistory((prevHistory) => [
      ...prevHistory,
      { type: "user", content: query },
      {
        type: "bot",
        content: data.choices
          ? data.choices[0].message.content
          : "No recommendation received.",
      },
    ]);

    setQuery("");
    setLoading(false);
  };

  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };

  const destinationMap = {
    "United States": [
      "Boston",
      "New York",
      "Pittsburgh",
      "New Orleans",
      "Utah",
      "California",
      "Key West",
      "Hawaii",
    ],
    Canada: ["Toronto"],
    Mexico: ["Tulum", "Cancun"],
    China: ["Hangzhou", "Shanghai", "Shenzhen"],
    Japan: ["Tokyo"],
  };

  return (
    <div className="aichat-container">
      {isVisible && (
        <div className="aichat-wrapper">
          <div
            className="aichat-close"
            onClick={() => {
              setIsVisible(false);
              setChatHistory([]);
              setSelectedCountry(null);
              setQuery("");
            }}
          >
            <IoIosCloseCircleOutline />
          </div>

          <div className="aichat-window">
            <div className="aichat-bubble bot-message">
              <p>Got a destination in mind? I can help you plan the trip!</p>
            </div>
            <div className="aichat-bubble aichat-choice">
              {Object.keys(destinationMap).map((country) => (
                <button
                  id="green-button"
                  key={country}
                  onClick={() => {
                    setSelectedCountry(country);
                    setChatHistory((prevHistory) => [
                      ...prevHistory,
                      {
                        type: "bot",
                        content: `Great choice! Any specific city you want to explore in ${country}?`,
                      },
                    ]);
                  }}
                >
                  {country}
                </button>
              ))}
            </div>
            {chatHistory.map((message, index) => (
              <div key={index}>
                <div
                  key={index}
                  className={`aichat-bubble ${
                    message.type === "user" ? "user-message" : "bot-message"
                  }`}
                >
                  <p>{message.content}</p>
                </div>
                {message.type === "bot" &&
                  message.content.includes(
                    "Any specific city you want to explore"
                  ) &&
                  selectedCountry && (
                    <div className="aichat-bubble aichat-choice">
                      {destinationMap[selectedCountry].map((city) => (
                        <button
                          id="green-button"
                          key={city}
                          onClick={() => {
                            const cityItineraries = itineraries.filter(
                              (itinerary) =>
                                itinerary.title
                                  .toLowerCase()
                                  .includes(city.toLowerCase()) ||
                                itinerary.description
                                  .toLowerCase()
                                  .includes(city.toLowerCase())
                            );

                            const result = cityItineraries.length
                              ? cityItineraries.slice(0, 3).map((itinerary) => (
                                  <div key={itinerary.id}>
                                    <Link to={`/itineraries/${itinerary.id}`}>
                                      <div className="chat_recommendation_preview bot-message">
                                        <img
                                          src={itinerary.preview_image_url}
                                          alt={itinerary.title}
                                        />
                                        <div className="chat_recommendation_desc">
                                          <h3>{itinerary.title}</h3>
                                          <div>
                                            Duration: {itinerary.duration} days
                                          </div>
                                        </div>
                                      </div>
                                    </Link>
                                    {/* <button
                                      id="green-button-full-width"
                                      onClick={async () => {
                                        const res = await fetch(
                                          "/api/ai/schedule",
                                          {
                                            method: "POST",
                                            headers: {
                                              "Content-Type":
                                                "application/json",
                                            },
                                            body: JSON.stringify({
                                              title: itinerary.title,
                                            }),
                                          }
                                        );

                                        const data = await res.json();
                                        const schedule =
                                          data.schedule || "No schedule found.";

                                        setChatHistory((prev) => [
                                          ...prev,
                                          { type: "bot", content: schedule },
                                        ]);
                                      }}
                                    >
                                      Schedule of This Itinerary
                                    </button> */}
                                  </div>
                                ))
                              : "No recommendations found for this city.";

                            setChatHistory((prev) => [
                              ...prev,
                              { type: "bot", content: result },
                            ]);

                            setQuery("");
                          }}
                        >
                          {city}
                        </button>
                      ))}
                    </div>
                  )}
              </div>
            ))}
          </div>
          <div className="chat-input">
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask me anything about your next trip :)"
            />
            <button onClick={handleSubmit}>
              {loading ? "Sending" : "Send"}
            </button>
          </div>
        </div>
      )}
      <h2 onClick={toggleVisibility} style={{ cursor: "pointer" }}>
        <span>
          <FaWandMagicSparkles />
        </span>
        <span> AI Assistant</span>
      </h2>
    </div>
  );
}

export default AIChat;
