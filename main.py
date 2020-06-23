import requests
import json
from termcolor import colored
from banner import banner


def covid19india():

    api = "https://api.rootnet.in/covid19-in/stats/latest"
    res = requests.get(api).json()

    summary = res['data']['unofficial-summary'][0]

    total_cases = summary['total']
    total_recovered = summary['recovered']
    total_deaths = summary['deaths']
    total_active = summary['active']

    regional_data = res['data']['regional']
    total_states = int(len(regional_data))

    for data in range(total_states):
        print(
            f"{colored('* State ','yellow',attrs=['bold','reverse'])} : {colored(regional_data[data]['loc'],'cyan',attrs=['bold','reverse'])}\n\n\
                    {colored('Active Indian Cases ','blue',attrs=['bold','reverse'])} : {regional_data[data]['confirmedCasesIndian']}\n\
                    {colored('Active Foreign Cases ','blue',attrs=['bold','reverse'])} : {regional_data[data]['confirmedCasesForeign']}\n\
                    {colored('Total ','magenta',attrs=['reverse','bold'])} : {regional_data[data]['totalConfirmed']}\n\
                    {colored('Recovered ','green',attrs=['reverse','bold'])} : {regional_data[data]['discharged']}\n\
                    {colored('Deaths ','white','on_grey',attrs=['reverse','bold'])} : {regional_data[data]['deaths']}\n\n", end=" ")

    stats = f"\n\n\t\t\t\t\n\
    \t\t\t\t\t{colored('Total Confirmed Cases ','red',attrs=['reverse','bold'])} : {total_cases:,}\n\
    \t\t\t\t\t{colored('Total Active Cases ','magenta',attrs=['reverse','bold'])} : {total_active:,}\n\
    \t\t\t\t\t{colored('Total Recovered ','green',attrs=['reverse','bold'])} : {total_recovered:,}\n\
    \t\t\t\t\t{colored('Total Deaths ','white','on_grey',attrs=['reverse','bold'])} : {total_deaths:,}\n"

    print(stats)


if __name__ == '__main__':
    banner()
    covid19india()
