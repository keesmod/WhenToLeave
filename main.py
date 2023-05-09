import streamlit as st
import os
from dotenv import load_dotenv
import googlemaps

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def display_map_with_traffic(location):
    # Geocode the location to get its latitude and longitude
    geocode_result = gmaps.geocode(location)
    if not geocode_result:
        st.error(f"Could not geocode {location}")
        return

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]

    # Construct the URL for the static map with traffic information
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=12&size=600x400&maptype=roadmap&traffic=yes&key={GOOGLE_MAPS_API_KEY}"

    # Display the map using Streamlit
    st.image(map_url)

st.title("Google Maps Traffic Information")

location = st.text_input("Enter a location:")
if location:
    display_map_with_traffic(location)

