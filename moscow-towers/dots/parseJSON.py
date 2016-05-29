#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

json_file = "bs.json"

json_data = open(json_file)
base_stations = json.load(json_data)

json_data.close()

#print(len(base_stations))
print("var bs = [")
for station in base_stations:
    print("['", station['Cells']['AdmArea'], station['Cells']['District'], "',", station['Cells']['geoData']['coordinates'][0], ',', station['Cells']['geoData']['coordinates'][1], "],")
print("];")