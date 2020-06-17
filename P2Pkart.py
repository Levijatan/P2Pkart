from flask import Flask, render_template
from flask_googlemaps import GoogleMaps as gmf
from flask_googlemaps import Map
import googlemaps

import os

app = Flask(__name__, template_folder="template")

key = os.environ["GOOGLEMAPS_KEY"]
gmf(app, key=key)
gmaps = googlemaps.Client(key=key)
geocode_result = gmaps.geocode("UiO")
lat = float(geocode_result[0]["geometry"]["location"]["lat"])
lon = float(geocode_result[0]["geometry"]["location"]["lng"])

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=lat,
        lng=lon,
        markers=[(lat, lon)]
    )

    return render_template('p2pkart.html', mymap=mymap)
