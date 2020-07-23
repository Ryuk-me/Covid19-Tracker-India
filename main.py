import requests
import json
from termcolor import colored
from banner import banner


def covid19india():

    api = "https://api.covid19india.org/data.json"
    res = requests.get(api).json()

    summary = res['statewise'][0]

    total_cases = int(summary['confirmed'])
    total_recovered = int(summary['recovered'])
    total_deaths = int(summary['deaths'])
    total_active = int(summary['active'])

    regional_data = res['statewise']
    total_states = int(len(regional_data))

    for data in range(1, total_states):
        if regional_data[data]['state'] == "State Unassigned":
            continue
        else:
            print(
                f"{colored('* State ','yellow',attrs=['bold','reverse'])} : {colored(regional_data[data]['state'],'cyan',attrs=['bold','reverse'])}\n\n\
                        {colored('Confirmed Cases ','magenta',attrs=['reverse','bold'])} : {int(regional_data[data]['confirmed']):,}\n\
                        {colored('Active Cases ','blue',attrs=['bold','reverse'])} : {int(regional_data[data]['active']):,}\n\
                        {colored('Recovered ','green',attrs=['reverse','bold'])} : {int(regional_data[data]['recovered']):,}\n\
                        {colored('Deaths ','white','on_grey',attrs=['reverse','bold'])} : {int(regional_data[data]['deaths']):,}\n\
                        {colored('Last Updated ON ', 'yellow', 'on_grey', attrs=['reverse', 'bold'])}: {(regional_data[data]['lastupdatedtime'])}\n\n", end=" ")

    print(f"\n\n\t\t\t\t\n\
                \t\t\t\t\t{colored('Total Confirmed Cases ','red',attrs=['reverse','bold'])} : {total_cases:,}\n\
                \t\t\t\t\t{colored('Total Active Cases ','magenta',attrs=['reverse','bold'])} : {total_active:,}\n\
                \t\t\t\t\t{colored('Total Recovered ','green',attrs=['reverse','bold'])} : {total_recovered:,}\n\
                \t\t\t\t\t{colored('Total Deaths ','white','on_grey',attrs=['reverse','bold'])} : {total_deaths:,}\n\
                \t\t\t\t\t{colored('Last Updated ON ','yellow','on_grey',attrs=['reverse','bold'])} : {res['statewise'][0]['lastupdatedtime']}\n")


if __name__ == '__main__':
    banner()
    covid19india()
