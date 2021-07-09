class Car:
    def __init__(self, color, type, company, age, year, owner):
        self.color = color,
        self.type = type,
        self.company = company,
        self.age = age,
        self.year = year,
        self.owner = str(owner)

    def compile(self):
        print("Aayush " + "bought a " + self.type + "Nissan " + "truck " + "in " + str(self.age))


    


carOne = Car("red", "truck", "Nissan", 20, 2001, "Aayush")

carOne.compile()

