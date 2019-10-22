from flask import Flask
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route("/")
def geo():
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse("18.847981, -97.099029")
    dict = location.raw
    print(dict)
