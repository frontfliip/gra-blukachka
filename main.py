import game

kitchen = game.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = game.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = game.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")

okurok = game.Item("okurok")
okurok.set_description("It is putler in youth")
dining_hall.set_item(okurok)

ben = game.Friend("Ben", "A friendly dog that is ready to help you")
ben.set_conversation("Hi, I'm Ben. Nice to meet you")
ben.set_item(book)
kitchen.set_character(ben)

current_room = kitchen
backpack = []

defeated = 0 
dead = False

while dead == False:

    print("\n")
    print(current_room.name)
    print("-"*20)
    print(current_room.decription)
    current_room.get_directions()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        if type(inhabitant).__name__ == "Enemy":
            inhabitant.describe()
        else:
            inhabitant.describe()
            if inhabitant.item is not None:
                inhabitant.describe_the_item()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - chec
        # k whether there is one!
        if inhabitant is not None:
            print("\n")
            inhabitant.talk()
        else:
            print("\n")
            print("There is no one to talk with")
    elif command == "fight":
        if inhabitant is not None:
            if type(inhabitant).__name__ == "Friend":
                print("\n")
                print("You don't have to fight with your friend")
            else:
                # Fight with the inhabitant, if there is one
                print("\n")
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("\n")
                        print("Hooray, you won the fight!")
                        defeated += 1 
                        current_room.character = None
                        if defeated == 2:
                            print("\n")
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("\n")
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("\n")
                    print("You don't have a " + fight_with)
        else:
            print("\n")
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("\n")
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("\n")
            print("There's nothing here to take!")
    elif command == "take from friend":
        if inhabitant is not None:
            if type(inhabitant).__name__ == "Friend" and inhabitant.item is not None:
                print("\n")
                print("You put the " + inhabitant.item.get_name() + " in your backpack")
                backpack.append(inhabitant.item.get_name())
                inhabitant.item = None
            elif type(inhabitant).__name__ == "Enemy":
                print("\n")
                print("It is your enemy!")
            else:
                print("\n")
                print("There is nothing to take")
        else:
            print("\n")
            print("There is no one in here or there is nothing to take")
    else:
        print("\n")
        print("I don't know how to " + command)