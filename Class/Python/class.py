class owCharacter :
    def __init__ (s, Name, Health, Shield, Armour, Ultgage):
        s.Name = Name
        s.Health = Health
        s.Shield = Shield
        s.Armour = Armour
        s.Ultgage = Ultgage

    def participate(self):
        print( self.Name +  " joined the game.")

    def attack(self, otherCharacter):
        otherCharacter.Health -= self.Armour
        print(otherCharacter.Health)


Hamjji = owCharacter("Hamjji", 500, 0, 100, 1375)
Dva = owCharacter("Dva", 400, 0, 200, 1375)
Genji = owCharacter("Genji",200,0, 0, 1500)

Dva.Name = "Hana"

Dva.participate()

print(Hamjji.Armour)
Hamjji.participate()

Hamjji.attack(Dva)

# while true:

# HW1
# develop this.
# make more methods.
# mimic HamjjiPlater.py

# HW2
# make 369.py in Javascript
# don't need to make it using recursive codes.
