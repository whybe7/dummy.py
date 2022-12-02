from abc import ABC,abstractmethod
import csv
class Employee:
    __ir = 0.19
    All = []
    def __init__(self, Matricule:int, Name:str, SalairyBase:float):
        assert Matricule >= 0, f'{self.Matricule} must be positive..!' 
        assert SalairyBase >= 0 and SalairyBase >= 100, f'{self.SalairyBase} must be at least great than 100$..!' 

        self.__Matricule = Matricule
        self.__Name = Name
        self.__SalairyBase = SalairyBase
        Employee.All.append(self)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.Name}', {self.Matricule}, {self.SalairyBase})"

    def IR(self):
        return self.__ir
    
    def get_matricule(self):
        return self.__Matricule

    def set_matricule(self, newMatricile:int):
        self.__Matricule = newMatricile

    Matricule = property(get_matricule,set_matricule)

    def get_name(self):
        return self.__Name

    def set_name(self,newName):
        self.__Name = newName

    Name = property(get_name,set_name)

    def get_salairyBase(self):
        return self.__SalairyBase

    def set_salairyBase(self,newSalairy:float):
        self.__SalairyBase = newSalairy

    SalairyBase = property(get_salairyBase,set_salairyBase)

    @abstractmethod
    def salairyCalculate(self):
        pass

    @classmethod
    def instFrom_csv(cls) -> object:
        with open('Employees.csv','r') as f:
            reader = csv.DictReader(f)
            employees = list(reader)
        for emp in employees:
            Employee(Matricule=int(emp.get('Matricule')), Name=emp.get('Name'), SalairyBase=float(emp.get('SalairyBase')))

    @classmethod
    def generateCSVDI(cls):
        with open("GenEmployees.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('Matricule','Name','SalairyBase'))
            for emp in Employee.All:
                writer.writerow((emp.Matricule, emp.Name, emp.SalairyBase))
        f.close()

# 10500, "alami", 7000, "Reseau"
Employee.instFrom_csv()
emp =  Employee(10500, 'alami', 7000)
emp1 = Employee(12445, 'Aziz', 25000)
emp2 = Employee(44486, 'same', 4200)
emp3 = Employee(15790, 'lobna', 650000)
print(Employee.All)
Employee.generateCSVDI()
print(Employee.All)
# print(emp.salairyCalculate())
# print(emp.Name)
# print(emp.Matricule)
# print(emp.SalairyBase)