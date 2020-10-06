# location-history-fencing

This script calculates the time spent around a specific location from your Google Timeline data.

## Requirements
Python3, GeoPy and tqdm installed on your system
## Usage
### Parameters:
1. path to the downloaded Google Timeline data json file
2. latitude of the desired location
3. longitude of the desired location
4. the maximum distance for the point from the location to be taken into account (in meters)
5. the minimum duration for the visit to be added to the summary (in minutes) 
### Example:
`python3 location-history-fencing.py location-history.json 47.252816 18.355761 250 30`
