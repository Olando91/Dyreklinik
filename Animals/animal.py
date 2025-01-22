from abc import ABC, abstractmethod
from datetime import datetime

class Animal(ABC):
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def get_age(self):
        age = datetime.now().year - self.year_of_birth
        return f"Navn: {self.name}, alder: {age}"
        
    @abstractmethod
    def make_sound(self):
        pass
            