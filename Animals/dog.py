from Utils.playSound import play_sound
from Animals.animal import Animal



class Dog(Animal):
    def __init__(self, name, year_of_birth):
        super().__init__(name, year_of_birth)
    
    def make_sound(self) -> str:
        play_sound("dog")
        return"Vuf vuf"