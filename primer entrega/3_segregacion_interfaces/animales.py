from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def respirar(self) -> str:
        pass

    @abstractmethod
    def comer(self) -> str:
        pass

    @abstractmethod
    def dormir(self) -> str:
        pass

# class Carnivoro(Animal):
#     @abstractmethod
#     def respirar(self):
#         pass

#     @abstractmethod
#     def comer(self):
#         pass

#     @abstractmethod
#     def dormir(self):
#         pass

class Carnivoro(Animal):
    def __init__(self):
        super().__init__()


class Herviboro(Animal):
    def __init__(self):
        super().__init__()


class Perro(Carnivoro):
    def __init__(self, animalito):
        self.animalito = animalito

    def respirar(self):
        print(f"Yo el perro {self.animalito} respiro por la nariz.")

    def comer(self):
        print(f"Yo el perro {self.animalito} como carne.")

    def dormir(self):
        print(f"Yo el perro {self.animalito} duermo todos los dias.")

class Vaca(Herviboro):
    def __init__(self, animalito):
        self.animalito = animalito

    def respirar(self):
        print(f"Yo la vaca {self.animalito} respiro por la nariz.")

    def comer(self):
        print(f"Yo la vaca {self.animalito} como plantas.")

    def dormir(self):
        print(f"Yo la vaca {self.animalito} duermo todos los dias.")


