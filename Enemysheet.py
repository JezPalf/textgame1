
class enemy:
    def __init__(self, name, currentHP, maxHP, maxdamage):
        self.name = name
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.maxdamage = maxdamage

Troll = enemy('Troll', 250, 250, 100)
Orc = enemy('Orc', 400, 400, 100)
Goblin = enemy('Goblin', 100, 100, 100)
Mage = enemy('Mage', 150, 150, 100)
Boss = enemy('Boss', 1000, 1000, 100)


enemyNames = [Troll, Orc, Goblin, Mage, Boss]

#for x in enemyNames:
#    print(vars(x))
#print(vars(Boss))

