import random
import time
import webbrowser
import os
import threading
import sys
import json





#final version of game to do list:



#To do now:
#find bugs today, if none then you're done!!!
shop_open = False
Lshop_open = False
airportloop = False

rod = [] #creates rod inventory
baitbag = [] #creates bait inventory
weathercount = 0
baitamount = 32
wallet = [] #creates wallet
currentlocation = "english lake"
fishdex = []



    
















print ("""                          
 

                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~           
                    ~ _____  _       _      _                                               ~
                    ~|  ___|(_) ___ | |__  (_) _ __    __ _    __ _   __ _  _ __ ___    ___ ~
                    ~| |_   | |/ __|| '_ \ | || '_ \  / _` |  / _` | / _` || '_ ` _ \  / _ \~
                    ~|  _|  | |\__ \| | | || || | | || (_| | | (_| || (_| || | | | | ||  __/~
                    ~|_|    |_||___/|_| |_||_||_| |_| \__, |  \__, | \__,_||_| |_| |_| \___|~
                    ~                                 |___/   |___/                         ~
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                                        
                                        
                                                      .+-.                 
                                                   ..-      =..             
                                                  .=.        .              
                                                 .-          .              
                                                .-           .              
                                                -.           ..             
                                               =-          .=:=#=           
                                              .-          .++===++.         
                                              --          **+++++*+.        
                                              --=:..     .*#*******=-.      
                                             -@+%%%%.   .**#******+===      
                                           .+-=%%**%%   **-+*****===.       
                                           =++@=#%%%.      +=***=-.         
                                          .++. ....          .*+            
                                          +++              =+****=          
                                          ...             ....:-... 

""")
print ("                                                Version 5")
print ("                                            By totallybananas7")
print ("                                            Please do not copy.")
#dialogue


print("")
print("")
print("")










def cutscene0():
    global name

    print ("")

    print ("*As the sun rises over the town, you get woken up by the serene noise of waves lapping against earth.")
    time.sleep(5) 
    print ("Sea gulls cry overhead, as the air is filled with a familiar scent.")
    time.sleep(4)
    print ("Amidst the chaos of the early morning rush, you prepare for another COMPLETELY NORMAL day of angling.")
    time.sleep(5)
    print ("...")
    time.sleep(3)
    print ("......")
    time.sleep(3)
    print ("*heavy breathing*")
    time.sleep(3)

    print ("You hear a voice to your left...")
    time.sleep(3)
    print ("???: Hello there young fella!")
    time.sleep(2)
    print ("???: I'm Cap'n Corkah, and what might be your name?")

    name = str(input()) #gives player a name


    print ("Cap'n Corkah: Ah!",name,"! What a fine name you have!")
    time.sleep(3)
    print ("Cap'n Corkah: My dad was a fisherman you know, but he stopped, BECAUSE HIS NET INCOME WAS NOT ENOUGH AHAHAHA *slaps knee*")#hA IS A CUNR ~ Olly quote
    time.sleep(7)
    print ("Cap'n Corkah: Ok, Ok. We need to talk seriously now.")
    time.sleep(6)
    print ("Cap'n Corkah: You may know about these wars... The Great Fishing War.")
    time.sleep(6)
    print ("Cap'n Corkah: Multiple factions have been at war over territories that are best for catching fish.")
    time.sleep(7)
    print ("Cap'n Corkah: The council has deemed you,",name,", fit enough to go into different territories and catch all the fish so we can study them.")
    time.sleep(8)
    print ("Cap'n Corkah: To start you off, I'm going to equip you with what every new cooperate needs to start his adventure into the great unknown.")
    time.sleep(8)
    print ("Cap'n Corkah: FISHING GEAR!")
    time.sleep(3)
    print ("*You take a rather antique looking fishing rod and some bait out of a rusty fridge.*")
    time.sleep(5)


    rod.append("starter fishing rod")
    baitbag.append("basic bait")
    wallet.append ("English Lake")

    print ("Cap'n Corkah: Now we've done that, you can head off now.")
    print("")
    time.sleep(3)
    print ("Cap'n Corkah: Before you ask, we are in England.")
    time.sleep(3)

    print ("")

    print("")
    time.sleep(3)





    print ("Cap'n Corkah: If you ever get stuck, these 'ere are the controls!")
    time.sleep(2)
    print("")
    print ("Cap'n Corkah: If you wanna see these again, just say the word \"controls\"!")
    time.sleep(2)

    print ("To enter the shop, say: \"shop\"")
    print ("To gamble, say: \"gamble\"")
    print ("")

    print ("To travel to a new area, say: \"travel\"")
    print ("To ask where you are, say: \"current location\"")
    print ("To ask what the current weather is, say: \"current weather\"")
    print ("To change the weather, say \"change weather\"")
    print ("To change your name, say \"change name\"")
    print ("")

    print ("To cast your fishing rod, say: \"cast\"")
    print ("To reel in your fishing rod, say: \"reel\"")
    print ("")

    print ("To check your luck, say: \"luck\"")
    print ("To check your wallet, say: \"wallet\"")
    print ("To check your fishdex, say: \"fishdex\"")
    print ("To look at all the fish in the game, say: \"fishlist\"")
    print ("")

    print ("To see the credits, say: \"credits\"")
    print ("To get to the main menu, say: \"menu\"")


    print("")
    print("")

    time.sleep(0)
    print("Cap'n Corkah: Now go!")

def cutsceneskip():
    global name
    try:
        print("Would you like to skip the first cutscene?")
        skipcutscene = input().lower()

        if skipcutscene in ["yes", "y"]:
            print("What is your name?")
            name = str(input())  # gives player a name
            print("Your name is now:", name)
            print("If you want to load a previous save, say the word 'menu'")
            rod.append("starter fishing rod")
            baitbag.append("basic bait")
            wallet.append("English Lake")

        elif skipcutscene in ["no", "n"]:
            cutscene0()
        else:
            print("Invalid input. Try again.")
            cutsceneskip()
    except KeyboardInterrupt:
        print("Don't exit my game you wanker.")
        cutsceneskip()

cutsceneskip()












luck = 2

money = 0


Weather_Outcomes = ("raining", "snowing", "sunny", "overcast", "windy", "stormy", "foggy", "hailing")
current_weather = random.choice(Weather_Outcomes)       
if current_weather == "raining":
    luck = luck+10
if current_weather == "stormy":
    luck = luck+5
if current_weather == "snowing":
    luck = luck+1
print ("The weather is currently:",current_weather)
print ("You have 0 money.")


def weatherchange():
    global weathercount
    global luck
    if weathercount == 30:
        Weather_Outcomes = ("raining", "snowing", "sunny", "overcast", "windy", "stormy", "foggy", "hailing")
        current_weather = random.choice(Weather_Outcomes)
                
        if current_weather == "raining":
            luck = luck+10
        if current_weather == "stormy":
            luck = luck+7
        if current_weather == "snowing":
            luck = luck+1
        print ("The weather is currently:",current_weather)
        weathercount = 0

    else:
        pass



# Define a function for shopping

# Define items in the shop and locations as dictionaries
shop_items = [
    {"name": "Hobbyist fishing rod", "price": 100, "type": "rod", "luck": 3},
    {"name": "Commercial fishing rod", "price": 300, "type": "rod", "luck": 8},
    {"name": "Old Kosmo fishing rod", "price": 500, "type": "rod", "luck": 15},
    {"name": "Rod of the sea", "price": 750, "type": "rod", "luck": 25},
    {"name": "Rod of the ocean", "price": 1000, "type": "rod", "luck": 40},
    {"name": "Titanium rod", "price": 1500, "type": "rod", "luck": 60},
    {"name": "Australium rod", "price": 2000, "type": "rod", "luck": 80},
    {"name": "Hellfire rod", "price": 3000, "type": "rod", "luck": 90},
    {"name": "God rod", "price": 5000, "type": "rod", "luck": 110},
    
    {"name": "Worm bait", "price": 5, "type": "bait", "luck": 4},
    {"name": "Amazing bait", "price": 50, "type": "bait", "luck": 8},
    {"name": "Fish bait", "price": 200, "type": "bait", "luck": 18},
    {"name": "Shark bait", "price": 400, "type": "bait", "luck": 28},
    {"name": "Master bait", "price": 800, "type": "bait", "luck": 35},
    {"name": "God bait", "price": 1500, "type": "bait", "luck": 45},
    ]




locations = [
    {"locationname": "English lake", "lprice": 100},
    {"locationname": "English river", "lprice": 300},
    {"locationname": "English sea", "lprice": 750},
    {"locationname": "American lake", "lprice": 1500},
    {"locationname": "American river", "lprice": 3000},
    {"locationname": "Lake Malawi", "lprice": 5000},
    {"locationname": "River Nile", "lprice": 7500},
    {"locationname": "Mediterranean Ocean", "lprice": 10000},
    {"locationname": "Great Barrier Reef", "lprice": 12500},
    {"locationname": "Australian river", "lprice": 15000},
    {"locationname": "Antarctica", "lprice": 20000},
    {"locationname": "Amazon river", "lprice": 25000},
    {"locationname": "Mangrove", "lprice": 30000},
    {"locationname": "Your local aquatic store", "lprice": 50000},
    ]


# Shop function using the list of dictionaries








def shop():
    global money
    global shop_open
    global shop_items
    global rod
    global baitbag
    global baitamount

    shop_open = True

    while shop_open:
        try:
            print("You have £", money, "on you right now.")
            print("Items available in the shop:")
            for item in shop_items:
                print(f"{item['name']} - £{item['price']}")

            print("Say what you want to buy, or say \"exit\"\n")
            purchase = input().lower()

            if purchase == "exit":
                print(f"Goodbye {name}!\n")
                print("TIP: If you forgot controls, just say the word \"controls\"")
                print("Current items in your inventory:")
                print(rod)
                print(baitbag)
                shop_open = False
                lucksystem(baitbag)

            else:
                # Check if the item is in the shop_items list
                item_to_buy = None
                for item in shop_items:
                    if item["name"].lower() == purchase:
                        item_to_buy = item
                        break

                if item_to_buy:
                    # Process the purchase
                    if money >= item_to_buy["price"]:
                        print(f"You purchased {item_to_buy['name']}!\n")
                        money -= item_to_buy["price"]

                        if item_to_buy["type"] == "rod":
                            # Remove the current rod, if any
                            if rod:
                                print(f"Removing {rod[0]} from your inventory.")
                                rod.pop(0)
                            # Add the purchased rod to the rod list
                            rod.append(item_to_buy['name'])
                        elif item_to_buy["type"] == "bait":
                            # Update baitbag
                            if not baitbag or baitamount == 0:
                                # If baitbag is empty or the player has 0 bait, simply add the new bait
                                baitbag.append(item_to_buy["name"])
                                baitamount = 32
                                print(f"You now have {item_to_buy['name']} in your baitbag.")
                            else:
                                # Remove existing bait and add the new one
                                baitbag.pop(0)
                                baitbag.append(item_to_buy["name"])
                                print(f"You now have {item_to_buy['name']} in your baitbag.")
                                baitamount = 32
                        else:
                            print("You don't have enough money for that.")
                    else:
                        print("Invalid choice. Try again.")
        except KeyboardInterrupt:
            print("Don't do that mate. Try again.")










# Luck calculation
def lucksystem(baitbag):
    rodluck = 0
    baitluck = 0

    if rod:  # Check if rod list is not empty
        for item in shop_items:
            if item["name"] == rod[0]:
                rodluck = item["luck"]
    
    if baitbag:  # Check if baitbag list is not empty
        for item in shop_items:
            if item["name"] == baitbag[0]:
                baitluck = item["luck"]

    overallluck = rodluck + baitluck
    print("Overall Luck:", overallluck)
    print("Your rod gives you:", rodluck, "luck!")
    print("Your bait gives you:", baitluck, "luck!")    







def airport():
    global currentlocation
    global nmprice
    global airportloop
    global money

    while True:
        try:
            print("Where do you want to travel to? Type 'exit' to leave.")
            print("English Lake - £100")
            print("English River - £300")
            print("English Sea - £750")
            print("American Lake - £1500")
            print("American River - £3000")
            print("Lake Malawi - £5000")
            print("River Nile - £7500")
            print("Mediterranean Ocean - £10000")
            print("Great Barrier Reef - £12500")
            print("Australian River - £15000")
            print("Antarctica - £20000")
            print("Amazon River - £25000")
            print("Mangrove - £30000")
            print("Your local aquatic store - £50000")

            wanted_destination = input().lower()

            if wanted_destination == "exit":
                print("Goodbye! Happy fishing!")
                airportloop = True
                break

            else:
                for itemL in locations:
                    if itemL["locationname"].lower() == wanted_destination:
                        if money >= itemL["lprice"]:
                            print("Traveling to", itemL["locationname"], "!")
                            print("Have a safe flight!")
                            currentlocation = wanted_destination
                            money = money - itemL["lprice"]
                            time.sleep(1)
                            print("Welcome to", itemL["locationname"], "!")
                            print("")
                            print("")
                            break
                        else:
                            print("Not enough money.")
                            break
                    
                else:
                    print("Destination not visible in the database. Try again.\n")

        except KeyboardInterrupt:
            print("Please don't try that.")
        
        



