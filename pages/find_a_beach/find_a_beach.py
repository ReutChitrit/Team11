from datetime import datetime
from flask import render_template, Blueprint, redirect, url_for, request, session
from meteostat import Point, Daily
from geopy.geocoders import Nominatim

from pages.find_a_beach.class_find_a_beach import display_all_cities, fetch_func, display_certain_cities

find_a_beach = Blueprint('find_a_beach', __name__, static_folder='static',
                         static_url_path='/find_a_beach',
                         template_folder='templates')


@find_a_beach.route('/find_a_beach')
def findabeachfunc():
    query = display_all_cities()
    cities = fetch_func(query)
    return render_template('find_a_beach.html', cities=cities)


@find_a_beach.route('/get_city_by_geolocation')
def get_city_by_geolocation():
    latitude = request.args['latitude']
    longitude = request.args['longitude']
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(latitude + "," + longitude)
    city = location.address.split(",")[-5]
    weather = get_weather(latitude=latitude, longitude=longitude)
    session['city'] = city
    session['weatherMin'] = weather[0]
    session['weatherMax'] = weather[1]
    return redirect(url_for('find_a_beach.findabeachfunc'))


@find_a_beach.route('/choose_city')
def choose_city_func():
    city = request.args['city']
    query = display_certain_cities(city)
    gps_list = fetch_func(query)
    weather = get_weather(latitude=gps_list[0][0], longitude=gps_list[0][1])
    session['city'] = city
    session['weatherMin'] = weather[0]
    session['weatherMax'] = weather[1]
    return redirect(url_for('find_a_beach.findabeachfunc'))


@find_a_beach.route('/')
def redirectfunc():
    return redirect(url_for('find_a_beach.findabeachfunc'))


def get_weather(latitude, longitude):
    start = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
    end = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
    city = Point(float(latitude), float(longitude), 0)
    data = Daily(city, start, end)
    data = data.fetch()
    tempmin = 0
    tempmax = 0
    if len(data.tmin) > 0:
        tempmin = data.tmin[0]
    if len(data.tmax) > 0:
        tempmax = data.tmax[0]
    return tempmin, tempmax
