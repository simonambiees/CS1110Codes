from Bus import Bus
from Town import Town
from People import People
import random

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

temp_for_people = []
for i in range(1, 500):
    person = People("person" + str(i), random.randint(1, 100))
    temp_for_people.append(person)

for i in range(0, len(temp_for_people)):
    temp_for_bus[random.randint(0, 12)].people_on.append(temp_for_people[i])

for i in range(0, len(temp_for_bus)):
    temp_for_bus[i].departure_town = temp_for_town[random.randint(0, 13)]
    randomcheck = random.randint(0, 1)
    if randomcheck == 0:
        temp_for_bus[i].arrival_town = temp_for_bus[i].departure_town.first_road_to
    elif randomcheck == 1:
        temp_for_bus[i].arrival_town = temp_for_bus[i].departure_town.second_road_to

    if temp_for_bus[i].status is "atStart":
        temp_for_town[temp_for_bus[i].departure_town.index].bus_here = temp_for_bus[i].route
    elif temp_for_bus[i].status is "atEnd":
        temp_for_town[temp_for_bus[i].arrival_town.index].bus_here = temp_for_bus[i].route

print("What would you like to do today, my boss?")
print("[1]see where a bus is")
print("[2]see which buses are in a town")
print("[3]see how many people are on a bus")
print("[4]see which roads goes out of a town")
user_choice = input("choose now\n")
if user_choice == "1":
    bus_number = int(input("give me the route number: "))
    if temp_for_bus[bus_number - 10].status == "atStart":
        print("Bus NO." + str(bus_number) + " is " + "at " + temp_for_bus[bus_number - 10].departure_town.name)
    elif temp_for_bus[bus_number - 10].status == "atEnd":
        print("Bus NO." + str(bus_number) + " is " + "at " + temp_for_bus[bus_number - 10].arrival_town.name)
    elif temp_for_bus[bus_number - 10].status == "inRoute":
        print("Bus NO." + str(bus_number) + " is " + "travelling from " + temp_for_bus[bus_number - 10].departure_town.name + " to " + temp_for_bus[bus_number - 10].arrival_town.name)