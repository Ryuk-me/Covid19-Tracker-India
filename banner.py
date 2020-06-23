from termcolor import colored


def banner():
    banner = f"""

            _____           _     _   _______             _               _____           _ _
           / ____|         (_)   | | |__   __|           | |             |_   _|         | (_)
          | |     _____   ___  __| |    | |_ __ __ _  ___| | _____ _ __    | |  _ __   __| |_  __ _
          | |    / _ \ \ / / |/ _` |    | | '__/ _` |/ __| |/ / _ \ '__|   | | | '_ \ / _` | |/ _` |
          | |___| (_) \ V /| | (_| |    | | | | (_| | (__|   <  __/ |     _| |_| | | | (_| | | (_| |
           \_____\___/ \_/ |_|\__,_|    |_|_|  \__,_|\___|_|\_\___|_|    |_____|_| |_|\__,_|_|\__,_|

                                                            Author : {colored('Neeraj Kumar (Ryuk-me)','green')}
                                                            Github : {colored('https://github.com/Ryuk-me','green')}


    """
    banner = colored(banner, 'blue', attrs=['bold'])
    print(banner)
