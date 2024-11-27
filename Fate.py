import time

class Saber:
    def __init__(self):
        self.hp = 1200
        self.atk = 200
        self.energy = 10
    
    def attack(self):
        self.energy -= 2
        print("Excalibur!")

    def hurt(self,saber_enemy):
        self.enemy = saber_enemy
        if self.enemy == "Archer":
            self.hp -= 300
        else: self.hp -= 200

    def dodge(self):
        self.energy -= 1


class Archer:
    def __init__(self):
        self.hp = 800
        self.atk = 300
        self.energy = 12

    def attack(self):
        self.energy -= 2
        print("I'm Bone Of Sword!")
    
    def hurt(self,archer_enemy):
        self.enemy = archer_enemy
        if self.enemy == "Saber":
            self.hp -= 200
        elif self.enemy == "Archer":
            self.hp -= 300
        else: self.hp -= 200

    def dodge(self):
        self.energy -= 1

                            
class Berserker:
    def __init__(self):
        self.hp = 1800
        self.atk = 200
        self.energy =8
        
    def attack(self):
        self.energy -= 2
        print("Crying Warmonger")
    
    def hurt(self,berserker_enemy):
        self.enemy = berserker_enemy
        if self.enemy == "Saber" or self.enemy == "Berserker":
            self.hp -=200
        else: self.hp -= 300

    def dodge(self):
        self.energy -= 1

####################################################################

def main():
    print("*"*70)
    time.sleep(4)
    print("######################################")
    print("####  Welcome to Fate_Stay_Night  ####")
    print("######################################")
    time.sleep(6)

    print("\nRoles Table:")
    roles = ["Saber","Archer","Berserker"]
    print("Saber: (hp)1200 (atk)200 (energy)10\n") 
    print("Archer: (hp)800 (atk)300 (energy)12\n")
    print("Berserker: (hp)1800 (atk)200 (energy)8\n")
   
    time.sleep(4)
    print("*"*70)

    print("(Player1)PLease select your role:\n")
    print("1.Saber | 2.Archer | 3.Berserker")
    choice1 = int(input("num: "))
    match choice1:
        case 1:
            player1 = Saber()
        case 2:
            player1 = Archer()
        case 3:
            player1 = Berserker()

    print(f"OK, Player1 selects {roles[choice1-1]}.")
    time.sleep(2)
    print("*"*70)

    print("\n(Player2)Please select your role:\n")
    print("1.Saber | 2.Archer | 3.Berserker")
    choice2 = int(input("num: "))
    match choice2:
        case 1:
            player2 = Saber()
        case 2:
            player2 = Archer()
        case 3:
            player2 = Berserker()
    print(f"OK, Player2 selects {roles[choice2-1]}.")
    
    player1_enemy = roles[choice2-1]
    player2_enemy = roles[choice1-1]
    time.sleep(2)
    print("*"*70)

####################################################################

    print("READY?")
    time.sleep(2)
    print("GO!")
    time.sleep(2)
    print("*"*70)

    action1 = '3'
    action2 = '3'
    while player1.hp > 0 and player2.hp > 0:
        current_role = roles[choice1-1]
        print(f"\nIt's (p1){current_role}'s turn")
        time.sleep(1)
        print(f"\n(p1){current_role}'s current state:\n")
        print('hp:',player1.hp,'|','energy:',player1.energy)
        time.sleep(2)
        action1 = input("Action (1.attack|2.dodge|3.skip) : ")

        if action1 == '1':
            if player1.energy == 0:
                print("(p1)Energy not enough, skip.")
            else:
                player1.attack()
                if action2 == '1':
                    time.sleep(1)
                    player1.hurt(player1_enemy)
                    print("*"*70)
                    print("(p1)Auch!")
                    time.sleep(1)
                    print("*"*70)
                    print("(p1)hp: ",player1.hp)
                    time.sleep(2)

        elif action1 == '2':
            if player1.energy == 0:
                print("(p1)Energy not enough, skip.")
            else:
                player1.dodge()
                if action2 == '1':
                    time.sleep(1)
                    print("*"*70)
                    print("(p1)You can't hurt me, haha.")
                    time.sleep(2)
                else:
                    time.sleep(1)
                    print("*"*70)
                    print("(p1)F**k, I waste a skill.")
                    time.sleep(2)
        
        elif action1 == '3':
            if action2 == '1':
                player1.hurt(player1_enemy)
                time.sleep(1)
                print("*"*70)
                print("(p1)Auch!")
                time.sleep(2)
            pass
        else: 
            time.sleep(1)
            print("*"*70)
            print("(p1)ERROR, skip automaticlly")
            time.sleep(2)


        current_role = roles[choice2-1]
        time.sleep(2)
        print("*"*70)
        print(f"\nIt's (p2){current_role}'s turn")
        time.sleep(1)
        print(f"\n(p2){current_role}'s current state:\n")
        print('hp:',player2.hp,'|','energy:',player2.energy)
        time.sleep(2)
        action2 = input("Action (1.attack|2.dodge|3.skip) : ")

        if action2 == '1':
            if player2.energy == 0:
                print("(p2)Energy not enough, skip.")
            else:
                player2.attack()
                if action1 == '1':
                    player2.hurt(player2_enemy)
                    time.sleep(2)
                    print("*"*70)
                    print("(p2)Auch!")
                    time.sleep(2)
                    print("*"*70)
                    print("(p2)hp: ",player2.hp)
                    time.sleep(2)
        
        elif action2 == '2':
            if player1.energy == 0:
                print("(p2)Energy not enough, skip.")
            else:
                player2.dodge()
                if action1 == '1':
                    time.sleep(1)
                    print("*"*70)
                    print("(p2)You can't hurt me, haha.")
                    time.sleep(2)
                else: 
                    time.sleep(1)
                    print("*"*70)
                    print("(p2)F**k, I waste a skill.")
                    time.sleep(2)

        elif action2 == '3':
            if action1 == '1':
                player2.hurt(player2_enemy)
                time.sleep(1)
                print("*"*70)
                print("(p2)Auch!")
                time.sleep(2)
            pass
        else:
            time.sleep(1)
            print("*"*70)
            print("(p2)ERROR, skip automaticlly")
            time.sleep(2)
        
        if player1.energy == 0 and player2.energy == 0:
            break
    
    print("*"*70)
    print("__GAME OVER__")
    time.sleep(2)
    if player1.hp <= 0:
        print("player2 wins!!!")
    elif player2.hp <= 0: 
        print("player1 wins!!!")
    else: print("No winner.")

main()
