import requests
import os
from dotenv import load_dotenv
load_dotenv()
NASA_API =os.getenv("NASA_API")
def apod(date):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": NASA_API,  
        "date": date       # YYYY-MM-DD
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data


