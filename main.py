from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route("/geo")
def geo():
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=10)
    location = geolocator.reverse("18.847981, -97.099029")
    dict = location.raw
    return jsonify(dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)