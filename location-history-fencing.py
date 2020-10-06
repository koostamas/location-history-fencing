# This script calculates the time spent around a specific location from your Google Timeline data.
# Requirements: Python3, GeoPy and tqdm installed on your system
# Parameters:
#	1: path to the downloaded Google Timeline data json file
#	2: latitude of the desired location
#	3: longitude of the desired location
#	4: the maximum distance for the point from the location to be taken into account (in meters)
#	5: the minimum duration for the visit to be added to the summary (in minutes) 
# Example:  python3 location-history-fencing.py location-history.json 47.252816 18.355761 250 30

import sys
import json
from tqdm import tqdm
from geopy import distance
from datetime import datetime

filepath = sys.argv[1]
coords = (float(sys.argv[2]), float(sys.argv[3]))
radius = (float(sys.argv[4]) / 1000)
minLength = (float(sys.argv[5]) / 60)

print('Reading from file...')
with open(filepath, encoding='utf-8') as file:
	data = json.load(file)
	startAndEnds = []
	previousDay = '1970-01-01', datetime.now()
	print('Calculating points:')
	for location in tqdm(data['locations']):
		latString = str(location['latitudeE7'])
		lonString = str(location['longitudeE7'])
		lat = float(latString[0:2] + '.' + latString[2:])
		lon = float(lonString[0:2] + '.' + lonString[2:])
		currCoords = (lat, lon)
		if distance.distance(coords, currCoords).km <= radius:
			timestampMs = location['timestampMs']
			parsedDatetime = datetime.fromtimestamp(int(timestampMs[0:-3]))
			parsedDate = str(parsedDatetime)[0:10]
			currentDay = parsedDate, parsedDatetime
			if previousDay[0] != parsedDate:
				startAndEnds.append(previousDay)
				startAndEnds.append(currentDay)
			previousDay = currentDay
	startAndEnds.append(currentDay)
	print('Result:')
	sum = 0
	for i in range(1, len(startAndEnds), 2):
		start = startAndEnds[i][1]
		end = startAndEnds[i + 1][1]
		hours = (end - start).total_seconds() / 60 / 60
		if hours >= minLength:
			sum += hours
			print('    ' + startAndEnds[i][0] + ': ' + str(round(hours, 2)) + ' hour(s)')
		else:
			print('    ' + startAndEnds[i][0] + ': ' + str(round(hours, 2)) + ' hour(s) (ignored)')
	print('Sum: ' + str(round(sum, 2)))















