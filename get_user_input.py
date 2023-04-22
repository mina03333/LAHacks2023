def get_location():
    location = input("Enter your location: ")
    return location


def get_activity() -> str:
    is_activities_valid = False
    activities = None
    activitiy_list = ['food', 'entertiment', 'outdoors', 'drinks', 'sports']
    while is_activities_valid == False:
        print("1. temp activity")
        print("2. temp activity")
        print("3. temp activity")
        print("4. temp activity")
        print("5. temp activity")
        activities = input("Select which activity you want to do: ")
        is_int = False

        try:
            int(activities)
            is_int = True
        except ValueError:
            print("Please enter a number, not anything else.")

        if is_int and (int(activities) > 5 or int(activities) < 1):
            print("Please enter a valid number.")
        elif is_int:
            is_activities_valid = True
    activity_name = activitiy_list[int(activities) -1]
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
            print("Please enter a number, not anything else.")

        if is_int and (int(distance) > 30 or int(distance) < 0):
            print("Please enter a valid number.")
        elif is_int:
            break

    return distance
