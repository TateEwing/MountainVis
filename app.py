import streamlit as st
import pandas as pd
import pydeck as pdk



@st.cache_data
def load_data():
    return pd.read_csv('data/activities_cloud.csv')

df = load_data()

deck = pdk.Deck(
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

st.title("My Outdoor Activity :man-mountain-biking: :snowboarder: :snow_capped_mountain:")
st.pydeck_chart(deck)
st.write('''
This is a quick project I put together to refresh my skills working with data, and to learn about :red[Streamlit].
My GPS location is represented in a cloud of points, with elevation gain within each activity represented by the color gradient.

The data are from :orange[Strava], an app I use to track my :green[outdoor activities] :camping:.
Scroll to the east along I-90 to see some of my regular spots.
Most of my activities are around Seattle, but if you zoom out you'll see some places I've traveled to :car: :smile:.
''')