import requests
import json
import SortAPI
from get_user_input import get_location, get_activity, get_distance


APIKEY = 'Bearer rlDWY6ro4dO-te4yEdDxzDmOG5Zx0pr8jtWYbvbMvF11brloUF0oeOzaoCo1I_9nZIU72r4QqeHcvqU-SrxNTFDP56g6WhiRcDrQsKADdDJ-PEio2YlLiOxpoiVEZHYx'


def get_data_from_API(location, activity, distance):
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={activity}&radius={distance}&sort_by=distance&limit={2}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": APIKEY
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    num_of_business = response.json()['businesses']
    print('-'*30)
    print('Here are some options: \n')
    for business in num_of_business:
        print(SortAPI.get_data_from_API(business))


def main() -> None:
    location = get_location()
    activity = get_activity()
    distance = get_distance()
    get_data_from_API(location, activity, int(distance)*1600)


if __name__ == '__main__':
    main()
