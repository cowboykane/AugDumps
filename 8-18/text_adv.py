rooms = {
    "start": {
        "description": "> A dim hallway. Doors lead north and east.",
        "exits": {"north": "armory", "east": "library"}
    },
    "armory": {
        "description": "> Racks of rusted weapons line the walls.",
        "exits": {"south": "start"}
    },
    "library": {
        "description": "> Dusty shelves tower over you.",
        "exits": {"west": "start"}
    }
}

# Player class

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def move(self, direction, rooms):
        self.direction = direction
        self.rooms = rooms
    def show_inventory(self):
        pass



print("Type 'quit' to exit.\n")

inventory = []
player = Player("Kane", "start")
current_room = "start"

while True:

    print(rooms[current_room]["description"])
    
    start_choice = input("Select an exit: ").lower().strip()
    print()
    
    if start_choice == "quit" or start_choice == "q":
        print("Exiting game...")
        break
    
    if start_choice in rooms[current_room]["exits"]:
            destination = rooms[current_room]["exits"][start_choice]
            print(f"You enter the {destination}.\n")
            current_room = destination
    else:
        print("You can't go that way!\n")
        
   
        
