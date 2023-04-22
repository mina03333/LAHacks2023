def get_location():
    location = input("Enter your location (Please do not use abbreviations): ")
    return location


def get_activity() -> str:
    is_activities_valid = False
    activities = None
    activity_list = ['restaurant', 'entertainment',
                     'outdoors', 'drinks', 'sports']
    while is_activities_valid == False:
        for i in range(len(activity_list)):
            print(f'{i+1}: {activity_list[i]}')

        activities = input("\nSelect which activity you want to do: ")
        is_int = False

        try:
            int(activities)
            is_int = True
        except ValueError:
            print("Please enter a number, not anything else.\n")

        if is_int and (int(activities) > 5 or int(activities) < 1):
            print("Please enter a valid number.\n")
        elif is_int:
            is_activities_valid = True

    activity_name = activity_list[int(activities) - 1]
    return activity_name


def get_distance():
    distance = None
    while True:
        distance = input("Enter distance in miles: ")
        is_int = False

        try:
            int(distance)
            is_int = True
        except ValueError:
            print("Please enter a number, not anything else.\n")

        if is_int and (int(distance) > 50 or int(distance) < 0):
            print("Please enter a valid number.\n")
        elif is_int:
            break

    return distance
