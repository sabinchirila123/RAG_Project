import { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [message, setMessage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setResponse(null);
    setMessage(null);

    try {
      const res = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
      });

      const data = await res.json();

      if (data.blocked) {
        setMessage(data.message);
      } else if (data.found === false) {
        setMessage(data.message);
      } else if (data.recommendation && data.title) {
        setResponse(data);
      } else {
        setMessage("Something went wrong. Please try again.");
      }
    } catch (error) {
      console.error("Network error:", error);
      setMessage("Network error. Please check your connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="bg-ornaments" aria-hidden="true" />
      <header className="header">
        <h1 className="title">Smart Librarian · <span className="accent">Chatbot</span></h1>
        <p className="subtitle">Find the perfect book by theme—fast, friendly, and a little magical</p>
      </header>

      <div className="card">
        <div className="input-row">
          <input
            type="text"
            placeholder="What theme do you want the book to have?"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Book theme"
          />
          <button
            onClick={handleSubmit}
            disabled={loading}
            className={`btn ${loading ? 'loading' : ''}`}
            aria-busy={loading}
          >
            {loading ? <span className="spinner" aria-hidden="true" /> : null}
            {loading ? "Searching..." : "Find Book"}
          </button>
        </div>

        {message && (
          <div className="message warning" role="status">
            {message}
          </div>
        )}

        {response && (
          <div className="response">
            <h2 className="book-title">{response.title}</h2>
            <p className="book-text">{response.recommendation}</p>

            {response.audio_url && (
              <div className="audio-block">
                <div className="audio-label">Listen to the recommendation</div>
                <audio controls className="audio-player">
                  <source src={response.audio_url} type="audio/mpeg" />
                  Your browser does not support audio playback.
                </audio>
              </div>
            )}

            {response.image_url && (
              <img
                src={response.image_url}
                alt={`Generated cover for ${response.title}`}
                className="book-image"
              />
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
