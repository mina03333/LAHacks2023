import requests
import get_user_input

APIKEY = 'Bearer vIJp-pW2ISoT0G0LVHUpdwhRfESBy_W5Wl53c2kpoalMOEIATNBkxNK_9ZNmn1IOjo6fG9Kb6tHxoGZJGl61DgB5FfkvgOj8dKIPNIMxsqMMAPGoLGVbXCuzn_NDZHYx'


url = f"https://api.yelp.com/v3/businesses/search?location={location}&latitude={latitude}&longitude={longitude}&term={term}&radius={radius}&categories={cat1}&categories={cat2}&sort_by=distance&limit={limit}"

#API call
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": APIKEY
    # this will fail

}

response = requests.get(url, headers=headers)
print(response.text)