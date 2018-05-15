
class character:
    def __init__(self, name, level,  currentHP, maxHP, maxDamage, attackSpeed, status):
        self.name = name
        self.level = level
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.maxDamage = maxDamage
        self.attackSpeed = attackSpeed
        self.status = status



Barbarian = character ('Barbarian', 5, 300, 300, 100, 2, 'normal')
Asassin = character ('Assasin', 5, 180, 180, 1000, 6, 'normal')
Ranger = character ('Ranger', 5, 240, 240, 100, 4, 'normal')

characterlist = [Barbarian, Asassin, Ranger]


#for x in characterlist:
    #print(vars(x))
#print(vars(Barbarian))
