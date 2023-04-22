function get_location():
    location = input("Enter your location: ")

function get_activity():
    is_activites_valid = False
    while !is_activities_valid:
        print("1. temp activity")
        print("2. temp activity")
        print("3. temp activity")
        print("4. temp activity")
        print("5. temp activity")
        activities = input("Select which activity you want to do: ")

        if type(input) != int:
            print("Please enter a number, not anything else.")
        elif input > 5 or input < 1:
            print("Please enter a valid number.")
        else:
            is_activities_valid = True;
            break

function get_distance():
    while True:
        distance = input("Enter distance in miles: ")
        if distance > 30:
            pass
        else:
            break