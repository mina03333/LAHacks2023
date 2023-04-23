def get_location():
    location = input("Enter your location(city, or specific address): ")
    return location


def get_activity() -> str:
    is_activities_valid = False
    activities = None
    activity_list = ['restaurant', 'entertainment',
                     'outdoors', 'drinks', 'sports']
    while is_activities_valid == False:
        for i in range(len(activity_list)):
            print(f'{i+1}: {activity_list[i]}')

        activities = input("\nSelect which activity you want to do (If you would like to make multiple choices, please seperate each choice by a space): ")
        activities = activities.split()

        is_int = False

        try:
            for i in activities:
                int(i)
            is_int = True
        except ValueError:
            print("Please enter a number, not anything else.\n")

        if is_int:
            for i in activities:
                if (int(i) > 5 or int(i) < 1):
                    print("Please enter a valid number.\n")
                    break
            is_activities_valid = True

    activity_name = []
    for i in activities:
        activity_name.append(activity_list[int(i) - 1])

    return activity_name


def get_distance():
    distance = None
    while True:
        distance = input("Enter distance in miles(max is 25): ")
        is_int = False

        try:
            int(distance)
            is_int = True
        except ValueError:
            print("Please enter a number, not anything else.\n")

        if is_int and (int(distance) > 25 or int(distance) < 0):
            print("Please enter a valid number.\n")
        elif is_int:
            break

    return distance
