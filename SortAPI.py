import json

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

def get_data_from_API(business):
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
    


    
