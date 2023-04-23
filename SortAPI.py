import requests

APIKEY = 'Bearer rlDWY6ro4dO-te4yEdDxzDmOG5Zx0pr8jtWYbvbMvF11brloUF0oeOzaoCo1I_9nZIU72r4QqeHcvqU-SrxNTFDP56g6WhiRcDrQsKADdDJ-PEio2YlLiOxpoiVEZHYx'


def check_if_open(business):
    if business['is_closed']:
        return True
    else:
        return False


def check_if_address(business):
    if business['location']['address1'] == None or business['location']['address1'].strip() == '':
        return False
    else:
        return True

def price_to_range(business):
    price = business['price']
    if price == '$':
        return "less than $10"
    elif price == "$$":
        return "$11-$30"
    elif price == "$$$":
        return "$31-$60"
    elif price == "$$$$":
        return "more than $60"
    else: 
        return "There is no specified price range."

def sort_data(business):
    if check_if_open and check_if_address:
        name = business['name']
        address_location = business['location']['display_address']
        address = ' '.join(str(x) for x in address_location)
        services = ''
        len_categories = len(business['categories'])
        for categories in business['categories']:
            if len_categories == 1:
                services += categories['title']
            else:
                services += categories['title'] + ', '
            len_categories -= 1
        phone_num = business['display_phone'] if len(business['display_phone'].strip()) > 0 else 'N/A'
        return f'Name: {name}\nPrice Range: {price_to_range(business)}\nAddress: {address}\nServices: {services}\nPhone Number: {phone_num}\n'
    else:
        return None
    

def get_data_from_API(location, activity, distance):
    final_list = []
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={activity}&radius={distance}&sort_by=distance&limit={2}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": APIKEY
    }

    response = requests.get(url, headers=headers)
    #print(response.text)
    num_of_business = response.json()['businesses']
    # print('-'*30)
    # print('Here are some options: \n')
    for business in num_of_business:
        final_list.append(sort_data(business))

    return final_list
    
