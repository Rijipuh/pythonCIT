class owTank :
    def __init__(self, Name, Health):
        self.Name = Name
        self.Health = Health

    def hi(self):
        print("Hi my name is " + self.Name)


class owMainTanker(owTank) :
    def __init__ (self, Name, Health, Shield):
        owTank.__init__(self, Name, Health)
        self.Shield = Shield


Rein = owMainTanker("Reinhardt" , 500, 2000)
Orisa = owMainTanker("Orisa", 400, 900 )

print(Rein.Shield)
print(Rein.Name)
# Rein.hi("Reinhardt")
Orisa.hi()
Rein.hi()
