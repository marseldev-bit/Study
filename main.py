class Car:
    """Simple car type"""
    def __init__(self, firm, model, year, owners):
        self.firm = firm
        self.model = model
        self.year = year
        self.run = 0
        self.owners = owners
    def getRunAfterOwner(self):
        self.run = 0
        getOwner = (self.owners[input('Run after which owner you want to get? ')])[0]
        index = 0
        for k, v in self.owners.items():
            self.run += v[1]
            index += 1
            if index == getOwner:
                return self.run
            
    def getCarName(self):
        return(f'{self.year} {(self.firm).title()} {(self.model).title()}')

    def getFullRun(self):
        for v in self.owners.values():
            self.run += v[1]
        return self.run
    
    def getRunInfo(self):
        print(f"{self.getCarName()} has {self.getFullRun()} kilometers on it")
    
porscheOwners = {'Jim': [1, 14000], 'Rylie': [2, 130000], 'Wincent': [3, 70000]}
porsche = Car('porsche', 'taycan', 2023, porscheOwners)

for k, v in porscheOwners.items():
    print(f"{k.title()} was {v[0]} owner of {porsche.getCarName()} and drove {v[1]} kilometers on it")
print()

porsche.getRunInfo()
print()

print(porsche.getRunAfterOwner())
# porsche.run = 14000 - Первый способ присваивания значения атрибуту по умолчанию
# porsche.giveRun(14000) - Второй способ

    
        



