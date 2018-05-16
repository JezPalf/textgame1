from random import randint, choice
import Enemysheet, Characterclasses



#currentCharacter = vars(Characterclasses.Ranger)
#currentEnemy =(vars(choice(Enemysheet.enemyNames)))

#print(currentCharacter.get('currentHP'))
def combat(currentCharacter, currentEnemy):
    status = 'battle'
    while status == 'battle':
        #imports a random enemy and the chosen character class
        currentEnemyHP = currentEnemy.get('currentHP')
        currentCharacterHP = currentCharacter.get('currentHP')
        #battle begins
        fight = input('You have encountered a ' + currentEnemy.get('name') + '!\nWhat do you do?\nType "R" to run or "F" to fight:\n')
        if fight.lower() == 'f':
            combat = 1
            while combat == 1:
                #attacks the enemy
                dmg = randint(1,currentCharacter.get('maxDamage'))
                print ('You did ' + str(dmg) + ' damage to the ' + str(currentEnemy.get('name')) + '.')
                print ('The ' + currentEnemy.get('name') + ' has ' + str(currentEnemyHP - dmg) + ' health remaining.\n')
                currentEnemyHP -= dmg
                #if enemy still alive, it attacks back
                if currentEnemyHP > 0:
                    enemyDamage = randint(1,currentEnemy.get('maxdamage'))
                    print('The ' + currentEnemy.get('name') + ' attacked you back for ' + str(enemyDamage) + ' damage.')
                    print('You have ' + str(currentCharacterHP - enemyDamage) + ' health remaining.\n')
                    currentCharacterHP -= enemyDamage
                    currentCharacter['currentHP'] = currentCharacterHP
                    #if you die
                    if currentCharacterHP <= 0:
                        print('You have died')
                        status = 'Dead'
                        currentCharacter['currentHP'] = currentCharacterHP
                        break
                #if you kill the enemy
                else:
                    print('You slayed the ' + currentEnemy.get('name') + '.')
                    status = 'normal'
                    currentCharacter['currentHP'] = currentCharacterHP
                    break

                #deciding to fight again after attacking at least once
                keepAttacking = input('Keep attacking?\nType "R" to run or "F" to continue fighting:\n')
                if keepAttacking == 'f':
                    print('You attack again\n')
                elif keepAttacking == 'r':
                    print('You escaped safely')
                    status = 'normal'
                    currentCharacter['currentHP'] = currentCharacterHP
                    break







        else:
            print('You escpaed safely')
            status = 'normal'
            print('\nYour status is ' + status)
            currentCharacter['currentHP'] = currentCharacterHP
            break

    else:
        print('\nYour status is "' + status + '"')
        currentCharacter['currentHP'] = currentCharacterHP

#combat(currentCharacter, vars(choice(Enemysheet.enemyNames)))
#print(currentCharacter.get('currentHP'))
#combat(currentCharacter, vars(Enemysheet.Boss))
