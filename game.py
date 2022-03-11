"""

"""


class Room:
    """
    """
    def __init__(self, name) -> None:
        self.name = name
        self.decription = None
        self.linked_rooms = []
        self.character = None
        self.item = None
    def set_description(self, description):
        self.decription = description 

    def link_room(self, next_room, direction):
        self.linked_rooms.append((next_room, direction))

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        for room in self.linked_rooms:
            if direction in room:
                return room[0]

    def get_directions(self):
        name = self.linked_rooms
        for direction in self.linked_rooms:
            print(f"The {direction[0].name} is {direction[1]}")

        


class Item:
    """
    """
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"There is a(an) {self.name}")
        print(f"{self.description}")
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

class Character:
    """
    """
    def __init__(self, conversation, description, name) -> None:
        self.description = description
        self.conversation = conversation
        self.name = name

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        print(self.conversation)

    

class Enemy(Character):
    """
    """
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

        super().__init__(self.conversation,description ,name)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, weapon):
        if weapon == self.weakness:
            return True   
        return False

class Friend(Character):
    """
    """
    def __init__(self, name, description) -> None:
        self.name = name
        self.conversation = None
        self.description = description
        self.item = None
        super().__init__(self.conversation, description, name)
    

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def set_item(self, item):
        self.item = item
    
    def describe_the_item(self):
        print(f"{self.name} has a {self.item.get_name()}")
        print(self.item.get_description())
        print("You can take it from your friend")

