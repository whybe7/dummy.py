from Employee import Employee

class Agent(Employee):
    All = []
    def __init__(self, Matricule:int, Name:str, SalairyBase:float, ca:float):
        super().__init__(Matricule, Name, SalairyBase)
        self.__ca = ca
        Agent.All.append(self)
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.Name}', {self.Mtricule}, {self.Salairbase}, {self.Ca})"
    
    def get_ca(self):
        return self.__ca
    
    def set_ca(self,newCa:float):
        self.__ca = newCa

    Ca = property(get_ca,set_ca)

    def salairyCalculate(self):
        return self.Salairbase - ((self.Salairbase * self.IR()) + (self.Ca * 0.02))


agt = Agent(10500, 'alami', 7000, 77.5)
print(agt.All)