import folium
import pandas as pd

data = pd.read_csv("volcanoes_data.txt", sep=";")

map = folium.Map(location=[39.071911, -98.644823], min_zoom=3)

fg = folium.FeatureGroup("Volcanoes")

fg.add_child(folium.GeoJson(data=open('world_data.json', 'r', encoding="utf-8-sig").read(), 
style_function = lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 5000000 else 'orange' if 5000000 <= x['properties']['POP2005'] < 60000000 else 'red', 'weight':0.5}))

def markerColor(elev):
    return "green" if elev < 1500 else "orange" if 1500 < elev < 3000 else "red"

def markerSize(elev):
    return 5 if elev < 1500 else 6 if 1500 < elev < 3000 else 7

style = "<a style='font-weight: bold; text-decoration: none; color: black;' href='https://www.google.com/search?q=%%22%s%%22' target='_blank' >%s</a><br>Type: %s<br>Country: %s<br>Height: %sm"
def placeMarker(x):
    iframe = folium.IFrame(html=style % (x.NAME, x.NAME, x.Type, x.Country, x.ELEV), width=220, height=90.5)
    fg.add_child(folium.CircleMarker(location=[x.LAT, x.LON], popup=folium.Popup(iframe), color="grey", fill_opacity=0.9, radius=markerSize(x.ELEV), fill=True, fill_color=markerColor(x.ELEV)))
data.apply(placeMarker, 1)

map.add_child(fg)
map.add_child(folium.LayerControl())
map.fit_bounds(map.get_bounds())

map.save("Volcanoes-map.html")