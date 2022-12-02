from mimetypes import init


class Animales:
    kingdom = []
    def __init__(self, name:str, age:int, genra:str, gender:str, family:str, bloodType:str, livingArea:str) -> None:
        assert genra.lower() in ('mammals', 'egganimales'), f'the genra {genra} not between (Mammals, eggAnimales)'
        assert gender.lower() in ('male', 'female'), f'the gender {gender} not between (Male, Female)'
        assert family.lower() in ('herbivorous', 'carnivorous'), f'the gender {family} not between (herbivorous, carnivorous)'
        assert bloodType.lower() in ('warm', 'cold'), f'the bllod type must be "warm" or "cold"'
        assert livingArea.lower() in ('land', 'sea'), f'the livingArea must be "land" or "sea"'
        assert age > 0 , 'age must be positive'
        self._name = name
        self._age = age
        self._genra = genra
        self._gender = gender
        self._family = family
        self._bloodType = bloodType
        self._livingArea = livingArea
        Animales.kingdom.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._name}', {self._age}, '{self._genra}', '{self._gender}', '{self._family}', '{self._bloodType}')"

    def getName(self):
        return self._name
    def setName(self, newName:str):
        self._name = newName
    name = property(getName, setName)

    def getAge(self):
        return self._age
    def setAge(self, newAge:int):
        if newAge > 0: self._age = newAge
    age = property(getAge, setAge)

    def getGenra(self):
        return self._genra
    def setGenra(self, newGenra:str):
        if newGenra.lower() in ('mammals', 'egganimales'): self._genra = newGenra
    genra = property(getGenra, setGenra)

    def getGender(self):
        return self._gender
    def setGender(self, newGender:str):
        if newGender.lower() in ('male', 'female'): self._genra = newGender
    gender = property(getGender, setGender)

    def getFamily(self):
        return self._family
    def setFamily(self, newFamily:str):
        if newFamily.lower() in ('herbivorous', 'carnivorous'): self._genra = newFamily
    family = property(getFamily, setFamily)

    def getBloodType(self):
        return self._bloodType
    def setBloodType(self, newBloodType:str):
        if newBloodType.lower() in ('warm', 'cold'): self._bloodType = newBloodType 
    bloodType = property(getBloodType, setBloodType)

    def getlivingArea(self):
        return self._livingArea
    def setlivingArea(self, newlivingArea:str):
        if newlivingArea.lower() in ('land', 'sea'): self._bloodType = newlivingArea 
    livingArea = property(getlivingArea, setlivingArea)

class Cat(Animales):
    def __init__(self, name:str, age:int, genra:str, gender:str, family:str, bloodType:str, livingArea:str, nature:str):
        super().__init__(name, age, genra, gender, family, bloodType, livingArea)
        assert nature.lower() in ('savage', 'pet'), f'the nature must be "savage" or "pet"'
        self._nature = nature
    
    def getNature(self):
        return self._nature
    def setNature(self, newNature:str):
        if newNature.lower() in ('savage', 'pet'): self._nature = newNature
    nature = property(getNature, setNature)

anm1 = Animales('zebra', 8, 'mammals', 'male', 'herbivorous', 'warm', 'land')

cat = Cat('catty', 8, 'mammals', 'female', 'carnivorous', 'warm', 'land', 'pet')

print(anm1)
print(cat.me('canada'))
