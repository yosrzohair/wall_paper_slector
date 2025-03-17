import sys
import requests
from datetime import datetime, timezone

def get_sun_times(latitude, longitude):
    """Fetch sunrise and sunset times in UTC from API."""
    url = f"https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}"
    response = requests.get(url)
    data = response.json()
    return data["results"]["sunrise"], data["results"]["sunset"]

def get_current_utc_time():
    """Get current UTC time as HH:MM:SS."""
    return datetime.now(timezone.utc).strftime("%H:%M:%S")

def select_wallpaper(sunrise, sunset, current_time):
    """Decide the correct wallpaper based on time."""
    if current_time < sunrise:
        return "night.png"
    elif current_time < "06:00:00":
        return "sunrise.png"
    elif current_time < "12:00:00":
        return "morning.png"
    elif current_time < "17:00:00":
        return "afternoon.png"
    elif current_time < sunset:
        return "sunset.png"
    else:
        return "night.png"

def main():
    if len(sys.argv) != 3:
        print("Usage: python wallpaper_selector.py <latitude> <longitude>")
        return
    
    latitude, longitude = sys.argv[1], sys.argv[2]
    sunrise, sunset = get_sun_times(latitude, longitude)
    current_time = get_current_utc_time()
    wallpaper = select_wallpaper(sunrise, sunset, current_time)
    print(wallpaper)  # Output the wallpaper name

if __name__ == "__main__":
    main()
