# tee ratkaisu tänne
# Write your solution here

import math

def get_station_data(filename: str):
    stations = {}
    with open(filename) as f:
        for line in f:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0] ) * 55.26
    y_km = (stations[station1][1] - stations[station2][1] ) * 111.2
   
    return math.sqrt(x_km**2 + y_km**2)


def greatest_distance(stations: dict):
    greatest = [str,str, 0]

    for name in stations:
        for namex in stations:
            if distance(stations, name, namex) > greatest[2]:
                greatest[0] = name
                greatest[1] = namex
                greatest[2] = distance(stations, name, namex)

    return (greatest[0], greatest[1], greatest[2])














# def main():
#     stations = get_station_data('stations1.csv')
#     station1, station2, greatest = greatest_distance(stations)
#     print(station1, station2, greatest)

# main()