import json

def get_data_from_API(business):
    name = business['name']
    address_location = business['location']['display_address']
    address = f'{address_location[0]}, {address_location[1]}'
    services = ''
    len_categories = len(business['categories'])
    for categories in business['categories']:
        if len_categories == 1:
            services += categories['title']
        else:
            services += categories['title'] + ', '
        len_categories -= 1
    phone_num = business['display_phone']

    return f'Name: {name}\nAddress: {address}\nServices: {services}\nPhone Number: {phone_num}\nby'