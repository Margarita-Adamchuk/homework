class Horse:
    hooves = 4
    population = 0

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        Horse.population += 1

    def nicker(self):
        print("Иго-го, Иго-го, Иго-го")

    def hop(self):
        print("Поскокали")
    
