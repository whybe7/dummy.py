from datetime import *
# initilaise earth revelution constent to function 
# for calculate outher planets revolution periods and orbit of the sun
#the thuerd low of kipler 
# Te^2/Re^3 = Tp^2/Rp^3 with: Te^2/Rp^3 = 1
#
constEarth = 365.26
def revPlanet(revPeriod: float) -> float:
    if revPeriod == 365:
        return 365.26
    return revPeriod / 365.26
     
def isLeap(year: int):
    if year < 1 and  year > 9999 :
        return year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def FormatDate(year: int,month: int,day: int):
    if  (year < 1 and year > 9999) and (month < 1 and month >= 12) and (day < 1 and day >= 31):
        return False
    return True

def EarthAge(year: int,month: int,day: int):
    
    if FormatDate(year,month,day):
        if len(str(day)) == 4 :
            blanck = day
            day = year
            year = blanck 
        return ((date.today()- date(year,month,day)).days) / revPlanet(revPeriod=365) # true value of revolution earth 
    return 1

def MercuryAge(EarthAge:float):
    # rev_merc = 87.97d
    return EarthAge / revPlanet(87.97)

def VenusAge(EarthAge:float):
    # rev_ven = 244.7d
    return EarthAge / revPlanet(244.7)

def MarsAge(EarthAge:float):
    # rev_mrs = 1.88y <=> 366.14d
    global constEarth
    return EarthAge / revPlanet(1.88*constEarth)

def JupiterAge(EarthAge:float):
    # rev_jup = 11.86y <=> 4331.9836d
    global constEarth
    return EarthAge / revPlanet(11.86*constEarth)

def SaturnAge(EarthAge:float):
    # rev_jup = 29.46y <=> 10760.5596d
    global constEarth
    return EarthAge / revPlanet(29.46*constEarth)

def UranusAge(EarthAge:float):
    # rev_jup = 84.01y <=> 30685.4926d
    global constEarth
    return EarthAge / revPlanet(84.01*constEarth)

def NeptuneAge(EarthAge:float):
    # rev_jup = 164.79y <=> 60191.1954d
    global constEarth
    return EarthAge / revPlanet(164.79*constEarth)

def PlutoAge(EarthAge:float):
    # rev_jup = 248.59y <=> 90799.9834d
    global constEarth
    return EarthAge / revPlanet(248.59*constEarth)
try:
    birthday = input("enter your birthday: ").split('-',3)
    earthage = EarthAge(int(birthday[0]),int(birthday[1]),int(birthday[2]))

    print(' '*15+"┌───────────────┐")
    print(" "*15+"│ Universal Age │")
    print('┌'+'─'*14+"┴──────┬────────┴"+'─'*17+'┐')
    print('│ your Earth age is'+' '*3+'│'+' '*16+f'{earthage:.2f} Y.O │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Mercury age is'+' '*1+'│'+' '*16+f'{MercuryAge(earthage):.2f} Y.O │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Venus age is'+' '*3+'│'+' '*16+f'{VenusAge(earthage):.2f} Y.O │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Mars age is'+' '*4+'│'+' '*16+f'{MarsAge(earthage):.2f} Y.O  │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Jupiter age is'+' '*1+'│'+' '*16+f'{JupiterAge(earthage):.2f} Y.O  │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Saturn age is'+' '*2+'│'+' '*16+f'{SaturnAge(earthage):.2f} Y.O  │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Uranus age is'+' '*2+'│'+' '*16+f'{UranusAge(earthage):.2f} Y.O  │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Neptune age is'+' '*1+'│'+' '*16+f'{NeptuneAge(earthage):.2f} Y.O  │')
    print("├"+"─"*21+'┼'+"─"*26+"┤")
    print('│ your Pluto age is'+' '*3+'│'+' '*16+f'{PlutoAge(earthage):.2f} Y.O  │')
    print("└"+"─"*21+'┴'+"─"*26+"┘")
    
except Exception:
    print(f"Date format Error: ['YYYY','MM <= 12','DD <= 31'] -> {birthday}")
except IndexError as idxe:
    print(f'\t-> {idxe}')
except ValueError as ve:
    print(f'\t-> {ve}')
except NameError as ne:
    print(f'\t-> {ne}')


