'''Write a simple terminal app that lists all the bus stops within a certain radius of a set
of GPS coordinates you supply. The user should be able to choose one bus stop which
then lists all the scheduled and estimated arrival times'''

#import the modules we need
from requests import get
import requests
from dateutil.parser import parse
from colorama import Fore


#fetch the data from the API 
# location longitude -97.15136753188683 and latitude 49.90157596507107
#set a certain radius of a set of GPS coordinates you supply
API_KEY = "dgu7jqpBulTaykJOPOif"
lon = -97.15136753188683
lat = 49.90157596507107
distance = 400

def get_nearby_stops():
    #try then except to catch the error
    try:
        resp_stops = requests.get(
            #GET https://api.winnipegtransit.com/v3/stops.json
            #params: api-key, lat, lon, distance
            url="https://api.winnipegtransit.com/v3/stops.json",
            params={
                "api-key": API_KEY,
                "lat": lat,
                "lon": lon,
                "distance": distance
            },
        )
        #check if the request is successful
        if resp_stops.status_code == 200:
            #convert the response to a python dictionary
            data = resp_stops.json()
            #print(data)
            print(f"Stops available within {distance} meters of {lat}, {lon}:")
            #return the list of stops
            return data
        else:
            #return an empty list
            return []
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        
    

#request the stops' schedule by stop number
def get_stop_info(stop_number):
    #try then except to catch the error
    try:
        resp_stop_info = requests.get(
            #GET https://api.winnipegtransit.com/v3/stops/{stop number}/schedule.json
            #params: api-key
            url=f"https://api.winnipegtransit.com/v3/stops/{stop_number}/schedule.json",
            params={
                "api-key": API_KEY,
            },
        )
        #check if the request is successful
        if resp_stop_info.status_code == 200:
            #convert the response to a python dictionary
            data = resp_stop_info.json()
            #return the stop info
            return data
        else:
            #return an empty list
            return []
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        
        
#display the stop info as user's choice
def show_schedule_details(available_stops):
    #print(available_stops)
    print('Enter stop number:')
    #get stop number from user
    stop_number = input()
    
    #check if stop number is integer
    if stop_number.isdigit() and int(stop_number) in available_stops:
        #get stop info
        stop_info = get_stop_info(stop_number)
        #if stop info is not None
        if stop_info is not None:
            #print stop info
            print(f"Stop number: {stop_info['stop-schedule']['stop']['name']}")
            print(f"Cross street: {stop_info['stop-schedule']['stop']['cross-street']['name']}")
            print(f"Routes:")
            for route in stop_info['stop-schedule']['route-schedules']:
                print(f"    {route['route']['number']} - {route['route']['name']}")
                
                #Bonus: Arrival times: (green=on_time, red=late, blue=early):
                print(f" {Fore.RESET}Arrival times: ({Fore.GREEN}green=on_time, {Fore.RED}red=late, {Fore.BLUE}blue=early)")
                #loop through the scheduled-time and estimated-time
                for scheduled_stop in route['scheduled-stops']:
                    #convert the time to a datetime object
                    arrival_time = parse(scheduled_stop['times']['arrival']['scheduled'])
                    #convert the time to a datetime object
                    estimated_time = parse(scheduled_stop['times']['arrival']['estimated'])
                    #check if the estimated time is earlier than the scheduled time
                    if estimated_time < arrival_time:
                        #print the estimated time in blue
                        print(f"    {Fore.BLUE}scheduled: {arrival_time.strftime('%H:%M:%S')}   estimated: {estimated_time.strftime('%H:%M:%S')}{Fore.RESET}")
                    #check if the estimated time is later than the scheduled time
                    elif estimated_time > arrival_time:
                        #print the estimated time in red
                        print(f"    {Fore.RED}scheduled: {arrival_time.strftime('%H:%M:%S')}   estimated: {estimated_time.strftime('%H:%M:%S')}{Fore.RESET}")
                    else:
                        #print the estimated time in green
                        print(f"    {Fore.GREEN}scheduled: {arrival_time.strftime('%H:%M:%S')}   estimated: {estimated_time.strftime('%H:%M:%S')}{Fore.RESET}")
        else:
            print(Fore.RED + "No stop info available"+Fore.RESET)
    else:
        print(f"{Fore.RED}[!] No stop info found for stop number: {stop_number}{Fore.RESET}")
        show_schedule_details(available_stops)
 
 
 
def main():
    #get the list of stops
    stops = get_nearby_stops()
    #print(stops)
    #create an empty list to store the available stops
    available_stops = []
    #if the stops list is not empty
    if stops:
        #loop through the stops
        for stop in stops['stops']:
            #append the stop number to the available stops list
            available_stops.append(stop["key"])
            #print(stop["key"]+"-"+stop["name"])
            print(f" {stop['key']} - {stop['name']}")
        #show the schedule details
        show_schedule_details(available_stops)         
    else:
        print(Fore.RED + "No stops available"+Fore.RESET)
        quit() #quit the program because there is no stop available,so there is no need to continue the program       
    
                      

#call the main function to run the program, if the program is not imported ,then run the program , otherwise don't run the program                     
if __name__ == "__main__":
    main()
    quit()
    
    
