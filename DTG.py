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


destinationlist = ["Milwaukee", "Las Vegeas", "Eugene"]

destination = destinationlist
destination1 = destinationlist.pop()
destination2 = destinationlist.pop(1)

transportationlist = ["Plane", "Train", "Bus"]

transportaion = transportationlist
transportaion1 = transportationlist.pop()
transportaion2 = transportationlist.pop(1)

restaurantlist = ["Steak House", "Sushi", "Taco Truck"]

restaurant = restaurantlist
restaurant2 = restaurantlist.pop()
restaurant3 = restaurantlist.pop(1)


entertainmentlist = ["Secret Rave", "College Football Game", "Bar Crawl"]

entertainment = entertainmentlist
entertainment2 = entertainmentlist.pop()
entertainment3 = entertainmentlist.pop(1)



day_trip_generator = "Thank you for selecting Day Trip Generator.  If you are looking for a randome and spontanious vacation, you have come to the right place!"


opening_destination_location = input(f'Would you like to go to {destination}?')

if opening_destination_location == 'Y':
    print('great! Lets move on to transportation.')
    

elif opening_destination_location == 'N':
    alternative_destinaition = input(f'No Problem, how does {destination1} sound?')
    if alternative_destinaition == 'Y':
        print('Great! Lets move on to transpertation')
    elif alternative_destinaition == 'N':
        alternative_destinaition3 = input(f'Okay, how about {destination2}?')
        if alternative_destinaition3 == 'Y':
            print('Awesome! lets work on transpertaion!')


opening_transportaion = input(f'Would you like to travel by {transportaion}?')

if opening_transportaion == 'Y':
    print('Great! Lets find a place for you to eat!')

elif opening_transportaion == 'N':
    alternative_transportation = input(f'would you rather {transportaion1}?')
    if alternative_transportation == 'Y':
        print('Fantastic! Now lets find some good food to eat!')
    elif alternative_transportation == 'N':
        alternative_transportation3 = input(f'so you would prefer to take a {transportaion2}?')
        if alternative_transportation3 == 'Y':
            print('Perfect, now lets eat! ')



opening_restaurant = input(f'Do you like {restaurant}?')

if opening_restaurant == 'Y':
    print('Awesome thats my favorit! Now for the entertainment!')

elif opening_restaurant == 'N':
    alternative_restaurant = input(f'Do you fancy {restaurant2}?')
    if alternative_restaurant == 'Y':
        print('Great! Now lets find something to do after!')

    elif alternative_restaurant == 'N':
        alternative_restaurant2 = input(f'should we get {restaurant3}?')
        if alternative_restaurant2 == 'Y':
            print('Sounds good to me! Time to find some entertainment!')

opening_entertainment = input(f' Wanna go to a {entertainment}?')

if opening_entertainment == 'Y':
    print(' This night is going to be awesome!')

elif opening_entertainment == 'N':
    alternate_entertainment = input(f' would you prefer a {entertainment2}?')
    if alternate_entertainment == 'Y':
        print('Thats what i really wanted to do also!')

    elif alternate_entertainment == 'N':
        alternate_entertainment2 = input(f'Okay, well how about we go to a {entertainment3}?')
        if alternate_entertainment2 == 'Y':
            print('Yes! Great Choice!')


confirmation = [opening_destination_location, opening_transportaion, opening_restaurant, opening_entertainment]

print(confirmation)