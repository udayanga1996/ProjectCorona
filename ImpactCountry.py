import requests
import json

def impact (TotalImpactCountry):
    para = {'Impacted Count': TotalImpactCountry}
    response = requests.get("https://api.thevirustracker.com/free-api?global=stats", params=para)
    print(response.status_code)

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    jprint(response.json())

impact(TotalImpactCountry="US")
