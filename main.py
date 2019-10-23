from flask import Flask
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route("/")
def geo():
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.reverse("18.847981, -97.099029")
    return location.address

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)