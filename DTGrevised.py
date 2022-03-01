# Day trip generator




#(5 points): As a developer, I want to make at least three commits with descriptive messages. 
#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
#(10 points): As a user, I want to display my completed trip in the console. 
#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


import random


def get_random_element(list):
    return random.choice(list)


destination_list = ["Milwaukee", "Las Vegeas", "Eugene"]
transportation_list = ["Plane", "Train", "Bus"]
restaurant_list = ["Steak House", "Sushi", "Taco Truck"]
entertainment_list = ["Secret Rave", "College Football Game", "Bar Crawl"]

random_destination = get_random_element(destination_list)
ramdom_transportaion = get_random_element(transportation_list)
random_restaurant = get_random_element(restaurant_list)
random_entertainment = get_random_element(entertainment_list)


not_satisfied = True 
   

    
while not_satisfied == True:
    print(f"Curent Location is {random_destination} is this okay?")
    user_input = input("Enter Yes or No")
    if user_input == "Yes":
            print("Great lets move on!")
            not_satisfied = False
    else:
        random_destination = get_random_element(destination_list)


while not_satisfied == True:
    print(f"current mode of transportation is {ramdom_transportaion}")
    user_input = input("Is this okay? Select Yes or No")
    if user_input == "Yes":
        print("Great lets move on")
        not_satisfied = False
    else:
        ramdom_transportaion = get_random_element(transportation_list)


def display_restaurant(restaurant):
    print(f"would you like to enjoy {restaurant}")

def reselect_trip_restaurant():
    global random_restaurant

    user_input = input("Is this okay? Select Yes or No\n")
    if user_input == "No":
        random_restaurant = get_random_element(restaurant_list)

    else:
        reselect_trip_restaurant()


def display_entertainment(entertainment):
    print(f"How does {entertainment} sound?")

def reselect_trip_entertainment():
    global random_entertainment

    user_input = input("Is this okay? Select Yes or No\n")
    if user_input == "No":
        random_entertainment = get_random_element(entertainment_list)

    else:
        reselect_trip_entertainment()



