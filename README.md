# 🌤️ Weather API by IP (Django)

This project is a Django-based Weather API that fetches real-time weather data based on the user's IP address. It uses the OpenWeatherMap API to get weather info and caches responses for better performance. The API is also rate-limited to prevent abuse.

### 🚀 Live Demo

Check it out live on Render:  
👉 [https://weatherapi-raptorx.onrender.com/weather-by-ip?ip=45.115.190.20](https://weatherapi-raptorx.onrender.com/weather-by-ip?ip=45.115.190.20)

---

## 📦 Features

- 🌍 Get weather info by providing an IP address.
- 📦 Caching (in-memory) with 10-minute expiry to reduce API calls.
- 🚫 Rate limiting: Max 10 requests per client per ipaddress within 10 minutes.
- 🧪 IP validation and graceful error handling.
- 📤 Deployed using Render's free-tier hosting.

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 4.x
- OpenWeatherMap API (`home.openweathermap.org`)
- IP Geolocation API (`ipinfo.io`)
- In-Memory Caching (Django `cache`)
- Render (for deployment)

---

<!--
## 📂 Project Structure

--- -->

## 🚀 Getting Started Locally

### Clone the Repo

```bash
git clone https://github.com/yourusername/raptorX-weather-api.git
cd raptorX-weather-api
```

### Create and Activate Virtual Environment (Optional)

```bash
python -m venv .venv
.venv\Scripts\activate # on windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a .env File

```bash
OPENWEATHER_API_KEY=your_openweather_api_key_here
IPINFO_TOKEN=your_ipinfo_token_here
```

### Run the Server

```bash
python manage.py runserver
```

Now, go to: `http://127.0.0.1:8000/weather-by-ip?ip=<your-preferred-ip-address>`

## 📌 API Usage

### Endpoint:

```bash
GET /weather-by-ip?ip=<IP_ADDRESS>
```

### Example:

```bash
curl https://weatherapi-raptorx.onrender.com/weather-by-ip?ip=101.178.192.51
```

### Response:

```bash
{
  "ip": "101.178.192.51",
  "location": {
    "city": "Jaipur",
    "country": "India"
  },
  "weather": {
    "temperature": 33.5,
    "humidity": 45,
    "description": "clear sky"
  }
}
```

## ⚠️ Rate Limiting

- A maximum of 10 requests per city are allowed within 10 minutes.

- If the limit is exceeded, you'll get:

```bash
{ "error": "Rate limit exceeded" }
```

## 🧼 To Do

- Add Redis or Memcached support.

- Add proper unit tests with pytest or unittest.

- Improve frontend with a small UI.

## 🙌 Acknowledgments

- OpenWeatherMap

- ip-api.com

- Render
