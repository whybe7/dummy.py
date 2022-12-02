class Person:
    all = []
    def __init__(self, name:str, age:int, gender:str, adress:str, cin:str):
        assert age > 0, f"{age} must be positive, >0"
        assert gender in ('male','female'), f"gender must be ethier 'male' or 'female'"
        self._name = name
        self._age = age
        self._gender = gender
        self._adress = adress
        self._cin = cin
        Person.All.append(self)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.age}, '{self.gender}', '{self.adress}', '{self.cin}')"

    def getName(self):
        return self._name
    def setName(self, newName:str):
        self._name = newName
    name = property(getName, setName)

    def getAge(self):
        return self._age
    def setAge(self, newAge:int):
        assert newAge > 0, self._age
        self._age = newAge
    age = property(getAge, setAge)

    def getGender(self):
        return self._gender
    def setGender(self, newGender:str):
        assert newGender in ('male','female'), self._gender
        self._gender = newGender
    gender = property(getGender, setGender)

    def getAdress(self):
        return self._adress
    def setAdress(self, newAdress:str):
        self._adress = newAdress
    adress = property(getAdress, setAdress)

    def getCin(self):
        return self._cin
    def setCin(self, newCin:str):
        self._cin = newCin
    cin = property(getCin, setCin)

    def nature(self):
        return f"i'm a {self.gender} Person"

    def me(self):
        return f"my name's {self.name} i'm a {self.gender} Person in {self.age} YO, i live in {self.adress}"


class Student(Person):
    def __init__(self, name:str, age:int, gender:str, adress:str, cin:str, school:str, major:str):
        super().__init__(name, age, gender, adress, cin)
        self._school = school
        self._major = major
    
    def getSchool(self):
        return self._school
    def setSchool(self, newSchool:str):
        self._school = newSchool
    school = property(getSchool, setSchool)
    
    def getMajor(self):
        return self._major
    def setMajor(self, newMajor:str):
        self._major = newMajor
    major = property(getMajor, setMajor)

    def nature(self):
        return f"i'm a {self.gender} Student"

    def me(self):
        return f"my name's {self.name} i'm a {self.gender} Student in {self.age} YO, i live in {self.adress} and i study in {self.school} at major of {self.major}"

p = Person('YB07', 18, 'male', 'Maroc', 'EE67735')
s = Student('YB07', 18, 'male', 'Maroc', 'EE67735', 'ISTIA', 'DEV')
# print(s)
# print(s.name)
# print(s.age)
# print(s.gender)
# print(s.adress)
# print(s.cin)
# print(s.school)
# print(s.major)
# print(p.me())
print(s.all)