def fishpool(currentlocation):
        
        

    if currentlocation == "english lake":
        return [ #uk lake
            {"name": "Water fern", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Chub", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Grayling", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Barbel", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Dace", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Salmon", "rarity": "uncommon", "sellprice": 15, "caught_before" : False},
            {"name": "Trout", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Three Spined Stickleback", "rarity": "rare", "sellprice": 25, "caught_before" : False},
            {"name": "Schelly", "rarity": "epic", "sellprice": 30, "caught_before" : False},
            {"name": "Atlantic Sturgeon", "rarity": "legendary", "sellprice": 55, "caught_before" : False},
            {"name": "Schneider's Smelt", "rarity": "legendary", "sellprice": 55, "caught_before" : False},
            {"name": "Loch Ness Monster", "rarity": "mythic", "sellprice": 100, "caught_before" : False}
        ]


    if currentlocation == "english river":
        return [ #UK river
            {"name": "Common reed", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Bleak", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Dace", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Gudgeon", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Roach", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Minnow", "rarity": "uncommon", "sellprice": 15, "caught_before" : False},
            {"name": "Ide", "rarity": "common", "sellprice": 10, "caught_before" : False},
            {"name": "Zander", "rarity": "rare", "sellprice": 25, "caught_before" : False},
            {"name": "Wels Catfish", "rarity": "rare", "sellprice": 25, "caught_before" : False},
            {"name": "Asp", "rarity": "epic", "sellprice": 30, "caught_before" : False},
            {"name": "European eel", "rarity": "legendary", "sellprice": 55, "caught_before" : False},
            {"name": "Beluga Sturgeon", "rarity": "legendary", "sellprice": 55, "caught_before" : False},
            {"name": "Water Hydra", "rarity": "mythic", "sellprice": 100, "caught_before" : False}
            ]

    
    if currentlocation == "english sea":
        return [ #UK sea
            {"name": "Kelp", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Cod", "rarity": "common", "sellprice": 15, "caught_before" : False},
            {"name": "Haddock", "rarity": "common", "sellprice": 15, "caught_before" : False},
            {"name": "Mackerel", "rarity": "common", "sellprice": 15, "caught_before" : False},
            {"name": "Herring", "rarity": "common", "sellprice": 15, "caught_before" : False},
            {"name": "Conger Eel", "rarity": "rare", "sellprice": 30, "caught_before" : False},
            {"name": "Thornback Ray", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Common Skate", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Warty Sea Cucumber", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Leafscale Gulper Shark", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Longsnout Dogfish", "rarity": "legendary", "sellprice": 65, "caught_before" : False},
            {"name": "Kraken", "rarity": "mythic", "sellprice": 125, "caught_before" : False}
            ]

    if currentlocation == "american lake":
        return [ #USA Lake
            {"name": "Coontail", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Largemouth Bass", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Bluegill", "rarity": "uncommon", "sellprice": 20, "caught_before" : False},
            {"name": "Yellow Perch", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Channel Catfish", "rarity": "rare", "sellprice": 35, "caught_before" : False},
            {"name": "Walleye", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "Crappie", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "Northern Pike", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Blue Catfish", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Rock Bass", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Humpback Chub", "rarity": "legendary", "sellprice": 65, "caught_before" : False},
            {"name": "Alligator Garr", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Devil's Hole Pupfish", "rarity": "legendary", "sellprice": 70, "caught_before" : False},
            {"name": "Alabama sturgeon", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Bigfoot", "rarity": "mythic", "sellprice": 100, "caught_before" : False}
            ]
    
    if currentlocation == "american river":
        return [ #USA river
            {"name": "Lupine", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Common Carp", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Channel Catfish", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "Rainbow Trout", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Smallmouth Bass", "rarity": "rare", "sellprice": 35, "caught_before" : False},
            {"name": "Lake Sturgeon", "rarity": "rare", "sellprice": 35, "caught_before" : False},
            {"name": "Paddlefish", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Muskie", "rarity": "epic", "sellprice": 45, "caught_before" : False},
            {"name": "Walleye", "rarity": "legendary", "sellprice": 70, "caught_before" : False},
            {"name": "Brook Trout", "rarity": "legendary", "sellprice": 65, "caught_before" : False},
            {"name": "Sturgeon", "rarity": "legendary", "sellprice": 60, "caught_before" : False},
            {"name": "White sucker", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Longear Sunfish", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Shorthead Redhorse", "rarity": "uncommon", "sellprice": 25, "caught_before" : False},
            ]
    
    if currentlocation == "lake malawi":
        return [ #lake M
            {"name": "Vallisneria", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Zebra Mbuna Cichlid", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Electric Yellow Lab", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Red Zebra Cichlid", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Afra Cichlid", "rarity": "uncommon", "sellprice": 25, "caught_before" : False},
            {"name": "Auratus Cichlid", "rarity": "uncommon", "sellprice": 20, "caught_before" : False},
            {"name": "Electric Blue Hap", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Super VC-10 Hap", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Peacock Cichlid", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Red Empress", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Azureus Hap", "rarity": "rare", "sellprice": 45, "caught_before" : False},
            {"name": "Blue Dolphin Cichlid", "rarity": "epic", "sellprice": 55, "caught_before" : False},
            {"name": "Giraffe Hap", "rarity": "epic", "sellprice": 55, "caught_before" : False},
            {"name": "Maleri Peacock Cichlid", "rarity": "legendary", "sellprice": 70, "caught_before" : False},
            {"name": "Taiwan Reef Hap", "rarity": "legendary", "sellprice": 70, "caught_before" : False},
            {"name": "Super Red Top Likoma", "rarity": "legendary", "sellprice": 70, "caught_before" : False},
            ]
    if currentlocation == "river nile":
        return [ #River N
            {"name": "Water Lotus", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Zillii Tilapia", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "African Butter Catfish", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Forskal's Labeo", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Nile Perch", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Upside Down Catfish", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Electric Catfish", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "African Arowana", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "African Butterfish", "rarity": "epic", "sellprice": 40, "caught_before" : False},
            {"name": "Nile Alligator", "rarity": "legendary", "sellprice": 75, "caught_before" : False},
            {"name": "African Sharptooth Catfish", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            ]
    
    if currentlocation == "mediterranean ocean":
        return [ #med ocean
            {"name": "Posidonia", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Gilthead Seabream", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "European Sea Bass", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "Red Mullet", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "European Barracuda", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Dusky Grouper", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Dentex", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Atlantic Bluefin Tuna", "rarity": "epic", "sellprice": 65, "caught_before" : False},
            {"name": "Ocean Sunfish", "rarity": "epic", "sellprice": 70, "caught_before" : False},
            {"name": "Anglerfish", "rarity": "epic", "sellprice": 65, "caught_before" : False},
            {"name": "Goliath Grouper", "rarity": "legendary", "sellprice": 80, "caught_before" : False},
            {"name": "Mobula Ray", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Thresher Shark", "rarity": "legendary", "sellprice": 80, "caught_before" : False},
            {"name": "Sea Serpent", "rarity": "mythic", "sellprice": 200, "caught_before" : False}
            ]

    if currentlocation == "great barrier reef":
        return [ # GBR
            {"name": "Sea lettuce", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Common Clownfish", "rarity": "common", "sellprice": 25, "caught_before" : False},
            {"name": "Blue Green Chromis", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Powdered Blue Tang", "rarity": "uncommon", "sellprice": 35, "caught_before" : False},
            {"name": "Lemon Damsel", "rarity": "uncommon", "sellprice": 35, "caught_before" : False},
            {"name": "Hippocampus Seahorse", "rarity": "uncommon", "sellprice": 45, "caught_before" : False},
            {"name": "Napoleon Wrasse", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Pallete Surgeonfish", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Yellow Tang", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Picasso Triggerfish", "rarity": "epic", "sellprice": 60, "caught_before" : False},
            {"name": "Neon Slug", "rarity": "epic", "sellprice": 55, "caught_before" : False},
            {"name": "Spinner Dolphin", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Humphead Parrotfish", "rarity": "epic", "sellprice": 60, "caught_before" : False},
            {"name": "White Spotted Pufferfish", "rarity": "epic", "sellprice": 75, "caught_before" : False},
            {"name": "Queen Angelfish", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Green Sea Turtle", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            {"name": "Red Lionfish", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            {"name": "Manta Ray", "rarity": "legendary", "sellprice": 150, "caught_before" : False},
            {"name": "Megladon", "rarity": "mythic", "sellprice": 400, "caught_before" : False}
            ]

    if currentlocation == "australian river":
        return [ #aus river
            {"name": "Waterhyssop", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Australian Bass", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Burramundi", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Mary River Cod", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Silver Perch", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Spangled Perch", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Freshwater Catfish", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Jungle Perch", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Golden Perch", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Eel-Tailed Catfish", "rarity": "epic", "sellprice": 60, "caught_before" : False},
            {"name": "Giant Mud Crab", "rarity": "epic", "sellprice": 50, "caught_before" : False},
            {"name": "Mary River Turtle", "rarity": "legendary", "sellprice": 90, "caught_before" : False},
            {"name": "Freshwater Crocodile", "rarity": "legendary", "sellprice": 150, "caught_before" : False},
            {"name": "Saxton Hale", "rarity": "mythic", "sellprice": 300, "caught_before" : False}
            ]

    if currentlocation == "antarctica":
        return [ #antarctica
            {"name": "Algae", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Antarctic Toothfish", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Antarctic Silverfish", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Krill", "rarity": "common", "sellprice": 30, "caught_before" : False},
            {"name": "Icefish", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Antarctic Dragonfish", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Weddell Seal", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Antarctic Cod", "rarity": "rare", "sellprice": 40, "caught_before" : False},
            {"name": "Emperor Penguin", "rarity": "rare", "sellprice": 60, "caught_before" : False},
            {"name": "Adelie Penguin", "rarity": "rare", "sellprice": 60, "caught_before" : False},
            {"name": "Wandering Albatross", "rarity": "epic", "sellprice": 75, "caught_before" : False},
            {"name": "Leopard Seal", "rarity": "epic", "sellprice": 90, "caught_before" : False},
            {"name": "Orca", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            {"name": "Blue Whale", "rarity": "legendary", "sellprice": 200, "caught_before" : False},
            {"name": "Colossal Squid", "rarity": "legendary", "sellprice": 250, "caught_before" : False},
            {"name": "Yeti", "rarity": "mythic", "sellprice": 500, "caught_before" : False}
            ]

    if currentlocation == "amazon river":
        return [ #amz river
            {"name": "Giant water lilly", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Neon Tetra", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Corydora Catfish", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Angelfish", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Electric Blue Acara", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Rummynose Tetra", "rarity": "uncommon", "sellprice": 35, "caught_before" : False},
            {"name": "Bristlenose Tetra", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Black Piranha", "rarity": "rare", "sellprice": 50, "caught_before" : False},
            {"name": "Red Bellied Piranha", "rarity": "rare", "sellprice": 60, "caught_before" : False},
            {"name": "Arowana", "rarity": "epic", "sellprice": 70, "caught_before" : False},
            {"name": "Redtail Catfish", "rarity": "epic", "sellprice": 70, "caught_before" : False},
            {"name": "Arapaimas Gigas", "rarity": "legendary", "sellprice": 75, "caught_before" : False},
            {"name": "Amazonian Manatee", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            {"name": "Capybara", "rarity": "mythic", "sellprice": 250, "caught_before" : False}
            ]

    if currentlocation == "mangrove":
        return [ #mangrove
            {"name": "Mangrove branch", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Mangrove Snapper", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Mud Skipper", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Mullet", "rarity": "common", "sellprice": 20, "caught_before" : False},
            {"name": "Fiddler Crab", "rarity": "uncommon", "sellprice": 30, "caught_before" : False},
            {"name": "Archer Fish", "rarity": "uncommon", "sellprice": 40, "caught_before" : False},
            {"name": "Halfbeak", "rarity": "uncommon", "sellprice": 50, "caught_before" : False},
            {"name": "Mangrove Seahorse", "rarity": "rare", "sellprice": 60, "caught_before" : False},
            {"name": "Mangrove Jack", "rarity": "rare", "sellprice": 60, "caught_before" : False},
            {"name": "Spotted Garr", "rarity": "rare", "sellprice": 65, "caught_before" : False},
            {"name": "Pygmy Sloth", "rarity": "epic", "sellprice": 75, "caught_before" : False},
            {"name": "Snook", "rarity": "epic", "sellprice": 80, "caught_before" : False},
            {"name": "Bull Shark", "rarity": "legendary", "sellprice": 100, "caught_before" : False},
            ]

    if currentlocation == "Your local aquatic store":
        return [ #mh
            {"name": "Anubias Barteri", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Duckweed", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Cryptocoryne", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Java fern", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Moss ball", "rarity": "plant", "sellprice": 15, "caught_before" : False},
            {"name": "Amano shrimp", "rarity": "common", "sellprice": 4, "caught_before" : False},
            {"name": "Cherry shrimp", "rarity": "common", "sellprice": 3, "caught_before" : False},
            {"name": "Nerite snail", "rarity": "common", "sellprice": 1, "caught_before" : False},
            {"name": "Bladder snail", "rarity": "common", "sellprice": 1, "caught_before" : False},
            {"name": "Zebra Danio", "rarity": "uncommon", "sellprice": 3, "caught_before" : False},
            {"name": "Chilli Rasbora", "rarity": "uncommon", "sellprice": 20, "caught_before" : False},
            {"name": "Rainbow Guppy", "rarity": "rare", "sellprice": 16, "caught_before" : False},
            {"name": "Pea Puffer", "rarity": "rare", "sellprice": 15, "caught_before" : False},
            {"name": "Neon Tetra", "rarity": "rare", "sellprice": 3, "caught_before" : False},
            {"name": "Corydora catfish", "rarity": "rare", "sellprice": 46, "caught_before" : False},
            {"name": "Betta", "rarity": "epic", "sellprice": 20, "caught_before" : False},
            {"name": "Pearl gourami", "rarity": "epic", "sellprice": 10, "caught_before" : False},
            {"name": "Endler's livebearer", "rarity": "legendary", "sellprice": 15, "caught_before" : False},
            {"name": "Employee", "rarity": "mythic", "sellprice": 100, "caught_before" : False},
            ]








def weather():
    global current_weather
    global money
    global luck

    while True:
        try:
            print("The weather is currently:", current_weather)
            weather_query = input("A godly voice whispers in your ears \"Do you want to change the weather? It only costs £100...\"\n").lower()
            
            if weather_query in ["yes", "y"]:
                if money >= 100:
                    money -= 100
                    current_weather = random.choice(Weather_Outcomes)
                    
                    if current_weather == "raining":
                        luck += 10
                    elif current_weather == "stormy":
                        luck += 5
                    elif current_weather == "snowing":
                        luck += 1

                    print("The weather has been changed to:", current_weather)

                else:
                    print("You don't have enough money!")

            elif weather_query in ["no", "n"]:
                print("The godly voice whispers \"Goodbye!\"")
                break

            else:
                print("Invalid input! Try again!")

        except KeyboardInterrupt:
            print("Bruh stop trying that it's mean >:(")

    
        
    
    

    

    






def catching_system():
    global money, baitamount, luck, currentlocation, luck_multiplier, caughtbefore, fishdex

    try:
        if baitamount == 0:
            baitbag.clear()

        fishlist = fishpool(currentlocation)

        # Adjusting the rarity probabilities based on luck
        rarity_probabilities = adjust_rarity_probabilities(luck)

        # Randomly select a rarity based on adjusted probabilities
        rarity = random.choices(list(rarity_probabilities.keys()), weights=list(rarity_probabilities.values()))[0]

        # Filter fish list based on selected rarity
        filtered_fish = [fish for fish in fishlist if fish["rarity"] == rarity]

        if filtered_fish:
            fish_data = random.choice(filtered_fish)
            fish = fish_data["name"]
            if current_weather == "sunny":
                sellprice = fish_data["sellprice"]
                sellprice = sellprice * 1.25
            else:
                sellprice = fish_data["sellprice"]

            caughtbefore = fish_data["caught_before"]

            print("Your bobber has been cast!")

            if current_weather == "windy":
                bobresttime = (3, 7)
            elif current_weather == "hailing":
                bobresttime = (1, 4)
            elif current_weather == "stormy":
                bobresttime = (3, 6)
            else:
                bobresttime = (2, 5)

            time.sleep(random.choice(bobresttime))

            print("A fish has latched on! Reel!")
            start_time = time.time()
            reel_input = input().lower()
            end_time = time.time()
            reel_time = end_time - start_time

            if reel_time > 5:
                if baitamount > 0:
                    baitamount -= 1
                    print("You were too slow so the fish swam away with your bait!\n")
                else:
                    print("You were too slow so the fish swam away!\n")

            elif reel_input == "reel":
                if fish not in fishdex:
                    caughtbefore = False
                else:
                    caughtbefore = True

                if caughtbefore == False:
                    if baitamount > 0:
                        print("You caught a new fish species!")
                        fishdex.append(fish)
                        baitamount -= 1
                        print(f"You caught a {fish}!")
                        print(f"It's {rarity}")
                        print(f"You sold the {fish} for ${sellprice}.\n")
                        money += sellprice
                        fishdexFUNCTION()
                    else:
                        print("You caught a new fish species!")
                        fishdex.append(fish)
                        print(f"You caught a {fish}!")
                        print(f"It's {rarity}")
                        print(f"You sold the {fish} for ${sellprice}.\n")
                        money += sellprice
                        fishdexFUNCTION()

                else:
                    if baitamount > 0:
                        baitamount -= 1
                        print(f"You caught a {fish}!")
                        print(f"It's a {rarity} fish!")
                        print(f"You sold the {fish} for ${sellprice}.\n")
                        money += sellprice
                    else:
                        print(f"You caught a {fish}!")
                        print(f"It's a {rarity} fish!")
                        print(f"You sold the {fish} for ${sellprice}.\n")
                        money += sellprice

    except KeyboardInterrupt:
        print("Mate can you not try that.")







# Adjusting rarity probabilities based on luck
def adjust_rarity_probabilities(luck):
    if luck != 0:  # Avoid division by zero
        luck_multiplier = 1.0 + 0.5 * (luck // 5)
    else:
        luck_multiplier = 1.0
    
    # Adjusting the rarity probabilities based on luck
    rarity_probabilities = {
        "common": max(0.1, 0.5 / luck_multiplier),  # Adjusting the base probability to ensure it's not too small
        "uncommon": max(0.1, 0.4 / luck_multiplier),
        "rare": max(0.1, 0.2 / luck_multiplier),
        "epic": max(0.05, 0.1 / luck_multiplier),
        "legendary": max(0.025, 0.05 / luck_multiplier),
        "mythic": max(0.005, 0.01 / luck_multiplier),
        "plant": max(0.1, 0.5 / luck_multiplier)
    }
    return rarity_probabilities



def cutscene1():
    print("Cap'n Corkah: Well done, lad! Ye've caught yer first fish!")
    time.sleep(4)
    print("Cap'n Corkah: But remember, there's more to anglin' than just reelin' them in.")
    time.sleep(5)
    print("Cap'n Corkah: Let me give ye some tips to become a true master angler.")
    time.sleep(4)
    print("")
    print("Cap'n Corkah: First, always pay attention to the weather.")
    time.sleep(4)
    print("Cap'n Corkah: Different weather conditions affect what fish ye catch, how much they sell for, and a whole heap o' other things.")
    time.sleep(7)
    print("")
    print("Cap'n Corkah: Second, don't forget to use the right bait.")
    time.sleep(4)
    print("Cap'n Corkah: The more expensive the bait is, the better fish ye can catch. Don't disregard 'em!")
    time.sleep(5)
    print("")
    print("Cap'n Corkah: And finally, be patient!")
    time.sleep(3)
    print("Cap'n Corkah: Fishing is a game of waitin', but the rewards be worth it in the end.")
    time.sleep(5)
    print("")
    print("Cap'n Corkah: Keep these tips in mind, and ye'll be reelin' in the big ones in no time!")




#----------------------------------------------------------------------------------------------------------------------------------



def cutscene2():
    print("Cap'n Corkah: Arrr, what a day for fishin', wouldn't ye say, matey?")
    print("Cap'n Corkah: Keep an eye on them waters now, the wind's changin' direction.")
    print("")
    time.sleep(7)
    print("As you cast your line into the shimmering waters, a mysterious breeze begins to pick up.")
    print("The once calm sea starts to churn, and you feel a sense of anticipation in the air.")
    print("")
    time.sleep(7)
    print("Cap'n Corkah: There be somethin' peculiar 'bout this breeze, lad. Keep yer wits about ye!")
    print("Cap'n Corkah: Look! The water beneath us, it's vanishing afore our eyes!")
    print("")
    time.sleep(7)
    print("You peer over the side of the boat and see the water rapidly receding, revealing a hidden passageway beneath.")
    print("Without hesitation, you and Cap'n Corkah follow the winding path into the depths of the cave.")
    print("")
    time.sleep(8)
    print("Cap'n Corkah: Aye, this be no ordinary cave. Legends speak of hidden treasures hidden away in these very waters!")
    print("Cap'n Corkah: Keep yer lantern lit, lad. We're explorin' the unknown now!")
    print("")
    time.sleep(9)
    print("As you navigate through the narrow passageways, the cave's walls seem to whisper ancient secrets of long-forgotten times.")
    print("Suddenly, you stumble upon a vast cavern, illuminated by the faint glow of bioluminescent fungi.")
    print("")
    time.sleep(9)
    print("Cap'n Corkah: By the Seven Seas! Look yonder, lad!")
    print("Cap'n Corkah: 'Tis the treasure cove of old Captain Blackfin, a legend among pirates!")
    print("")
    time.sleep(9)
    print("You gaze in awe at the sight before you - a hoard of glittering riches, strewn about the cavern floor.")
    print("Among the treasures lies a peculiar artifact, adorned with intricate engravings.")
    print("")
    time.sleep(9)
    print("Cap'n Corkah: Take a gander at this, matey. 'Tis a relic of the sea, forged by hands long gone.")
    print("Cap'n Corkah: This here be a token of the past, holdin' secrets untold.")
    print("")
    time.sleep(9)
    print("With trembling hands, you reach out and grasp the artifact, feeling its weight and significance.")
    print("Cap'n Corkah: Crikey! That's bleedin Blackfin's Cuisnart Toaster!")
    print("A sense of purpose fills your heart, and you know that your journey has only just begun.")
    print("")
    time.sleep(9)
    print("Cap'n Corkah: 'Tis time we return to shore, lad. The sea's callin', but me ship needs mendin'.")
    print("Cap'n Corkah: Ye, however, have a destiny to fulfill. Keep this treasure close, for it may yet guide ye to greatness!")
    print("")
    time.sleep(9)
    print("With the artifact safely stowed away, you bid farewell to the treasure cove and set sail for new horizons.")
    print("As Cap'n Corkah heads home to repair his ship, you steel yourself for the adventures that lie ahead.")
    print("The sea awaits, and so does your destiny!")

#----------------------------------------------------------------------------------------------------------------------------------


def cutscene3():
    print ("As you fish, you see dark clouds loom overhead, as a fishing vessel appears out of the gloom.")
    time.sleep(4)
    print ("A band of fierce fishermen appear on the bow of their ship, standing ready for confrontation.")
    time.sleep(4)
    print ("")
    print("Rival Fisherman 1: Arr, what have we here? Looks like some fresh bait has wandered into our territory!")
    time.sleep(5)
    print("Rival Fisherman 2: Ye best be turnin' tail and sailin' back to yer own waters, matey!")
    time.sleep(4)
    print("Rival Fisherman 3: Aye, but if ye be wantin' to pass through, ye gotta prove yer worth against us!")
    time.sleep(5)
    print("Rival Fisherman 1: We'll see if ye be worthy of treadin' these waters!")
    time.sleep(4)
    print("Rival Fisherman 2: Aye, let's show 'em what it means to challenge the might of the Seafarer's syndicate!")
    time.sleep(5)
    print("")
    print("You find yourself confronted by the fierce rival fishermen, known as the Seafarer's syndicate.")
    time.sleep(4)
    print("It seems you'll have to battle them if you want to proceed.")
    time.sleep(3)
    print("Prepare yourself for a challenging confrontation!")
    time.sleep(3)
    print("")
    print("")

    Fight_One()



def Fight_One():
    global boat_health, boat_defence, enemy_boat_health
    boat_health = 100
    boat_defence = 5
    enemy_boat_health = 100

    print("You remember that you have a loaded shotgun in your cabin in case of emergencies.")
    time.sleep(1)
    print("You grab the shotgun and ready up for the oncoming battle.")
    time.sleep(1)

    def fight_input():
        global boat_health, boat_defence, enemy_boat_health
        print("Do you want to:\n1. Shoot at them\n2. Cast your rod and hope for something that may help.")

        try:
            choice = input()
        except KeyboardInterrupt:
            print("\nYou can't escape the battle!")
            fight_input()

        if choice == "1" or choice.lower() == "shoot":
            print("You load your shotgun and aim at the enemy ship.")
            boat_hitpoints = ("mast", "stern", "hull", "propeller")
            boat_hit_point = random.choice(boat_hitpoints)
            damage = random.randint(10, 20)

            print("You did", damage, "damage to the ship's", boat_hit_point, "!")
            time.sleep(1)
            print("")
            enemy_boat_health -= damage
            if enemy_boat_health <= 0:
                print("You won the battle!")
                print("The enemy boat slowly sinks into the water as the defeated pirates paddle into the distance on a tiny life raft...")
                print("Back to fishing!")
                print("")
            elif enemy_boat_health > 0:
                print("The enemy has", enemy_boat_health, "health left.")
                time.sleep(1)
                print("")
                enemy_fight_input()

        elif choice == "2" or choice.lower() == "cast":
            print("You cast out a line hoping to catch something that may help.")
            time.sleep(1)
            loot_outcomes = ("boot", "wooden plank", "plastic bag", "crate", "glue", "oar")
            loot_obtained = random.choice(loot_outcomes)

            if loot_obtained in ("boot", "plastic bag"):
                print("You fished out a", loot_obtained, "which doesn't help!")
                time.sleep(1)
                print("")
                enemy_fight_input()

            elif loot_obtained in ("wooden plank", "glue"):
                boat_defence += 2
                print("You fished out a", loot_obtained, "which increased your boat's strength so damage taken is reduced!")
                time.sleep(1)
                print("")
                enemy_fight_input()

            elif loot_obtained == "crate":
                boat_health += 10
                print("You fished out a crate which had supplies to help mend your boat!")
                time.sleep(1)
                print("Your boat has",boat_health,"health left.")
                print("")
                enemy_fight_input()

            elif loot_obtained == "oar":
                print("The oar gave your boat some extra speed so you get another go!")
                time.sleep(1)
                print("")
                fight_input()

        else:
            print("Invalid input. Try again!")
            fight_input()
            
    def enemy_fight_input():
        global boat_health, boat_defence, enemy_boat_health
        enemy_random_choice = random.randint(1,2)

        if enemy_random_choice == 1:
            print("The three buccaneers aim their pistols at your ship, and you dive for cover.")
            time.sleep(1)
            boat_hitpoints = ("mast", "stern", "hull", "propeller")
            boat_hit_point = random.choice(boat_hitpoints)
            enemy_damage = random.randint(10, 30)
            real_enemy_damage = max(0, enemy_damage - boat_defence)

            print("The enemy bombarded your ship with their pistols, dealing", real_enemy_damage, "damage to your", str(boat_hit_point) + "!")
            time.sleep(1)
            print("")
            boat_health -= real_enemy_damage

            if boat_health <= 0:
                print("Your boat was torn to pieces by the enemy fisherman, and you slowly sink into the water.")
                print("Everything fades to black...")
                print("A faint voice whispers: You have to be careful out there!")
                print("Go back out there and show those pirates what you are made of!")
                print("You wake up, realising half of your money is missing... Those damn pirates...")
                money = money/2
                Fight_One()
            elif boat_health > 0:
                print("Your boat has", boat_health, "health remaining.")
                print("")
                fight_input()

        elif enemy_random_choice == 2:
            print("One of the rival fishermen cast out a line.")
            time.sleep(1)
            enemy_loot_outcomes = ("boot", "plastic bag", "crate", "oar")
            enemy_loot_obtained = random.choice(enemy_loot_outcomes)

            if enemy_loot_obtained in ("boot", "plastic bag"):
                print("They fished out a", enemy_loot_obtained, "which does nothing!")
                time.sleep(1)
                print("")
                fight_input()

            elif enemy_loot_obtained == "crate":
                enemy_boat_health += 10
                print("They fished out a crate which had supplies that healed their boat!")
                print ("The enemy has",enemy_boat_health,"health remaining.")
                time.sleep(1)
                print("")
                fight_input()

            elif enemy_loot_obtained == "oar":
                print("They fished out an oar which gave them enough speed to have another go!")
                time.sleep(1)
                print("")
                enemy_fight_input()

    fight_input()


#---------------------------------------------------------------------------------------------------------------------------








            
def fight_2():
    #kraken fight
    #attack tentacles
    #get swallowed into kraken
    #destroy it from inside

    kraken_health = 50
    boat_health = 500

    print ("Get ready to have the battle of a lifetime!")

    def phase_1_kraken():
        nonlocal kraken_health
        nonlocal boat_health

        print("Controls:")
        print("1. Cannon")
        print("2. Reel")

        while True:
            try:
                kinput = input("Enter your input: ")
            except KeyboardInterrupt:
                print("\nYou can't escape the battle!")
                continue

            if kinput == "1" or kinput.lower() == "cannon":
                print ("You shot at a tentacle!")
                print ("It did 50 damage.")
                kraken_health -= 50
                if kraken_health <= 0:
                    print ("The kraken recoiled its tentacles!")
                    phase_2_kraken()
                else:
                    print ("It has", kraken_health, "health left.")
                    kraken_move()

            elif kinput == "2" or kinput.lower() == "reel":
                lootL = ("crate", "wooden plank", "boot", "glue")
                loot = random.choice(lootL)

                if loot == "crate":
                    print ("You fished up a crate and you healed your boat for 50 health.")
                    boat_health += 50
                    print ("Your boat now has", boat_health, "health.")
                    kraken_move()

                elif loot == "wooden plank":
                    print ("You fished up a wooden plank and healed your boat your 25 health.")
                    boat_health += 25
                    print ("Your boat now has", boat_health, "health remaining.")
                    kraken_move()

                elif loot == "boot":
                    print ("You fished up a boot which did nothing.")
                    kraken_move()

                elif loot == "glue":
                    print ("You fished up some glue which healed your boat for 10 health.")
                    boat_health += 10
                    print ("Your boat now has", boat_health, "health remaining.")
                    kraken_move()

            else:
                print ("Not a valid response. Try again.")
                continue

    def kraken_move():
        nonlocal kraken_health
        nonlocal boat_health
        
        kraken_dmg = random.randint(40, 70)
        print ("The mighty kraken slams its tentacle into your boat, dealing", kraken_dmg, "to you!")
        boat_health -= kraken_dmg
        print ("Your boat has", boat_health, "health left.")
        if boat_health <= 0:
            print ("You ran out of health!")
            print ("....")
            fight_2()
        phase_1_kraken()

    def phase_2_kraken():
        print("With a thunderous crash, the last tentacle recoils, defeated.")
        time.sleep(1)
        print("But before you can celebrate, a violent jolt throws you into the yawning mouth of the Kraken!")
        time.sleep(2)
        print(".")
        print("...")
        print("You wake up in a daze, surrounded by the fleshy insides of the giant sea monster.")
        time.sleep(2)
        print("The leviathan's acids slowly burn away at your clothes, so it's only a matter of time before your eaten alive....")
        time.sleep(1)
        print("You remember you still have your shotgun on you, your last hope at survival...")
        time.sleep(2)

        print ("Enter anything to shoot!")
        print ("Be quick so you don't get digested by the acid!")

        start_time = time.time()

        duration = 20
        shots_fired = 0

        while time.time() - start_time < duration:
            try:
                belly_input = input()
                shots_fired += 1
                print ("You shot at the monsters insides. Do it again!")
                if shots_fired == 10:
                    print ("The creature gurgles. Do it more!")

                if shots_fired == 25:
                    print ("You hear a giant screaming noise. Do it more!")
                
                if shots_fired == 40:
                    print ("The creature is thrashing around! Your nearly there!")
                
                if shots_fired == 50:
                    time.sleep(1)
                    print ("You shot at the monster's insides and it burst open!")
                    kraken_end()
                    return

            except KeyboardInterrupt:
                print("\nYou can't escape the battle!")
                continue
                
        print ("You were too slow, and you were digested by the monster!")
        print ("..............")
        phase_2_kraken()
        
        
        

    def kraken_end():
        print("You get shot out of the creature's innards, as it screams in pain.")
        time.sleep(4)
        print("Picking yourself off the floor of your boat, you take a moment to catch your breath.")
        time.sleep(4)
        print("")
        print("The once turbulent sea now lays calm around you, the remnants of the Kraken slowly sinking beneath the waves.")
        time.sleep(6)
        print("As you survey the aftermath, you notice something glinting amidst the debris.")
        time.sleep(5)
        print("")
        print("Curious, you reach out and find a small chest wedged between pieces of flesh and broken ship parts.")
        time.sleep(5)
        print("With a sense of anticipation, you pry it open and discover its contents.")
        time.sleep(4)
        print("")
        print("Inside, you find a collection of precious gems, artifacts, and a mysterious ancient map totalling to £150.")
        time.sleep(6)
        money = money + 150
        print("Whilst searching through the treasures, you see a green reflection emit from the bridge.")
        time.sleep(5)
        print("It seems to be the Cuisnart toaster you obtained in your earlier travels.")
        time.sleep(5)
        print("")
        print("Remembering your journey to acquire it, you realize that this toaster might be more than it seems.")
        time.sleep(5)
        print("")
        print("Suddenly, as if in response to your thoughts, the toaster begins to emit a soft, pulsating glow.")
        time.sleep(5)
        print("The glow intensifies, casting an otherworldly light that illuminates your surroundings.")
        time.sleep(5)
        print("")
        print("Intrigued and somewhat awestruck by the toaster's newfound radiance, you sense that it holds hidden powers yet to be unlocked.")
        time.sleep(6)
        print("With a smile, you carefully stow away the glowing Cuisinart toaster, knowing that it may prove invaluable in your future adventures.")

    phase_1_kraken()

def cutscene4():
    print ("As the ship sailed through the calm waters, a foreboding presence lurked beneath the surface.")
    time.sleep(3)
    print ("Suddenly, with a violent thrash, a massive tentacle erupted from the depths, signaling the arrival of the Kraken!")
    time.sleep(5)
    print ("You spring into action, scrambling to man the cannons as the ship rocked under the creature's immense strength.")
    time.sleep(5)
    print ("With each passing moment, the situation grew more dire as the Kraken's tentacles coiled around the vessel, threatening to crush it.")
    time.sleep(8)
    fight_2()


#----------------------------------------------------------------------------------------------------------------------------------

def cutscene5():
    print ("---------------------------------------------------------------------------------------------------------------------------------------------")
    print ("As the sun begins to dip below the horizon, casting long shadows across the ocean, the player notices several boats in the distance, rapidly approaching their location.")
    time.sleep(3)
    print ("Amidst the sound of crashing waves, the player strains to hear voices carried on the wind. Among them, they discern the unmistakable tones of Cap'n Corkah, his voice filled with anger and frustration.")
    time.sleep(3)
    print ("")
    print ("Cap'n Corkah: Ye scallywags! Ye think ye can silence me? I'll have ye know— ")
    time.sleep(3)
    print ("Cap'n Corkah: Ow!")
    print ("")
    time.sleep(2)
    print ("Finn Marlin: Shut yer trap, Corkah! We've got business to attend to.")
    time.sleep(3)
    print ("As the boats draw nearer, one of them glides smoothly alongside the player's vessel, and with practiced ease, three faction leaders leap aboard.")
    time.sleep(3)
    print ("")
    print ("Captain Barnacle: Listen up, matey. We've got news for ye, and it ain't good.")
    time.sleep(3)
    print ("Marina Swiftwind: Corkah's been snatched right from under yer nose. Kidnapped, he is.")
    time.sleep(3)
    print ("Cap'n Corkah's voice rises above the din once more, frantic and urgent.")
    print ("")
    time.sleep(3)
    print ("Cap'n Corkah: Lad, ye've got to help me! They've taken me, and I fear for the village. Ye've got to stop—")
    time.sleep(3)
    print ("But the leaders waste no time in asserting their control over the situation.")
    print ("")
    time.sleep(3)
    print ("Finn Marlin: Quiet, Corkah! We've got this under control. And as for ye, listen up. We're calling the shots now.")
    time.sleep(3)
    print ("Captain Barnacle: Aye, that's right. And if ye want to see Corkah again, ye'll do as we say.")
    time.sleep(3)
    print ("Marina Swiftwind: We'll be waitin' for ye at the village. Don't keep us waiting too long.")
    print ("")
    time.sleep(3)
    print ("Despite Corkah's protests, the leaders make it clear that they're in charge. With a swift kick to silence the captain, they make their exit.")
    time.sleep(3)
    print ("Unsure of what to do, you decide to carry on your journey until you can learn more about the situation.")

#----------------------------------------------------------------------------------------------------------------------------------

def cutscene6():
    print("After a while of contemplating what you should do next, you decide to travel towards the village.")
    time.sleep(4)
    print("")
    print("After a while of sailing, you see a vessel you seem to remember from your childhood.")
    time.sleep(4)
    print("It's Barry Bobkin's ship!")

    print("")
    time.sleep(2)
    print("Barry Bobkin: Hey there, matey. Got some news for ya, and it ain't good.")
    time.sleep(2)
    print("Barry Bobkin: I've managed to sneak outta that village, but it's a mess in there. The faction leaders got everyone in a tight grip.")
    time.sleep(5)
    print("Barry Bobkin: People are scared stiff. Can't even whisper 'round there without gettin' in trouble.")
    time.sleep(3)
    print("Barry Bobkin: Tried to stand up to 'em, but it didn't end well for those brave enough to try.")
    print("")
    time.sleep(3)
    print("Barry Bobkin: I made a run for it when I had the chance, but I knew someone had to do something about it.")
    time.sleep(3)
    print("Barry Bobkin: What they're after exactly, I dunno. But they're up to no good, that's for sure.")
    time.sleep(3)
    print("Barry Bobkin: If you're headin' in there, watch your back. These guys ain't playin' around.")
    print("")
    time.sleep(3)
    print("Barry Bobkin: Just remember, you gotta be smart about this. Their security is tight, so sneaking around is the only way to work. Prepare yourself my friend.")
    time.sleep(5)
    print("")
    print("You turn towards the village, ready to confront whatever awaits you.")
    print("")

    time.sleep(3)

    print ("")
    print ("Arriving at the village, you crouch in some bushes, overhearing some of the guard's conversations.")
    time.sleep(3)

    print("\nGuard 1: Ey, ye know what's bett'r than a bottle o' rum?")
    time.sleep(2)
    print("Guard 2: What's that, matey?")
    time.sleep(2)
    print("Guard 1: Two bottles o' rum! *laughs*")
    time.sleep(2)
    print("Guard 2: Aye, ye got that right, ye cheeky scallywag!")
    time.sleep(2)
    print("..")
    time.sleep(2)
    print ("...")
    print("")
    time.sleep(2)
    print("Guard 1: Ye know what I'd do for a kiss from the captain's parrot right now?")
    time.sleep(3)
    print("Guard 2: *laughs* What's that?")
    time.sleep(3)
    print("Guard 1: I'd walk the plank blindfolded!")
    time.sleep(3)
    print("Guard 2: *laughs* Ye're a madman, matey! That's a sure way to meet ol' Davy Jones!")
    time.sleep(3)
    print("Guard 1: Aye, but it'd be worth it for a chance with Polly!")
    time.sleep(3)
    print("Guard 2: Well, I'll drink to that!")
    print("")
    time.sleep(2)
    print("You chuckle at their banter, but your laughter quickly turns to shock as Guard 1 decides to take up the dare.")
    time.sleep(4)
    print("You watch in disbelief as he blindfolds himself and stumbles towards the edge of the pier, arms flailing wildly.")
    time.sleep(4)
    print("With a misstep, he plunges into the water with a splash, followed by a chorus of laughter from his companion, who falls to the floor in a drunken manner.")
    time.sleep(6)
    print("Seizing your chance, you sneak into the village.")
    print("")
    print("")

    time.sleep(2)

    print ("To walk around the village quietly, you need to input buttons at the correct time.")
    time.sleep(3)
    print ("If you fail to do so, the guards may be alerted to your location!")
    time.sleep(4)

    

 

    



    def sneak_sequence1():
        print("Press the correct buttons to sneak around quietly.")
        time.sleep(4)
        print("Watch out for the guards!")
        time.sleep(3)
        print("Get ready...")
        time.sleep(2)
        print ("Go!")
        print("")

        # Define a list of buttons for the player to press
        buttons = ["A", "O", "B", "F", "M"]

        # Randomize the sequence of buttons
        sequence = random.choices(buttons, k=5) #5

        for button in sequence:
            # Display the current button to press
            print("Press", button)

            # Create a thread to handle input with a time limit
            input_thread = threading.Thread(target=get_user_input, args=(button,))
            input_thread.start()
            input_thread.join(timeout=5)  # Set a time limit of 5 seconds for each button press

            # Check if the player's input matches the required button
            if user_input == button:
                print("Correct!")
            else:
                fails = fails+1
                if fails >=5:
                    print("Incorrect/Too long! A guard saw you!")
                    print("")
                    game_over()
                    return
                else:
                    print ("Incorrect!")
        print("")
        time.sleep(2)
        print("You've got to the fishmonger, who tells you that somewhere there is a prison where everyone is being kept.")
        time.sleep(3)
        sneak_sequence2()

    def sneak_sequence2():
        # Define a list of buttons for the player to press
        buttons = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        # Randomize the sequence of buttons
        sequence = random.choices(buttons, k=10) #10

        for button in sequence:
            # Display the current button to press
            print("Press", button)

            # Create a thread to handle input with a time limit
            input_thread = threading.Thread(target=get_user_input, args=(button,))
            input_thread.start()
            input_thread.join(timeout=3)  # Set a time limit of 3 seconds for each button press

            # Check if the player's input matches the required button
            if user_input == button:
                print("Correct!")
            else:
                fails = fails+1
                if fails >=5:
                    print("Incorrect/Too long! A guard saw you!")
                    print("")
                    game_over()
                    return
                else:
                    print ("Incorrect!")
        print("")
        print("You find the bakery, where you find it overrun by guards. You carry on your search for the prison.")
        time.sleep(3)
        sneak_sequence3()

    def sneak_sequence3():
        # Define a list of buttons for the player to press
        buttons = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        # Randomize the sequence of buttons
        sequence = random.choices(buttons, k=15)

        for button in sequence:
            # Display the current button to press
            print("Press", button)

            # Create a thread to handle input with a time limit
            input_thread = threading.Thread(target=get_user_input, args=(button,))
            input_thread.start()
            input_thread.join(timeout=2.5)  # Set a time limit of 3 seconds for each button press

            # Check if the player's input matches the required button
            if user_input == button:
                print("Correct!")
            else:
                fails = fails+1
                if fails >=5:
                    print("Incorrect/Too long! A guard saw you!")
                    print("")
                    game_over()
                    return
                else:
                    print ("Incorrect!")
        print("")
        print("Sneaking along, you find a big building. You seem to remember this building, as once apon a time your parents told you to never go near it.")
        time.sleep(3)
        print("")
        print("")
        sneak_sequence4()





    def sneak_sequence4():
        # Define a list of buttons for the player to press
        buttons = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        # Randomize the sequence of buttons
        sequence = random.choices(buttons, k=20)

        for button in sequence:
            # Display the current button to press
            print("Press", button)

            # Create a thread to handle input with a time limit
            input_thread = threading.Thread(target=get_user_input, args=(button,))
            input_thread.start()
            input_thread.join(timeout=2.5)  # Set a time limit of 3 seconds for each button press

            # Check if the player's input matches the required button
            if user_input == button:
                print("Correct!")
            else:
                fails = fails+1
                if fails >=5:
                    print("Incorrect/Too long! A guard saw you!")
                    print("")
                    game_over()
                    return
                else:
                    print ("Incorrect!")

        print("You get into the building. It's the prison!")
        time.sleep(1)
        print("Walking around, you hear a faint whisper.")
        print("")
        time.sleep(1)
        print("Cap'n Corkah: Matey! It's me! Corkah!")
        time.sleep(2)
        print("Cap'n Corkah: Listen up kiddo, you don't have all day.")
        time.sleep(2)
        print("Cap'n Corkah: The guard over there has the keys, so go grab em' before he wakes up!")
        time.sleep(4)
        print("Cap'n Corkah: This will be hard, so give it your full attention!")
        print("")
        print("")
        time.sleep(3)
        sneak_sequence5()




    def sneak_sequence5():
        # Define a list of buttons for the player to press
        buttons = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"]

        # Randomize the sequence of buttons
        sequence = random.choices(buttons, k=25)

        for button in sequence:
            # Display the current button to press
            print("Press :", button)

            # Create a thread to handle input with a time limit
            input_thread = threading.Thread(target=get_user_input, args=(button,))
            input_thread.start()
            input_thread.join(timeout=2.5)  # Set a time limit of 3 seconds for each button press

            # Check if the player's input matches the required button
            if user_input == button:
                print("Correct!")
            else:
                fails = fails+1
                if fails >=5:
                    print("Incorrect/Too long! The guard woke up!")
                    print("")
                    game_over()
                    return
                else:
                    print ("Incorrect!")

        print("The keys fall out of his pockets, and you grab them.")
        time.sleep(3)
        print("You walk back over to Corkah and attempt to open the doors.")
        time.sleep(4)
        print("Suddenly, you hear guards coming.")
        time.sleep(3)
        print("As the sound of footsteps grows louder, you realize the guards are closing in.")
        time.sleep(4)
        print("In a panic, you hurriedly try the keys in the lock, hoping to unlock the doors before the guards arrive.")
        time.sleep(5)
        print ("")

        print("The lock clicks open just in time, and you swing the doors wide.")
        time.sleep(3)
        print("But before you can make your escape, one of the three captains spots you and shouts to the guards.")
        time.sleep(4)
        print("The guards rush towards you with weapons drawn, ready to apprehend you.")
        time.sleep(3)
        print ("")
        print("")

        print("Corkah grabs your arm, urgency in his eyes.")
        time.sleep(3)
        print("Corkah: Quick lad, there's no time to waste. Go now, while you still can.")
        time.sleep(4)
        print("You hesitate, torn between staying to help Corkah and fleeing to safety.")
        time.sleep(4)
        print("Corkah: Don't worry about me, lad. There's something important I need to tell you before it's too late.")
        time.sleep(5)
        print ("")
        print("")
        
        print("Corkah leans in closer, his voice barely above a whisper.")
        time.sleep(4)
        print("Corkah: The toaster, lad. It's not just an ordinary appliance. It holds the key to unlocking a power greater than you can imagine.")
        time.sleep(7)
        print("Corkah: The secret lies in the fish, lad. Catching all the fish will reveal the true potential of the toaster.")
        time.sleep(4)
        print("With a nod from Corkah, you turn and flee into the night, the weight of his words heavy on your mind.")
        time.sleep(5)
        print("Go catch the last fish!")
        print("")
        
        
        pass

    def get_user_input(button):
        global user_input
        user_input = input("Enter the button: ").upper()

    def game_over():
        print("You were caught! You were clubbed by the guard, and you fall unconscious....")
        print("")
        time.sleep(1)
        sneak_sequence1()

    # Start the sneak sequence
    sneak_sequence1()








#----------------------------------------------------------------------------------------------------------------------------------
def cutscene7():
    global finn_boat_health
    global boat_defence
    global boat_health
    print("You did it! You caught the final fish!")
    time.sleep(3)
    print("As you gaze at the shimmering scales of the final fish, something extraordinary happens.")
    time.sleep(4)
    print("The toaster in your possession begins to emit a faint green auric light, growing brighter with each passing moment.")
    time.sleep(5)
    print("You watch in awe as the light envelops the toaster, casting an otherworldly glow around you.")
    time.sleep(4)
    print("Then, as suddenly as it started, the light fades away, leaving the toaster seemingly unchanged.")
    time.sleep(4)
    print("But you can't shake the feeling that something significant has occurred.")
    time.sleep(4)
    print("With the final fish in hand and the mysterious event behind you, you make your way back to the village once more.")
    time.sleep(4)
    print("")
    print("")




    print ("You steer your boat towards the village, the waves crashing against its sturdy hull.")
    time.sleep(3)
    print ("As you approach, the silhouette of the village emerges from the mist, its structures standing like sentinels against the darkening sky.")
    time.sleep(7)
    print("As your boat glides closer to the village, you notice figures standing on the shore.")
    time.sleep(5)
    print ("Three imposing figures, unmistakably the faction leaders, are gathered around a kneeling figure.")
    time.sleep(5)
    print ("It's Cap'n Corkah, bound and helpless, forced to his knees beside Captain Barnacle, who's securely tied up.")
    print("")
    print("")



    print ("Captain Barnacle: Well well well. Who do we 'ave ere?")
    time.sleep(3)
    print ("Marina Swiftwind: Seems like you've got yourself in a bit of a predicament, haven't you!")
    time.sleep(4)
    print ("Finn Marlin: Hahaha! Aye, you're in a spot of bother now, matey.")
    time.sleep(4)
    print ("Captain Barnacle: You see, lad, we've been watchin' your little escapades with great interest.")
    time.sleep(5)
    print ("Captain Barnacle: And I think you know what weer' after boy.")
    time.sleep(4)
    print ("𝘵𝘩𝘦 𝘵𝘰𝘢𝘴𝘵𝘦𝘳....")
    time.sleep(3)
    print("")
    print("")


    print ("Captain Corkah: Don't do it pal! It's not worth it!")
    time.sleep(4)
    print ("Captain Barnacle: Shut your gob Corkah!")
    time.sleep(4)
    print ("Captain Barnacle: Ya know what? I've had enough of your gob ya loud-mouthed git.")
    time.sleep(4)
    print ("Captain Barnacle unsheaths his sword, and stabs Corkah's stomach.")
    time.sleep(4)
    print ("Corkah slumps to the floor, dead.")
    time.sleep(4)
    print ("Captain Barnacle: Now he's out the way, why don't we cut to the chase?")
    time.sleep(4)
    print ("Captain Barnacle: We're after your toaster, and you'll be givin' it to us one way or another.")
    print("")
    print("")
    time.sleep(4)


    print ("Captain Barnacle: Finn Marlin, why don't you get in your boat and have a littl' fun.")
    time.sleep(4)
    print ("Finn gets into his boat, and sails it out to yours.")
    time.sleep(4)
    print ("Finn Marlin: Ready up, maggot. I'm gona tear your boat to pieces...")
    print("")
    print("")

    





    def boss_fight_1():
        global boat_health, boat_defence, finn_boat_health
        boat_health = 100
        boat_defence = 5
        finn_boat_health = 150  # Initialize the variable

        print("You mount your cannon and get ready for the upcoming battle.")
        time.sleep(1)

        def fight_input():
            global boat_health, boat_defence, finn_boat_health
            print("Do you want to:\n1. Shoot at them\n2. Cast your rod and hope for something that may help.")
            print ("")

            choice = input()
            
            if choice == "1" or choice.lower() == "shoot":
                print("You load your cannon and aim at the enemy ship.")
                boat_hitpoints = ("mast", "stern", "hull", "propeller")
                boat_hit_point = random.choice(boat_hitpoints)
                damage = random.randint(10, 20)

                print("You did", damage, "damage to the ship's", boat_hit_point, "!")
                time.sleep(1)
                print("")
                finn_boat_health -= damage  # Corrected variable name
                if finn_boat_health <= 0:  # Corrected variable name
                    print("You won the battle!")
                    time.sleep(1)
                    print("The enemy boat slowly sinks into the water, being consumed by the ocean waves...")
                    time.sleep(3)
                    print("But suddenly, from the sinking ship, Finn emerges, gasping for air.")
                    time.sleep(3)
                    print("He locks eyes with you, his face contorted with rage, as he struggles to stay afloat.")
                    time.sleep(3)
                    print("Finn Marlin: 'You may have defeated me today, but mark my words, this isn't over!'")
                    time.sleep(4)
                    print("You watch as Finn Marlin disappears beneath the waves, consumed by the ocean.")
                    time.sleep(3)
                    print("")
                    boss_fight_2()
                elif finn_boat_health > 0:  # Corrected variable name
                    print("The enemy has", finn_boat_health, "health left.")
                    time.sleep(1)
                    print("")
                    enemy_fight_input()

            elif choice == "2" or choice.lower() == "cast":
                print("You cast out a line hoping to catch something that may help.")
                time.sleep(1)
                loot_outcomes = ("boot", "wooden plank","crate", "glue", "oar")
                loot_obtained = random.choice(loot_outcomes)

                if loot_obtained in ("boot"):
                    print("You fished out a", loot_obtained, "which doesn't help!")
                    print("")
                    time.sleep(1)
                    print("")
                    enemy_fight_input()

                elif loot_obtained in ("wooden plank", "glue"):
                    boat_defence += 2
                    print("You fished out a", loot_obtained, "which increased your boat's strength so damage taken is reduced!")
                    print("")
                    time.sleep(1)
                    print("")
                    enemy_fight_input()

                elif loot_obtained == "crate":
                    boat_health += 10
                    print("You fished out a crate which had supplies to help mend your boat!")
                    print("")
                    time.sleep(1)
                    print("Your boat has", boat_health, "health left.")
                    print("")
                    enemy_fight_input()

                elif loot_obtained == "oar":
                    print("The oar gave your boat some extra speed so you get another go!")
                    print("")
                    time.sleep(1)
                    print("")
                    fight_input()

            else:
                print("Invalid input. Try again!")
                fight_input()
                
        def enemy_fight_input():
            global boat_health, boat_defence, finn_boat_health
            enemy_random_choice = random.randint(1,2)

            if enemy_random_choice == 1:
                print("The pirate aims his cannon and fires at your vessel.")
                time.sleep(1)
                boat_hitpoints = ("mast", "stern", "hull", "propeller")
                boat_hit_point = random.choice(boat_hitpoints)
                enemy_damage = random.randint(10, 30)
                real_enemy_damage = max(0, enemy_damage - boat_defence)

                print("The cannonball dealt", real_enemy_damage, "damage to your", str(boat_hit_point) + "!")
                time.sleep(1)
                print("")
                boat_health -= real_enemy_damage

                if boat_health <= 0:
                    print("Your boat was torn to pieces by the enemy fisherman, and you slowly sink into the water.")
                    time.sleep(2)
                    
                    print("Everything fades to black...")
                    time.sleep(1)
                    print("A faint voice whispers: You have to be careful out there!")
                    time.sleep(1)
                    print("Have another try!")
                    time.sleep(1)
                    print("")
                    boss_fight_1()
                elif boat_health > 0:
                    print("Your boat has", boat_health, "health remaining.")
                    time.sleep(1)
                    print("")
                    fight_input()

            elif enemy_random_choice == 2:
                print("One of the rival fishermen cast out a line.")
                time.sleep(1)
                enemy_loot_outcomes = ("boot", "plastic bag", "crate", "oar")
                enemy_loot_obtained = random.choice(enemy_loot_outcomes)

                if enemy_loot_obtained in ("boot", "plastic bag"):
                    print("They fished out a", enemy_loot_obtained, "which does nothing!")
                    time.sleep(1)
                    print("")
                    fight_input()

                elif enemy_loot_obtained == "crate":
                    finn_boat_health += 10
                    print("They fished out a crate which had supplies that healed their boat!")
                    print ("The enemy has", finn_boat_health, "health remaining.")
                    time.sleep(1)
                    print("")
                    fight_input()

                elif enemy_loot_obtained == "oar":
                    print("They fished out an oar which gave them enough speed to have another go!")
                    time.sleep(1)
                    print("")
                    enemy_fight_input()

        fight_input()
        
        
        
    

    
    def boss_fight_2():
        print("Marina Swiftwind: Impressive.")
        print("")
        time.sleep(2)
        print("Marina Swiftwind: But you're not out of the woods yet. If you think taking down Finn Marlin is the end of your troubles, you're sorely mistaken.")
        time.sleep(6)
        print("She brandishes her katana, ready for a showdown, her voice dripping with lust for the revenge of Finn Marlin.")
        time.sleep(5)
        print("Marina Swiftwind: You may have bested Finn, but you've yet to face the wrath of the sea itself.")
        time.sleep(4)
        print("As Marina Swiftwind issues her challenge, a fierce storm begins to brew on the horizon, promising a battle as tumultuous as the ocean itself.")
        time.sleep(7)
        print("")
        print("")

        print("Get ready to parry Marina Swiftwind's attacks!")
        time.sleep(4)
        print("Press the corresponding key when it appears on the screen.")
        time.sleep(4)
        print("")

        arrows = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","-","=","+",";","'","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  # Arrow keys
        successful_parrys = 0
        max_fails = 3
        fails = 0

        def input_thread():
            nonlocal successful_parrys, fails
            while successful_parrys < 30:  # Player needs to parry 30 attacks to win
                sleeprandom = random.randint(1, 3)
                time.sleep(sleeprandom)
                arrow_key = random.choice(arrows)
                print("Parry:", arrow_key)

                user_input = input("Enter the arrow key: ")
                print("Your input:", user_input)

                if user_input == arrow_key:  # Check if input matches the generated key
                    print("Parry successful!")
                    successful_parrys += 1
                else:
                    print("Failed to parry!")
                    fails += 1

                    if fails >= max_fails:
                        print("She swiped at you once more, and you fail to parry.")
                        print("You fall to the ground, and you hear a voice.")
                        print("Don't worry ya puny weed, you'll have another chance! When you defeat Finn again! AHAHAHAAHA!")
                        boss_fight_1()
                        return

        # Start the input thread
        input_thread_handle = threading.Thread(target=input_thread)
        input_thread_handle.start()

        # Wait for the input thread to finish or 20 successful parries
        input_thread_handle.join()


        print("You can see your opponent is tiring, and you get in a stab at her. She falls to the ground.")
        print("")
        time.sleep(4)
        print("Marina Swiftwind: You... You dare to strike me?!")
        time.sleep(2)
        print("Marina Swiftwind: You may have won this battle, but mark my words, this is far from over!")
        print("")
        time.sleep(5)
        print("Marina Swiftwind: We'll make sure you regret crossing paths with us, you insolent fool!")
        time.sleep(4)
        print("Drawing in her last breath, she shouts the word:")
        time.sleep(5)
        print("Marina Swiftwind: Captain!")
        time.sleep(4)
        print("...")
        time.sleep(4)
        print("")
        print("")
        boss_fight_3()
    

    

        
        
    def boss_fight_3():
        print("Captain Barnacles: Well well well.")
        time.sleep(4)
        print("Captain Barnacles: Who do we 'ave ere?")
        time.sleep(3)
        print("Captain Barnacles: So, ye think ye be worthy enough to face me, do ye?")
        time.sleep(6)
        print("Captain Barnacles: Let's settle this right here and now!")
        time.sleep(4)
        print("Captain Barnacles: Draw yer fists, ye scurvy dog, and let's see if ye have what it takes to best me!")
        print("")
        print("")
        time.sleep(7)

        def fist_fight():
            player_health = 100
            captain_health = 100

            def player_attack():
                return random.randint(10, 20)

            def captain_attack():
                return random.randint(10, 25)

            def player_block():
                return random.randint(5, 10)

            print("You encounter Captain Barnacles!")
            time.sleep(4)
            print("")
            print("Prepare for a showdown!")
            print("")
            print("")

            while player_health > 0 and captain_health > 0:
                print("\nYour Health:", player_health)
                print("Captain Barnacles' Health:", captain_health)

                # Player's turn
                print("\nIt's your turn to attack or block!")
                choice = input("Enter 'a' to attack or 'b' to block: ")

                if choice == 'a':
                    # Player attacks
                    player_damage = player_attack()
                    print("You attack Captain Barnacles, dealing", player_damage, "damage!")
                    captain_health -= player_damage
                elif choice == 'b':
                    # Player blocks
                    block_amount = player_block()
                    print("You block Captain Barnacles' attack, reducing damage taken by", block_amount)
                    player_health += block_amount  # Increase player's health by the amount blocked
                else:
                    print("Invalid choice! Try again.")

                # Check if Captain Barnacles is defeated
                if captain_health <= 0:
                    print("\nYou've defeated Captain Barnacles!")
                    break

                # Captain Barnacles' turn
                print("\nCaptain Barnacles strikes back!")
                captain_damage = captain_attack()
                print("Captain Barnacles attacks you, dealing", captain_damage, "damage!")
                time.sleep(3)
                player_health -= captain_damage

                # Check if the player is defeated
                if player_health <= 0:
                    print("\nCaptain Barnacles has bested you!")
                    break

        # Start the fist fight
        fist_fight()









        time.sleep(3)
        print("Captain Barnacles: Ye know, lad, I've sailed the seven seas, faced creatures of the deep, and fought many a battle.")
        time.sleep(4)
        print("Captain Barnacles: But never before have I seen someone like ye, standin' before me.")
        time.sleep(4)
        print("Captain Barnacles: Ye got fire in yer eyes, and a determination that's not to be underestimated.")
        time.sleep(4)
        print("Captain Barnacles: But ye see, lad, in this world, it ain't just about strength or skill.")
        time.sleep(4)
        print("Captain Barnacles: It's about wits, it's about knowin' when to strike, and when to hold back.")
        time.sleep(5)
        print("Captain Barnacles: And now, ye stand at the crossroads of fate, with me holdin' all the cards.")
        time.sleep(4)
        print("Captain Barnacles: So, what'll it be, lad? Will ye fight like a man, or will ye cower like a beaten dog?")
        time.sleep(4)
        print("Captain Barnacles: Make yer choice wisely, for it may well be yer last.")
        print("")
        print("")
        

        time.sleep(3)
        print("You feel the tension in the air as Captain Barnacles awaits your move.")
        print("")

        time.sleep(3)
        print("Suddenly, he reaches for his holster, drawing a pistol with lightning speed.")
        time.sleep(2)
        print("Before you can react, he points it straight at you and fires.")
        time.sleep(3)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(3)
        print("....")
        print("")

        time.sleep(2)

        print("Suddenly, there's a loud noise.")
        time.sleep(2)
        print("")
        print("The toaster, that was sitting next to Corkah's corpse begins shaking and glowing once more.")
        time.sleep(3)
        print("Suddenly a red sea dragon emerges from it, shattering it into peices.")
        time.sleep(3)
        print("Captain Barnacles: WHAT IN THE DEPTHS OF DAVY JONES LOCKER IS GOING ON HERE???")
        time.sleep(3)
        print("")
        print("The dragon screams, and flies down towards the player.")
        time.sleep(4)
        print("It opens it's mouth, and sprays a green mist onto the bullet wound.")
        time.sleep(3)
        print("The once bleeding fleshy bullethole closed shut, like it was never there.")
        time.sleep(3)
        print("Next, it fluttered down to Corkah's lifeless body, and repeated the same thing. The salty breath of the dragon healed his wounds, and breathed life into him.")
        time.sleep(6)
        print("As Corkah's eyes flickered open, he gasped for air, astonished at the sight of the majestic creature before him.")
        time.sleep(5)
        print("Captain Corkah: What in the ~")
        print("")
        print("")
        time.sleep(3)
        print("The dragon turns towards Captain Barnacles, its eyes blazing with fury.")
        time.sleep(4)
        print("Dragon: You have desecrated the seas far to long, human.")
        time.sleep(4)
        print("Captain Barnacles: What madness is this? You dare challenge me, foul beast?")
        time.sleep(5)
        print("He draws his sword, and rushes for the dragon.")
        time.sleep(4)
        print("With a deafening roar, it unleashes a torrent of flames, engulfing Captain Barnacles in a searing inferno.")
        time.sleep(6)
        print("Captain Barnacles screams in agony as he's consumed by the dragon's wrath, his body disappearing in a flash of fire and smoke.")
        time.sleep(7)
        print("")
        print("")
        print("The dragon turns back to you, its gaze softer now, filled with gratitude.")
        time.sleep(5)
        print("Dragon: You have shown kindness and bravery, mortal. But I must go.")
        time.sleep(5)
        print("The dragon spreads it's wings, and flies into the sunrise, screaching as it went.")
        time.sleep(4)
        print("")
        print("Captain Corkah: What the bloody hell just happened there. I need a drink.")
        time.sleep(5)
        print(".....")
        print("")
        print("")

        print("The end.")

        print ("")
        time.sleep(2)
        print ("Made by yours truly, totallybananas7.")
        time.sleep(3)
        print ("Blackjack made by DDOG")
        time.sleep(3)
        print ("Roulette (somewhat) made by breadbug (i had to do lots of debugging so it's practically mine) and for helping find bugs")
        time.sleep(3)
        print ("_name1ess_ / imaburger257 for moral support/bug helping")
        time.sleep(3)
        print ("My computing teacher for giving me the reason to start this project in the first place.")
        time.sleep(3)
        print ("ChatGPT for the rarity system (after hours of coding i still don't understand it)")

        print("Thanks for playing!")
        print("You can continue to play now.")
        print("")
        print("")
        
        
        








    boss_fight_1()
               





    
#----------------------------------------------------------------------------------------------------------------------------------


def fishdexFUNCTION():
    global fishinfishdexcount
    global remainingfishleft
    
    fishinfishdexcount = len(fishdex)
    remainingfishleft = 200 - fishinfishdexcount

    if fishinfishdexcount == 1:
        cutscene1()
    elif fishinfishdexcount == 40:
        cutscene2()
    elif fishinfishdexcount == 80:
        cutscene3()
    elif fishinfishdexcount == 120:
        cutscene4()
    elif fishinfishdexcount == 160:
        cutscene5()
    elif fishinfishdexcount == 199:
        cutscene6()
    elif fishinfishdexcount == 200:
        cutscene7()


    
    
#Cutscene 1: Tutorial completion (at 1 unique fish caught) DONE
#Cutscene 2: Cave with treasure (at 20 unique fish caught) DONE
#Cutscene 3: First battle with an oposing faction (40 unique fish caught) DONE
#Cutscene 4: Battle with kraken DONE
#Cutscene 5: player finds out Cap'n Corkah get kidnapped by the biggest of the cartels  (80 unique fish caught) DONE
#Cutscene 6: Showdown with the biggest of the fishing factions where the player finds out the only way to save Cap'n Corkah is to fish up all of the 107 unique fish fish and obtain the best gear in the game (106 unique fish caught)
#Cutscene 7: Something mysterious happens and the player gains power to save Cap'n Corkah and defeat the biggest faction (107 out of 107 unique fish caught)




def printfishdex():
    global remainingfishleft
    global fishinfishdexcount
    print("You have caught",fishinfishdexcount,"unique fish!")
    print("You are missing", remainingfishleft, "fish!")

    for item in fishdex:
        print(item, "- ✓")

    if remainingfishleft == 0:
        print("Wow! You've caught all of the fish! GG!")
    
    




def controls():
    print ("To enter the shop, say: \"shop\"")
    print ("To gamble, say: \"gamble\"")
    print ("")
    
    print ("To travel to a new area, say: \"travel\"")
    print ("To ask where you are, say: \"current location\"")
    print ("To ask what the current weather is, say: \"current weather\"")
    print ("To change the weather, say \"change weather\"")
    print ("To change your name, say \"change name\"")
    print ("")

    print ("To cast your fishing rod, say: \"cast\"")
    print ("To reel in your fishing rod, say: \"reel\"")
    print ("")
    
    print ("To check your luck, say: \"luck\"")
    print ("To check your wallet, say: \"wallet\"")
    print ("To check your fishdex, say: \"fishdex\"")
    print ("To look at all the fish in the game, say: \"fishlist\"")
    print ("")
    
    print ("To see the credits, say: \"credits\"")
    print ("To get to the main menu, say: \"menu\"")
        








def incorrectinput():
    print ("Would you like to play again? y/n")
    yesorno = str(input())
    if yesorno == "y":
        blackjack()
    else:
        incorrectinput()




def blackjack():

    def startgame():
        global pcount
        global dcount
        global cards
        global suits
        global playerscore
        global dealerscore
        global pcardcount
        global dcardcount
        global bet
        global d17
        
        d17 = False
        
        pcount = 0
        dcount = 0
        bet = 0
        cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        suits = ["♠", "♦", "♥", "♣"]
        
        playerscore = 0
        dealerscore = 0
        
        pcardcount = 0
        dcardcount = 0
        
        BetAndValidation()

    def BetAndValidation():
        global bet
        global money
        
        if money == 0:
            print("You have no money!")
            return
        
        print("Welcome to Blackjack! Please place your bet below.")
        print("You have", money, "money")
        val = False
        
        while not val:
            try:
                bet = int(input("Bet: "))
                if bet > money:
                    print("You only have", money, "money")
                else:
                    print("Bet placed!")
                    money -= bet
                    print("You now have", money, "money")
                    break
            except ValueError:
                print("Invalid input, please enter an integer")

        addplayercard()

    def addplayercard():
        global pcount
        global playerscore
        global cards
        global suits
        global pcardcount
        
        global money
        
        if pcardcount == 0:
            print("You are dealt a card:")
        if pcardcount != 1 and pcardcount != 0:
            print("The dealer deals you another card")
        
        cardnumber = random.choice(cards)
        cardsuit = random.choice(suits)

        if cardnumber in ["J", "Q", "K"]:
            playerscore += 10
        elif cardnumber == "A":
            val = False
            while not val:
                AceChoice = input("Would you like to take your ace as 11 or 1? ")
                try:
                    AceChoice = int(AceChoice)
                    if AceChoice in [1, 11]:
                        print("Accepted")
                        playerscore += AceChoice
                        break
                    else:
                        print("Invalid input, Please enter 1 or 11!")
                except ValueError:
                    print("Invalid input, Please enter 1 or 11!")
        else:
            playerscore += cardnumber
            
        print_card(cardnumber, cardsuit)
        
        time.sleep(0.5)
        pcount += 1
        pcardcount += 1

        if pcardcount == 0 or pcardcount == 1:
            addplayercard()
        elif pcardcount == 2:
            print("Your Total score is now", playerscore)
            print("-------------------------------------")
            adddealercard()
        else:
            print("Your Total score is now", playerscore)
            print("-------------------------------------")
            HitorStand()

    def adddealercard():
        global dcount
        global dealerscore
        global cards
        global suits
        global dcardcount

        if dcardcount == 0:
            print("The dealer is dealt a card:")
        else:
            print("The dealer deals themselves another card")

        cardnumber = random.choice(cards)
        cardsuit = random.choice(suits)

        if cardnumber in ["J", "Q", "K"]:
            dealerscore += 10
        elif cardnumber == "A":
            if dealerscore < 11:
                dealerscore += 11
            else:
                dealerscore += 1
        else:
            dealerscore += cardnumber

        print_card_back()  # Print dealer card face down

        time.sleep(0.5)
        dcount += 1
        dcardcount += 1

        if dealerscore >= 17 and dealerscore <= 21:  # Stop dealing cards to the dealer if score is 17 or higher
            HitorStand()
        elif dealerscore > 21:  # Dealer busts if score is over 21
            print("The dealer busted!")
            playagain()
        else:
            adddealercard()  # Continue dealing cards if score is less than 17 and not busted

    def HitorStand():
        global playerscore
        global dealerscore

        if playerscore == 21 and dealerscore == 21:
            print("You and the dealer both have Blackjack! It's a draw.")
            playagain()
        elif playerscore == 21:
            print("You have Blackjack! You win!")
            playagain()
        elif playerscore > 21:
            print("You busted! You lose!")
            playagain()
        else:
            hitorstand = input("Hit or Stand? (h/s): ").lower()
            if hitorstand == "h":
                addplayercard()
            elif hitorstand == "s":
                adddealercard()  # Proceed to dealer's turn
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")
                HitorStand()  # Repeat the prompt

    def print_card(cardnumber, cardsuit):
        if cardnumber == 10:
            print("┌─────────┐")
            print("│", cardnumber, "     │")
            print("│         │")
            print("│         │")
            print("│   ", cardsuit, "   │")
            print("│         │")
            print("│         │")
            print("│     ", cardnumber, "│")
            print("└─────────┘")
        else:
            print("┌─────────┐")
            print("│", cardnumber, "      │")
            print("│         │")
            print("│         │")
            print("│   ", cardsuit, "   │")
            print("│         │")
            print("│         │")
            print("│      ", cardnumber, "│")
            print("└─────────┘")

    def print_card_back():
        # Print a placeholder for the dealer's face-down card
        print("┌─────────┐")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("│░░░░░░░░░│")
        print("└─────────┘")

    def playagain():
        global money, bet, playerscore, dealerscore

        if playerscore <= 21 and (playerscore > dealerscore or dealerscore > 21):
            money += bet * 2  # Update the player's money only when they win
            print("You won", bet * 2, "money!")  # Display the amount won
        else:
            print("You lost the game.")
            # If the player lost, deduct the bet amount from their money
            money -= bet
            print ("You lost your bet.")
            if money < 0:
                money = 0  # Ensure the money doesn't go below zero

        Playagain = input("Would you like to play again? (yes/no): ").lower()
        if Playagain == "yes" or Playagain == "y":
            startgame()
        else:
            print("Okay! Thanks for playing!")
            print("You now have",money,"quid.")

    startgame()















def roulette():
    global money

    print("Welcome to fish-roulette!")
    print("RULES:")
    print("If you bet on a number between 1-36, you will receive 3 times your bet.")
    print("If you bet on a color, you will receive 1.25x your bet.")
    print("If you bet on 0 or 00, you will receive 2x your bet.")

    def bet_input():
        global money
        print("How much would you like to bet?")
        bet_input_str = input().strip()

        try:
            bet = int(bet_input_str)

            if bet <= 0:
                print("Invalid input! Please enter a positive integer.")
                bet_input()
            elif bet > money:
                print("You don't have that much money!")
                bet_input()
            else:
                print("You bet:", bet)
                game(bet)
        except ValueError:
            print("Invalid input! Please enter a positive integer.")
            bet_input()

    def game(bet):
        money_won = 0
        win = False
        
        possible_outcomes = (0, 00, *range(1, 37))
        possible_outcomes_colour = ("red", "black")

        print("What number or color do you want to bet on? Enter 'red', 'black', 0, 00, or a number between 1 and 36.")
        choice = input().lower()

        if choice.isdigit() and int(choice) in range(1, 37):
            if int(choice) == random.choice(possible_outcomes):
                print("Congrats! The ball landed on your number!")
                money_won = bet * 3
                win = True
            else:
                print("Sorry, the ball didn't land on your number.")
        elif choice in possible_outcomes_colour:
            if choice == random.choice(possible_outcomes_colour):
                print("The ball landed on your colour!")
                money_won = bet * 1.25
                win = True
            else:
                print("Sorry, the ball didn't land on your colour.")
        elif choice in ("0", "00"):
            if choice == random.choice(("0", "00")):
                print("Congrats! The ball landed on", choice)
                money_won = bet * 2
                win = True
            else:
                print("Sorry, the ball didn't land on", choice)
        else:
            print("Invalid choice. Please enter a valid number between 0-36, 00, red, or black.")
            game(bet)

        end(money_won, win, bet)

    def end(money_won, win, bet):
        global money

        if win:
            print("You won", money_won, "quid!")
            money += money_won
        else:
            print("You didn't win this time.")
            money -= bet

        print("You now have", money, "cash left.")
        play_again()

    def play_again():
        global money
        if money > 0:
            print("Would you like to play again? Y/N")
            pa = input().strip().lower()
            if pa in ("y", "yes"):
                bet_input()
            elif pa in ("n", "no"):
                print("Ok! Goodbye!")
            else:
                print("Invalid input. Please enter Y or N.")
                play_again()
        else:
            print("You don't have enough money.")
            print("Remember, the house always wins!")

    bet_input()
        



            

        

        

        

        

        #chooses number
        #chooses colour
            
            

        



        
    

def lottery():
    global money
    possible_winnings = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,25,25,25,25,25,25,25,50,50,50,50,100,100,100,250,250,500)

    def lottery_repeat():
        global money
        answer = input("Do you want to buy a lottery ticket? They cost £50.\n").lower()
        if answer == "yes" or answer == "y":
            if money >= 50:
                print("Ok")
                money -= 50
                amount_won = random.choice(possible_winnings)
                print("You won a total of £", amount_won, "!")
                money += amount_won
                lottery_repeat()
            else:
                print("Not enough money!")
                print("Goodbye!")

        elif answer == "no" or answer == "n":
            print("Goodbye!")

        else:
            print("Invalid input. Try again.")
            lottery_repeat()

    lottery_repeat()




def load_save_wipe():
    global money
    global name
    global rod
    global baitbag
    global baitamount
    global currentlocation
    global fishdex
    global fishinfishdexcount
    global remainingfishleft
    
    print ("Would you like to\n1. Save your current game\n2. Load a previous save\n3. Wipe your current save\n4. Exit the game\n5. Exit menu")
    loadsavewipe = input().lower()


    

    if loadsavewipe == "1" or loadsavewipe == "save":
        # Saving game state
        game_state = {
            "money" : money,
            "name" : name,
            "fishing_rod" : rod,
            "bait" : baitbag,
            "bait_amount" : baitamount,
            "location" : currentlocation,
            "caught_fish" : fishdex,
            "fishinfishdexcount" : fishinfishdexcount,
            "remainingfishleft" : remainingfishleft
        }

        with open("fishgamesavefile.txt", "w") as game_save:
            # Write the game state dictionary to the file
            json.dump(game_state, game_save)

        print ("Saved!")


        



    elif loadsavewipe == "2" or loadsavewipe == "load":
            try:
                # Load game state from file
                with open("fishgamesavefile.txt", "r") as game_save:
                    game_state = json.load(game_save)
                    # Assign loaded values to variables
                    money = game_state["money"]
                    name = game_state["name"]
                    rod = game_state["fishing_rod"]
                    baitbag = game_state["bait"]
                    baitamount = game_state["bait_amount"]
                    currentlocation = game_state["location"]
                    fishdex = game_state["caught_fish"]
                    fishinfishdexcount = game_state["fishinfishdexcount"]
                    remainingfishleft = game_state["remainingfishleft"]
                    
                print("Game loaded successfully!")
            except FileNotFoundError:
                # If the file is not found, return None
                print("No previous save file found.")
                return None






    elif loadsavewipe == "3" or loadsavewipe == "wipe":
        # Wipe game state
        game_state = {
            "money" : 0,
            "name" : None,
            "fishing_rod" : None,
            "bait" : None,
            "bait_amount" : 0,
            "location" : None,
            "caught_fish" : None,
            "fishinfishdexcount" : 0,
            "remainingfishleft" : 0
        }

        with open("fishgamesavefile.txt", "w") as game_save:
            # Write the game state dictionary to the file
            json.dump(game_state, game_save)

        print ("Goodbye! See you next time!")
        exit()





    elif loadsavewipe == "4" or loadsavewipe == "exit":
        # Confirm if the player wants to exit
        def yorn():
            yorn_input = input("Are you sure you want to quit?").lower()
            if yorn_input == "yes" or yorn_input == "y":
                time.sleep(1)
                print ("Quitting game...")
                exit()
            elif yorn_input == "no" or yorn_input == "n":
                print ("Continuing game...")
            else:
                print ("Invalid input. Try again.")
                yorn()

        yorn()



    elif loadsavewipe == "5" or "exit menu":
        print ("Happy fishing!")
        

    else:
        print("Invalid input. Try again.")
        load_save_wipe()






def all_fish():

    print("")
    print ("""    Fish Name                             Rarity         Location
    -------------------------------------------------------------------------------
    1.   Water fern                       plant          english lake
    2.   Chub                             common         english lake
    3.   Grayling                         common         english lake
    4.   Barbel                           common         english lake
    5.   Dace                             common         english lake
    6.   Trout                            common         english lake                 
    7.   Salmon                           uncommon       english lake
    8.   Three Spined Stickleback         rare           english lake
    9.   Schelly                          epic           english lake
    10.  Atlantic Sturgeon                legendary      english lake
    11.  Schneider's smelt                legendary      english lake
    12.  Loch Ness Monster                mythic         english lake

    --------------------------------------------------------------------------------
    13.  Common reed                      plant          english river
    14.  Dace                             common         english river
    15.  Gudgeon                          common         english river
    16.  Roach                            common         english river
    17.  Minnow                           common         english river
    18.  Zander                           common         english river
    19.  Ide                              uncommon       english river
    20.  Wels catfish                     rare           english river
    21.  Asp                              rare           english river
    22.  European eel                     epic           english river
    23.  Beluga sturgeon                  legendary      english river
    24.  Water hydra                      mythic         english river
    
    --------------------------------------------------------------------------------
    
    25.  Kelp                             plant          english sea
    26.  Cod                              common         english sea
    27.  Haddock                          common         english sea
    28.  Mackerel                         common         english sea
    29.  Herring                          common         english sea
    30.  Common skate                     uncommon       english sea
    31.  Thornback Ray                    rare           english sea
    32.  Conger eel                       rare           english sea
    33.  Warty Sea Cucumber               epic           english sea
    34.  Leafscale Gulper Shark           epic           english sea
    35.  Longsnout Dogfish                legendary      english sea
    36.  Kraken                           mythic         english sea

    --------------------------------------------------------------------------------
    37.  Coontail                         plant          american lake
    38.  Largemouth Bass                  common         american lake
    39.  Yellow perch                     common         american lake
    40.  Walleye                          common         american lake
    41.  Crappie                          common         american lake
    42.  Bluegill                         uncommon       american lake
    43.  Channel catfish                  rare           american lake
    44.  Northern Pike                    rare           american lake
    45.  Blue Catfish                     rare           american lake
    46.  Rock Bass                        epic           american lake
    47.  Alabama sturgeon                 epic           american lake
    48.  Alligator Garr                   epic           american lake
    49.  Devil's Hole Pupfish             legendary      american lake
    50.  Humback chub                     legendary      american lake
    51.  Bigfoot                          mythic         american lake

    --------------------------------------------------------------------------------

    52.  Lupine                           plant          american river
    53.  Common Carp                      common         american river
    54.  Channel Catfish                  common         american river
    55.  White sucker                     common         american river
    56.  Longear Sunfish                  common         american river
    57.  Rainbow Trout                    uncommon       american river
    58.  Shorthead Redhorse               uncommon       american river
    59.  Smallmouth Bass                  rare           american river
    60.  Lake Sturgeon                    rare           american river
    61.  Paddlefish                       epic           american river
    62.  Muskie                           epic           american river
    63.  Walleye                          legendary      american river
    64.  Brook Trout                      legendary      american river
    65.  Sturgeon                         legendary      american river

    --------------------------------------------------------------------------------

    66.  Vallisneria                      plant          lake malawi                    
    67.  Zebra Mbuna Cichlid              common         lake malawi
    68.  Electric Yellow Lab              common         lake malawi
    69.  Red Zebra Cichlid                common         lake malawi
    70.  Afra Cichlid                     uncommon       lake malawi
    71.  Auratus Cichlid                  uncommon       lake malawi
    72.  Electric Blue Hap                uncommon       lake malawi
    73.  Super VC-10 Hap                  rare           lake malawi
    74.  Peacock Cichlid                  rare           lake malawi
    75.  Red Empress                      rare           lake malawi
    76.  Azureus Hap                      rare           lake malawi
    77.  Blue Dolphin Cichlid             epic           lake malawi
    78.  Giraffe Hap                      epic           lake malawi
    79.  Maleri Peacock Cichlid           legendary      lake malawi
    80.  Taiwan Reef Hap                  legendary      lake malawi
    81.  Super Red Top Likoma             legendary      lake malawi

    --------------------------------------------------------------------------------
    
    82.  Lotus                            plant          river nile
    83.  Zillii Tilapia                   common         river nile
    84.  African Butter Catfish           common         river nile
    85.  Forskal's Labeo                  common         river nile
    86.  Nile Perch                       uncommon       river nile
    87.  Upside Down Catfish              uncommon       river nile
    88.  Electric Catfish                 rare           river nile
    89.  African Arowana                  epic           river nile
    90.  African Butterfish               epic           river nile
    91.  Nile Alligator                   legendary      river nile
    92.  African Sharptooth Catfish       legendary      river nile

    --------------------------------------------------------------------------------
    
    93. Posidonia                         plant          mediterranean ocean
    94. Gilthead Seabream                 common         mediterranean ocean
    95. European Sea Bass                 common         mediterranean ocean
    96. Red Mullet                        common         mediterranean ocean
    97. European Barracuda                uncommon       mediterranean ocean
    98. Dusky Grouper                     rare           mediterranean ocean
    99. Dentex                            rare           mediterranean ocean
    100. Atlantic Bluefin Tuna            epic           mediterranean ocean
    101. Ocean Sunfish                    epic           mediterranean ocean
    102. Anglerfish                       epic           mediterranean ocean
    103. Goliath Grouper                  legendary      mediterranean ocean
    104. Mobula Ray                       rare           mediterranean ocean
    105. Thresher Shark                   legendary      mediterranean ocean
    106. Sea Serpent                      mythic         mediterranean ocean

    --------------------------------------------------------------------------------
    
    107. Sea lettuce                      plant          great barrier reef
    108. Common Clownfish                 common         great barrier reef
    109. Blue Green Chromis               common         great barrier reef
    110. Powdered Blue Tang               uncommon       great barrier reef
    111. Lemon Damsel                     uncommon       great barrier reef
    112. Hippocampus Seahorse             uncommon       great barrier reef
    113. Napoleon Wrasse                  rare           great barrier reef
    114. Pallete Surgeonfish              rare           great barrier reef
    115. Yellow Tang                      rare           great barrier reef
    116. Picasso Triggerfish              epic           great barrier reef
    117. Neon Slug                        epic           great barrier reef
    118. Spinner Dolphin                  epic           great barrier reef
    119. Humphead Parrotfish              epic           great barrier reef
    120. White Spotted Pufferfish         epic           great barrier reef
    121. Queen Angelfish                  epic           great barrier reef
    122. Green Sea Turtle                 legendary      great barrier reef
    123. Red Lionfish                     legendary      great barrier reef
    124. Manta Ray                        legendary      great barrier reef

    --------------------------------------------------------------------------------
    
    125. Water Hyssop                     plant          australian river
    126. Australian Bass                  common         australian river
    127. Burramundi                       common         australian river
    128. Mary River Cod                   common         australian river
    129. Silver Perch                     uncommon       australian river
    130. Spangled Perch                   uncommon       australian river
    131. Freshwater Catfish               uncommon       australian river
    132. Jungle Perch                     rare           australian river
    133. Golden Perch                     rare           australian river
    134. Eel-Tailed Catfish               epic           australian river
    135. Giant Mud Crab                   epic           australian river
    136. Mary River Turtle                legendary      australian river
    137. Freshwater Crocodile             legendary      australian river
    138. Saxton Hale                      mythic         australian river

    --------------------------------------------------------------------------------
    
    139. Algae                            plant          antarctica
    140. Antarctic Toothfish              common         antarctica
    141. Antarctic Silverfish             common         antarctica
    142. Krill                            common         antarctica
    143. Icefish                          uncommon       antarctica
    144. Antarctic Dragonfish             uncommon       antarctica
    145. Weddell Seal                     uncommon       antarctica
    146. Antarctic Cod                    rare           antarctica
    147. Emperor Penguin                  rare           antarctica
    148. Adelie Penguin                   rare           antarctica
    149. Wandering Albatross              epic           antarctica
    150. Leopard Seal                     epic           antarctica
    151. Orca                             legendary      antarctica
    152. Blue Whale                       legendary      antarctica
    153. Colossal Squid                   legendary      antarctica
    154. Yeti                             mythic         antarctica

    --------------------------------------------------------------------------------
    
    155. Giant water lilly                plant          amazon river
    156. Neon Tetra                       common         amazon river
    157. Corydora Catfish                 common         amazon river
    158. Angelfish                        common         amazon river
    159. Electric Blue Acara              uncommon       amazon river
    160. Rummynose Tetra                  uncommon       amazon river
    161. Bristlenose Tetra                uncommon       amazon river
    162. Black Piranha                    rare           amazon river
    163. Red Bellied Piranha              rare           amazon river
    164. Arowana                          epic           amazon river
    165. Redtail Catfish                  epic           amazon river
    166. Arapaimas Gigas                  legendary      amazon river
    167. Amazonian Manatee                legendary      amazon river
    168. Capybara                         mythic         amazon river
    --------------------------------------------------------------------------------
    
    169. Mangrove branch                  plant          mangrove
    170. Mangrove Snapper                 common         mangrove
    171. Mud Skipper                      common         mangrove
    172. Mullet                           common         mangrove
    173. Fiddler Crab                     uncommon       mangrove
    174. Archer Fish                      uncommon       mangrove
    175. Halfbeak                         uncommon       mangrove
    176. Mangrove Seahorse                rare           mangrove
    177. Mangrove Jack                    rare           mangrove
    178. Spotted Garr                     rare           mangrove
    179. Pygmy Sloth                      epic           mangrove
    180. Snook                            epic           mangrove
    181. Bull shark                       legendary      mangrove

    --------------------------------------------------------------------------------
    
    182. Anubias Barteri                  plant          Your local aquatic store
    183. Duckweed                         plant          Your local aquatic store
    184. Cryptocoryne                     plant          Your local aquatic store
    185. Java fern                        plant          Your local aquatic store
    186. Moss ball                        plant          Your local aquatic store
    187. Amano Shrimp                     common         Your local aquatic store
    188. Cherry Shrimp                    common         Your local aquatic store
    189. Nerite snail                     common         Your local aquatic store
    190. Zebra Danio                      uncommon       Your local aquatic store
    191. Chilli Rasbora                   uncommon       Your local aquatic store
    192. Rainbow Guppy                    rare           Your local aquatic store
    193. Pea Puffer                       rare           Your local aquatic store
    194. Neon Tetra                       rare           Your local aquatic store
    195. Corydora Catfish                 rare           Your local aquatic store
    196. African dwarf frog               rare           Your local aquatic store
    197. Betta                            epic           Your local aquatic store
    198. Pearl Gourami                    epic           Your local aquatic store
    199. Endler's livebearers             legendary      Your local aquatic store
    200. Employee                         mythic         Your local aquatic store """)

















playerinput = ""  # Initialize playerinput variable

        

while True:
    try:
        playerinput = input().lower()
    except KeyboardInterrupt:
        print("Bruh don't try crash my game you lil bitch")

    if playerinput == "shop":
        print ("")
        shop()

    elif playerinput == "travel":
        print ("")
        airport()

    elif playerinput == "current location":
        print (currentlocation)
        
        
    elif playerinput == "luck":
        print ("")
        lucksystem(baitbag)
        
    elif playerinput == "wallet":
        print("")
        print("£", money)
        print(currentlocation, "license")
        print(rod)
        if baitbag and baitamount > 0:
            print(baitamount, baitbag[0])
        else:
            print("No bait.")
        

    elif playerinput == "cast":
        baitamount = baitamount
        if current_weather == "foggy":
            missornot = random.randint(1,5)
            if missornot == 1:
                print ("Due to it being foggy, your bobber hit the ground instead of the water!")
            else:
                weathercount = weathercount +1
                weatherchange()
                catching_system()
        else:
            weathercount = weathercount +1
            weatherchange()
            catching_system()
        
        
    elif playerinput == "controls":
        print ("")
        controls()

    elif playerinput == "gamble":
        def gamblelounge():
            global money
            
            print ("What would you like to play?")
            print ("You have",money,"pounds on you right now.")
            print ("We have blackjack, roulette and lottery. Or exit, by saying exit")
            print ("Enter your game:")
            wantedgame = str(input())
            if wantedgame == "blackjack":
                blackjack()
            elif wantedgame == "roulette":
                roulette()
            elif wantedgame == "lottery":
                lottery()

            elif wantedgame == "exit":
                print ("Goodbye!")
            else:
                print ("Please enter a valid input!")
                gamblelounge()

        gamblelounge()

            
        
    elif playerinput == "credits":
        print ("")
        print ("Made by yours truly, totallybananas7.")
        time.sleep(3)
        print ("Blackjack made by DDOG")
        time.sleep(3)
        print ("Roulette (somewhat) made by breadbug (i had to do lots of debugging so it's practically mine) and for helping find bugs")
        time.sleep(3)
        print ("_name1ess_ / imaburger257 for moral support/bug helping")
        time.sleep(3)
        print("My computing teacher for giving me the reason to start this project in the first place.")
        time.sleep(3)
        print("ChatGPT for the rarity system (after hours of coding i still don't understand it)")

        #edward hall didn't do anything

    elif playerinput == "fishdex":
        printfishdex()


    elif playerinput == "fishlist":
        all_fish()

    elif playerinput == "menu":
        load_save_wipe()


    elif playerinput == "change weather":
        weather()

    elif playerinput == "current weather":
        print ("The weather is currently:",current_weather)

    elif playerinput == "change name":
        name = str(input())
        print ("You rechanged your name to:",name)

        
    else:
        print ("Invalid input. Please try again.")
        print ("")
