class Animal:
    def __init__(self, name, call, animal_class, mobility_type):
        self.name = name
        self.call = call
        self.animal_class = animal_class
        self.mobility_type = mobility_type

    def make_call(self):
        print(self.call)

class Enclosure:
    def decide_enclosure_type(self, animal):
        if animal.mobility_type == 'to_ground':
            return 'fence'
        elif animal.mobility_type == 'flying':
            return 'net'
        elif animal.mobility_type == 'swimming':
            return 'tank'

    def __init__(self, animal):
        self.animal = animal
        self.enclosure_type = self.decide_enclosure_type(animal)

class Zoo:
    def __init__(self, enclosures):
        self.enclosures = enclosures

    def get_all_enclosures(self):
        for enclosure in self.enclosures:
            print(enclosure.enclosure_type)

    def visit_enclosure(self, animal):
        for enclosure in self.enclosures:
            if enclosure.animal.name == animal:
                enclosure.animal.make_call()

    def get_animal_info(self, animal):
        for enclosure in self.enclosures:
            if enclosure.animal.name == animal:
                print(f'Animal Name: {enclosure.animal.name}\n'
                      f'Animal Class: {enclosure.animal.animal_class}\n'
                      f'Mobility Type: {enclosure.animal.mobility_type}\n')

    def add_animal_to_zoo(self, animal):
        self.enclosures.append(Enclosure(animal))

def create_zoo(animals):
    enclosures = []
    for animal in animals:
        enclosures.append(Enclosure(animal))
    return Zoo(enclosures)

if __name__ == '__main__':
    # Initial list of animals
    emu = Animal('emu','grrrg', 'bird', 'to_ground')
    flamingo = Animal('flamingo','bokbok', 'bird', 'flying')
    zebra = Animal('zebra','eaheah', 'mammal', 'to_ground')
    # Create zoo
    zoo = create_zoo([flamingo, emu, zebra])
    # Add new animal
    flounder = Animal('flounder', 'blubb', 'fish', 'swimming')
    zoo.add_animal_to_zoo(flounder)

