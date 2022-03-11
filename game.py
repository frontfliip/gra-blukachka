"""
A game module
"""


class Room:
    """
    A class that represents a room
    """

    def __init__(self, name) -> None:
        """
        Parameters
        ----------
        name : str
           The name of the room
        """
        self.name = name
        self.decription = None
        self.linked_rooms = []
        self.character = None
        self.item = None

    def set_description(self, description) -> None:
        """
        Adds the description of the room
        """
        self.decription = description

    def link_room(self, next_room, direction) -> None:
        """
        Adds the closest rooms to the list
        """
        self.linked_rooms.append((next_room, direction))

    def set_character(self, character) -> None:
        """
        Adds the character into the room
        """
        self.character = character

    def set_item(self, item) -> None:
        """
        Adds the item
        """
        self.item = item

    def get_character(self) -> object:
        """
        Returns the character of the room
        """
        return self.character

    def get_item(self) -> object:
        """
        Returns the item of the room
        """
        return self.item

    def move(self, direction) -> object:
        """
        Changes the room
        """
        for room in self.linked_rooms:
            if direction in room:
                return room[0]

    def get_directions(self) -> str:
        """
        Prints all closest rooms and its directions
        """
        for direction in self.linked_rooms:
            print(f"The {direction[0].name} is {direction[1]}")


class Item:
    """
    A class that represents the class
    """

    def __init__(self, name) -> None:
        """
        Parameters
        ----------
        name : str
           The name of the item
        """
        self.name = name
        self.description = None

    def set_description(self, description) -> None:
        """
        Adds the description of the item
        """
        self.description = description

    def describe(self) -> str:
        """
        Prints the full description of the item
        """
        print(f"There is a(an) {self.name}")
        print(f"{self.description}")

    def get_name(self) -> str:
        """
        Returns the name of the item
        """
        return self.name

    def get_description(self) -> str:
        """
        Returns the description of the item
        """
        return self.description


class Character:
    """
    Parent class for all characters in the game
    """

    def __init__(self, conversation, description, name) -> None:
        """
        Parameters
        ----------
        conversation : str
            The replica of the character
        description : str
            The description of the character
        name : str
            The name of the character
        """
        self.description = description
        self.conversation = conversation
        self.name = name

    def describe(self) -> str:
        """
        Prints the full description of the character
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self) -> str:
        """
        Prints the replica of the character
        """
        print(self.conversation)


class Enemy(Character):
    """
    A class that represents the enemy
    """

    def __init__(self, name, description) -> None:
        """
        Parameters
        ----------
            The description of the enemy
        name : str
            The name of the enemy
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

        super().__init__(self.conversation, description, name)

    def set_conversation(self, conversation) -> None:
        """
        Adds a replica of the enemy
        """
        self.conversation = conversation

    def set_weakness(self, weakness) -> None:
        """
        Adds the weakness of the enemy
        """
        self.weakness = weakness

    def fight(self, weapon) -> bool:
        """
        Shows if the you win or lose
        """
        if weapon == self.weakness:
            return True
        return False


class Friend(Character):
    """
    A class that represents the friend
    """

    def __init__(self, name, description) -> None:
        """
        Parameters
        ----------
            The description of the friend
        name : str
            The name of the friend
        """
        self.name = name
        self.conversation = None
        self.description = description
        self.item = None
        super().__init__(self.conversation, description, name)

    def set_conversation(self, conversation) -> None:
        """
        Adds the replica of the friend
        """
        self.conversation = conversation

    def set_item(self, item) -> None:
        """
        Adds the item for the friend
        """
        self.item = item

    def describe_the_item(self) -> str:
        """
        Prints the description of the friend
        """
        print(f"{self.name} has a {self.item.get_name()}")
        print(self.item.get_description())
        print("You can take it from your friend")
