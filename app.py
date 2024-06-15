import streamlit as st
import pandas as pd
import pydeck as pdk



@st.cache_data
def load_data():
    return pd.read_csv('data/activities_cloud.csv')

df = load_data()

deck = pdk.Deck(
    # api_keys={"mapbox": "pk.eyJ1IjoidGF0ZS1ld2luZyIsImEiOiJjbHhkbjNncW8wN3F1MnBwb284eDRjZTRsIn0.2L99AQ1SOkn06v99tCr3yQ"},
    map_provider="mapbox",
    map_style="mapbox://styles/mapbox/outdoors-v12",
    initial_view_state=pdk.ViewState(latitude=47.6061, longitude=-122.3328, zoom=11, bearing=0, pitch=45),
    layers=[
        pdk.Layer(
            'PointCloudLayer',
            data=df,
            get_position=["longitude", "latitude", "altitude"],
            get_color=["r", "g", "b"],
            get_normal=[0, 0, 15],
            auto_highlight=True,
            pickable=True,
            point_size=3,
        )
    ],
)

st.title("Tate's Outdoor Activity :man-mountain-biking: :snowboarder: :snow_capped_mountain:")
st.pydeck_chart(deck)
st.write('''
This is a project I put together to have some fun with Mapbox and work with my own GPX data.
         
I've spent a lot of time using mapping software to help find spots for these adventures, so it's cool to see what's behind the scenes.

The data are from :orange[Strava], an app I use to track my :green[outdoor activities] :camping:.
Scroll to the east along I-90 to see some of my regular spots. 
Most of my activities are around Seattle, but if you zoom out you'll see some places I've traveled to :car: :smile:.
''')