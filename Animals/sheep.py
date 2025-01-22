from Animals.animal import Animal
from Utils.playSound import play_sound

class Sheep(Animal):
    def __init__(self, name, year_of_birth):
        super().__init__(name, year_of_birth)
    
    def make_sound(self) -> str:
        play_sound("sheep")
        return "Baaahhh"