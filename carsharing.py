import sys
from csv_reader import csv_read
from heur import Request, Zone
import numpy as np

def local_search():
    pass

def cost_function(not_reserveds, near_reserveds):
    for not_reserved in not_reserveds:
        cost_not_reserved += not_reserved.p1
    for near_reserved in near_reserveds:
        cost_near_reserved += near_reserved.p2
    return cost_not_reserved + cost_near_reserved

def main():
    input_file = sys.argv[1]
    requests, zones, vehicles, days = csv_read(input_file)
    not_reserveds = np.empty(len(requests)) #Reservatie ID
    vehicle_in_zones = np.empty((len(vehicles), len(zones))) #Vehicle ID, Zone ID
    request_vehicles = np.empty((len(requests), len(vehicles))) #Reservatie ID, Vehicle ID

if __name__== "__main__":
  main()
