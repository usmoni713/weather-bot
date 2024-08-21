BOT_API_TOKEN = "YOUR_BOT_API_TOKEN"
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY" #from https://home.openweathermap.org/api_keys

CURRENT_WEATHER_API_CALL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + WEATHER_API_KEY + "&units=metric"
)

CACHE_TIME = 60 * 5  # In seconds
