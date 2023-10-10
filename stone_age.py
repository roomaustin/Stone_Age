class Charcoal:
    def __init__(self):
        self.type = "Charcoal"
    
    def ignite(self):
        return "Charcoal is burning."

class Stick:
    def __init__(self):
        self.type = "Stick"
    
    def use_as_tool(self):
        return "Using the stick as a tool."

class Stone:
    def __init__(self):
        self.type = "Stone"
    
    def strike(self):
        return "Striking with the stone."

if __name__ == "__main__":
    # Create instances of charcoal, stick, and stone
    charcoal = Charcoal()
    stick = Stick()
    stone = Stone()

    # Simulate interactions
    print(charcoal.ignite())
    print(stick.use_as_tool())
    print(stone.strike())
