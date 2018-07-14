import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
	if elevation < 1000:
		return "green"
	elif elevation < 3000:
		return "orange"
	else:
		return "red"

def pop_color(x):
	pop = x["properties"]["POP2005"]

	if pop < 1000000:
		return {"fillColor" : "green"}
	elif pop < 20000000:
		return {"fillColor" : "orange"}
	else:
		return {"fillColor" : "red"}

geomap = folium.Map(location=(38.58, -99.0), zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for nm, lt, ln, el in zip(name, lat, lon, elev):
	fgv.add_child(folium.CircleMarker(
		location=(lt, ln),
		radius=6,
		color="grey",
		fill=True,
		fill_color=color_producer(el),
		fill_opacity=0.7,
		popup=folium.Popup("Name = " + nm + "\n" + " Elevation = " + str(el) + " m", parse_html=True)))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
	data=open("world.json", "r", encoding = "utf-8-sig").read(),
	style_function=pop_color))

geomap.add_child(fgp)
geomap.add_child(fgv)
geomap.add_child(folium.LayerControl())

geomap.save("map.html")
