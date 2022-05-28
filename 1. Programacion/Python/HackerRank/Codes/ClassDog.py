class Dog:
    kind = "Canine"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)
        
x = Dog("Fico")
y = Dog('Rufo')

x.add_tricks("Roll over")
y.add_tricks("sit")
