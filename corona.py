import json

import requests


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
            active = data['response'][i]['cases']['active']
            recovered = data['response'][i]['cases']['recovered']
            new_cases = data['response'][i]['cases']['new']
            critical = data['response'][i]['cases']['critical']
            total = data['response'][i]['cases']['total']
            total_deaths = data['response'][i]['deaths']['total']
            new_deaths = data['response'][i]['deaths']['new']
            data_complete = x + "\n" + "Total Infected: " + str(total) + "\n" + "Active Cases: " + str(
                active) + "\n" + "Total Recovered: " + str(recovered) + "\n" + "Critical Cases" + str(
                critical) + "\n" + "New Cases: " + str(total) + "\n" + "Total Deaths: " + str(
                total_deaths) + "\n" + "New Deaths: " + str(total)

            return data_complete
            break
    return "Country entered not found"
