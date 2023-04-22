import requests
from get_user_input import get_location, get_activity, get_distance


APIKEY = 'Bearer vIJp-pW2ISoT0G0LVHUpdwhRfESBy_W5Wl53c2kpoalMOEIATNBkxNK_9ZNmn1IOjo6fG9Kb6tHxoGZJGl61DgB5FfkvgOj8dKIPNIMxsqMMAPGoLGVbXCuzn_NDZHYx'


def get_data_from_API(location, activity, distance):
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={activity}&radius={distance}&sort_by=distance&limit={20}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": APIKEY
    }

    response = requests.get(url, headers=headers)
    print(response.text)


def main() -> None:
    location = get_location()
    activity = get_activity()
    distance = get_distance()
    get_data_from_API(location, activity, distance)


if __name__ == '__main__':
    main()
