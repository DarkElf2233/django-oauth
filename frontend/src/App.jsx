import "./App.css";
import axios from "axios";
import { useState } from "react";

function App() {
  const [token, setToken] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    const form = e.currentTarget;
    const username = form[0].value;
    const password = form[1].value;

    const formData = new URLSearchParams();
    formData.append("grant_type", "password");
    formData.append("client_id", "BMVXUFRVLmd87uVTrxzvM5kdimPbHyB4AEdmwHeO");
    formData.append("client_secret", "wASBM9oWqvpaHxx1diyGqCHLABYBuiv6OWLf9ErHcRK0SMqNt4Izeo5q0zQWaeEuRO7ydqWlNEBqCeYMyPkDfEwrCeab9OKZDjMxcTMPDoyTQZfRvFwT4qkCx80Epghn");
    formData.append("username", username);
    formData.append("password", password);

    axios
      .post("http://localhost:8000/api/token/", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
      .then((response) => {
        setToken(response.data.access_token)
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>Username</label>
        <input type="text" />
        <br />
        <br />
        <label>Password</label>
        <input type="text" />
        <br />
        <br />
        <button type="submit">Send</button>
      </form>
      <h3>Token: {token}</h3>
      <br />
      <p></p>
    </div>
  );
}

export default App;
