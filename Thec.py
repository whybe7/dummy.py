from Employee import Employee

class Thec(Employee):
    All = []
    def __init__(self, Matricule: int, Name: str, SalairyBase: float, Speciality: str):
        super().__init__(Matricule, Name, SalairyBase)
        __Speciality = Speciality
        Thec.All.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.Name}', {self.Mtricule}, {self.Salairbase}, '{self.Speciality}')"

    def get_speciality(self):
        return self.__Speciality
    
    def set_speciality(self,newSpeciality:str):
        self.__Speciality = newSpeciality

    Speciality = property(get_speciality,set_speciality) 

    def salairyCalculate(self):
        return self.Salairbase - (self.Salairbase * self.IR())


t = Thec(10500, 'alami', 7000, 'Resau')