import SortAPI
from get_user_input import get_location, get_activity, get_distance
from itinerary_recommendations import itinerary

def main() -> None:
    quit = False
    while not quit:
        location = get_location()
        activities = get_activity()
        distance = get_distance()
        final_list = []
        for i in activities:
            final_list.append(SortAPI.get_data_from_API(location, i, int(distance)*1600))

        stringify = ''
        for i in final_list:
            for j in i:
                stringify += j + '\n'

        schedule = itinerary(stringify)
        print(schedule)
        quit_input = input("If you are happy with your result, enter 'q' to exit: ")
        if quit_input.lower().strip() == 'q':
            quit = True



if __name__ == '__main__':
    main()
