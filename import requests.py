import requests
APIKEY = 'Bearer vIJp-pW2ISoT0G0LVHUpdwhRfESBy_W5Wl53c2kpoalMOEIATNBkxNK_9ZNmn1IOjo6fG9Kb6tHxoGZJGl61DgB5FfkvgOj8dKIPNIMxsqMMAPGoLGVbXCuzn_NDZHYx'

priceLevel = input('number of $!')

url = f"https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20&location=LA&price={priceLevel}"

#zip_code = input('Enter the zip code :')


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": APIKEY

}

response = requests.get(url, headers=headers)
print(response.text)