import csv
from heur import Request, Zone


def csv_read(csv_input):
    requests = []
    zones = []
    vehicles = []
    with open(csv_input, 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if row[0][0] == "+":
                csv_type = row[0].split("+")
                csv_type = csv_type[1].split(":")
                csv_class = csv_type[0]
                csv_number = int(csv_type[1])
                if csv_class == "Days":
                    days = csv_number
                    break
                continue
            else:
                if csv_class == "Requests":
                    vehicles = row[5].replace('car', '')
                    vehicles = vehicles.split(",")
                    vehicles = [int(vehicle) for vehicle in vehicles]
                    requests.append(Request(int(row[0].lstrip('req')), row[1], int(row[2]), int(row[3]), int(row[4]), vehicles, int(row[6]), int(row[7])))

                if csv_class == "Zones":
                    nears = row[1].replace('z', '')
                    nears = nears.split(",")
                    nears = [int(near) for near in nears]
                    zones.append(Zone(int(row[0].replace('z', '')), nears))

                if csv_class == "Vehicles":
                    vehicles.append(row[0])
    return requests, zones, vehicles, days
