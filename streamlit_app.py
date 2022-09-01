import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, app, timelapse, rasterviz, eedata, lcmap # import your app modules here

st.set_page_config(page_title="GeoIT App", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": timelapse.app, "title": "Timelapse", "icon": "📷"},
    {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
    {"func": app.app, "title": "Geocode", "icon": "map"},
    
    {"func": rasterviz.app, "title": "Raster Data Visualization", "icon": "🏜️"},
    {"func": eedata.app, "title": "Earth Engine Dataset", "icon": "🌍"},
    {"func": lcmap.app, "title": "Land Cover Mapping", "icon": "🌲"},

]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This App is made to Monitor the Geospatial and environmental factors in Morocco.

        *This analysis will complement CLASP’s ongoing efforts on
        region/county selection and inform a robust, data driven
        prioritization process.

        More menu infos? please visit!: [GeoMID](https://ham811.github.io/streamli_app/)
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
