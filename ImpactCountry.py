from Enter_Country import enter_country

import requests
import json

def impact (countryTotal):
    para = {'countryTotal': countryTotal}
    response = requests.get("https://api.thevirustracker.com/free-api", params=para)
    print(response.status_code)

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    country_data = response.json()['countrydata']
    jprint(country_data)

impact(countryTotal=enter_country())


