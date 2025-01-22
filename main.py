import time
from Animals.dog import Dog
from Animals.cat import Cat
from Animals.sheep import Sheep

if __name__ == "__main__":
    dyr = [
        Dog("Chewie", 2019),
        Cat("Misser", 2020),
        Sheep("Dolly", 2010)
    ]

    for i in dyr:
        print(i.get_age())
        print(i.make_sound())