import { useState } from "react";
import { FaWandMagicSparkles } from "react-icons/fa6";

function AIAssistant() {
  const [query, setQuery] = useState("");
  const [isVisible, setIsVisible] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query) return;
    setLoading(true);

    const res = await fetch("/api/ai/recommendations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: query }),
    });

    const data = await res.json();

    // Add both the query and response to chat history
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

  return (
    <div className="ai-container">
      <h2 onClick={toggleVisibility} style={{ cursor: "pointer" }}>
        <span>
          <FaWandMagicSparkles />
        </span>
        <span> AI Assistant</span>
      </h2>
      {isVisible && (
        <div className="ai-chat">
          <div className="chat-window">
            {chatHistory.map((message, index) => (
              <div
                key={index}
                className={`chat-bubble ${
                  message.type === "user" ? "user-message" : "bot-message"
                }`}
              >
                <p>{message.content}</p>
              </div>
            ))}
            {loading && (
              <div className="chat-bubble bot-message">
                <p>Loading...</p>
              </div>
            )}
          </div>

          <div className="chat-input">
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder='Ask me questions like "top 10 tourist destinations in San Francisco"'
            />
            <button onClick={handleSubmit}>
              {loading ? "Sending" : "Send"}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default AIAssistant;
