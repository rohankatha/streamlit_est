import folium as fl
from streamlit_folium import st_folium
import streamlit as st
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
 
    
def get_pos(lat, lng):
    return lat, lng


m = fl.Map()

m.add_child(fl.LatLngPopup())

map = st_folium(m, height=350, width=700)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    

if data is not None:
    data = list(data)
    data[0] = str(data[0])
    data[1] = str(data[1])
    location = geolocator.geocode(data[0]+","+data[1])# Writes to the app
    print(data[0]) # Writes to terminal
