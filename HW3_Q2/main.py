from Bus import Bus
from Town import Town
from People import People
import random
import pickle

# generating towns for the company
temp_for_town = []
town1 = Town("One Town", 0)
town2 = Town("Two Town", 1)
town3 = Town("Three Town", 2, town1, town2)
town4 = Town("Four Town", 3, town3, town1)
town5 = Town("Five Town", 4, town1, town3)
town6 = Town("Six Town", 5, town2, town3)
town7 = Town("Seven Town", 6, town1, town5)
town8 = Town("Eight Town", 7, town6, town4)
town9 = Town("Nine Town", 8, town7, town5)
town10 = Town("Ten Town", 9, town9, town2)
town11 = Town("Eleven Town", 10, town10, town6)
town12 = Town("Twelve Town", 11, town11, town2)
town13 = Town("Thirteen Town", 12, town5, town10)
town14 = Town("Fourteen Town", 13, town11, town13)
town1.first_road_to = town12
town1.second_road_to = town14
town2.first_road_to = town10
town2.second_road_to = town13
temp_for_town.append(town1)
temp_for_town.append(town2)
temp_for_town.append(town3)
temp_for_town.append(town4)
temp_for_town.append(town5)
temp_for_town.append(town6)
temp_for_town.append(town7)
temp_for_town.append(town8)
temp_for_town.append(town9)
temp_for_town.append(town10)
temp_for_town.append(town11)
temp_for_town.append(town12)
temp_for_town.append(town13)
temp_for_town.append(town14)

# generating buses for the company
temp_for_bus = []
for i in range(10, 23):
    bus = Bus(random.randint(40, 60), None, None, i)
    randomCheck = random.randint(0, 2)
    if randomCheck is 0:
        bus.status = "atStart"
    elif randomCheck is 1:
        bus.status = "inRoute"
    elif randomCheck is 2:
        bus.status = "atEnd"
    temp_for_bus.append(bus)
for bus in temp_for_bus:
    print("Bus route NO." + str(bus.route) + " Max load is " + str(bus.max_load) + " people.")

# generating people to ride the buses
temp_for_people = []
for i in range(1, 500):
    person = People("person" + str(i), random.randint(1, 100))
    temp_for_people.append(person)

# putting people on buses randomly
for i in range(0, len(temp_for_people)):
    temp_for_bus[random.randint(0, 12)].people_on.append(temp_for_people[i])

# setting departure and arrival towns for each bus
for i in range(0, len(temp_for_bus)):
    temp_for_bus[i].departure_town = temp_for_town[random.randint(0, 13)]
    randomcheck = random.randint(0, 1)
    if randomcheck == 0:
        temp_for_bus[i].arrival_town = temp_for_bus[i].departure_town.first_road_to
    elif randomcheck == 1:
        temp_for_bus[i].arrival_town = temp_for_bus[i].departure_town.second_road_to
    # setting positions of each bus
    if temp_for_bus[i].status is "atStart":
        temp_for_town[temp_for_bus[i].departure_town.index].bus_here.append(temp_for_bus[i].route)
    elif temp_for_bus[i].status is "atEnd":
        temp_for_town[temp_for_bus[i].arrival_town.index].bus_here.append(temp_for_bus[i].route)

# prompting if boss wants to resume from last time
load_or_not = input("Do you want to load data from last time? y for YES and n for NO: ")
if load_or_not == "y":
    save_status = pickle.load(open("save.txt", "rb"))
    temp_for_bus = save_status[0]
    temp_for_people = save_status[1]
    temp_for_town = save_status[2]
else:
    print("statring program with new data...")

# generating menu for the boss to use the program
print("What would you like to do today, my boss?")
print("[1]see where a bus is")
print("[2]see which buses are in a town")
print("[3]see how many people are on a bus")
print("[4]see which roads goes out of a town")
print("This is only a beta program. Be careful of what you enter! Or program will crash!")
user_choice = input("choose now\n")

# case where boss wants to know the position of a bus
if user_choice == "1":
    bus_number = int(input("give me the route number from 10 to 22: "))
    if temp_for_bus[bus_number - 10].status == "atStart":
        print("Bus NO." + str(bus_number) + " is " + "at " + temp_for_bus[bus_number - 10].departure_town.name)
    elif temp_for_bus[bus_number - 10].status == "atEnd":
        print("Bus NO." + str(bus_number) + " is " + "at " + temp_for_bus[bus_number - 10].arrival_town.name)
    elif temp_for_bus[bus_number - 10].status == "inRoute":
        print("Bus NO." + str(bus_number) + " is " + "travelling from " + temp_for_bus[bus_number - 10].departure_town.name + " to " + temp_for_bus[bus_number - 10].arrival_town.name)
    # codes to save status to a file
    save_or_not = input("\nDo you want to save status for next time? y for YES and n for NO: ")
    if save_or_not == "y":
        save_status = [temp_for_bus, temp_for_people, temp_for_town]
        pickle.dump(save_status, open("save.txt", "wb"))
    else:
        x = input("type anything to exit")
# case where boss wants to see buses at a town
elif user_choice == "2":
    town_number = int(input("give me a town number from 1 to 14: "))
    print("Buses NO." + str(temp_for_town[town_number - 1].bus_here) + " are at " + temp_for_town[town_number - 1].name)
    # codes to save status to a file
    save_or_not = input("\nDo you want to save status for next time? y for YES and n for NO: ")
    if save_or_not == "y":
        save_status = [temp_for_bus, temp_for_people, temp_for_town]
        pickle.dump(save_status, open("save.txt", "wb"))
    else:
        x = input("type anything to exit")
# case where boss wants to see the people on a bus
elif user_choice == "3":
    bus_number = int(input("give me the route number from 10 to 22: "))
    print("These are the people on this bus now: ")
    for item in temp_for_bus[bus_number - 10].people_on:
        print("    " + item.name)
    print(str(len(temp_for_bus[bus_number - 10].people_on)) + " people on this bus.")
    # codes to save status to a file
    save_or_not = input("\nDo you want to save status for next time? y for YES and n for NO: ")
    if save_or_not == "y":
        save_status = [temp_for_bus, temp_for_people, temp_for_town]
        pickle.dump(save_status, open("save.txt", "wb"))
    else:
        x = input("type anything to exit")
# case where boss wants to see the roads out of a town
elif user_choice == "4":
    town_number = int(input("give me a town number from 1 to 14: "))
    print("This town has two road heading out.\n    First is towards " + temp_for_town[town_number - 1].first_road_to.name)
    print("    Second is towards " + temp_for_town[town_number - 1].second_road_to.name)
    # codes to save status to a file
    save_or_not = input("\nDo you want to save status for next time? y for YES and n for NO: ")
    if save_or_not == "y":
        save_status = [temp_for_bus, temp_for_people, temp_for_town]
        pickle.dump(save_status, open("save.txt", "wb"))
    else:
        x = input("type anything to exit")