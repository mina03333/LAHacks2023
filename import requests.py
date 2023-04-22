import requests
APIKEY = 'Bearer vIJp-pW2ISoT0G0LVHUpdwhRfESBy_W5Wl53c2kpoalMOEIATNBkxNK_9ZNmn1IOjo6fG9Kb6tHxoGZJGl61DgB5FfkvgOj8dKIPNIMxsqMMAPGoLGVbXCuzn_NDZHYx'

priceLevel = input('number of $!').strip()
search_words = input("Enter any acitivity that you want to do:\n").strip().replace(" ", "_")

url = f"https://api.yelp.com/v3/businesses/search?attributes={search_words}sort_by=best_match&limit=20&location=LA&price={priceLevel}"

#zip_code = input('Enter the zip code :')


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": APIKEY
    #"postal_code":zip_code
}

response = requests.get(url, headers=headers)
print(response.text)