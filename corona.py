import json

import requests
import _json


def get_data(msg_text):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "1051a04ab3msh58010353202dd07p19b60fjsnd3ca01e107c0"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.text
    data = json.loads(data)
    for i in range(len(data['response'])):
        x = data['response'][i]['country']
        if x.lower() == msg_text.lower():
            active = data['response'][i]['active']
            recovered = data['response'][i]['recovered']
            new_cases = data['response'][i]['new']
            critical = data['response'][i]['critical']
            total = data['response'][i]['total']
            total_deaths = data['response'][i]['deaths']['total']
            new_deaths = data['response'][i]['deaths']['new']
            data_complete = """"total_infected: """ + str(total) + """"
                              active_cases: """ + str(active) + """"
                              recovered: """ + str(recovered) + """"
                              critical_cases: """ + str(critical) + """"
                              new_cases: """ + str(new_cases) + """"
                              total_deaths: """ + str(total_deaths) + """"
                              new_deaths: """ + str(new_deaths)
            return data_complete
            break
    return "Country entered not found"
