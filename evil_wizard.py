# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def health_potion(self):
        self.health += 20
        print(f"{self.name} drinks a health potion and heals for 20 points! Current health: {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=35)
                
    def special_1(self,opponent):
        """ Shield Bash - warrior attacks with their shield and then raises it to reduce incoming damage."""
        print(f"{self.name} attacks {opponent.name} with their shield for 15 damage!")
        print(f"{self.name} raises their shield.")
        opponent.health -= 15
        if opponent.health > 0:
            opponent.regenerate()
            print(f"{opponent.name} attacks for 8 damage.")
            self.health -= 8
            if self.health > 0:
                battle(self, opponent)
            else:
                print(f"{self.name} had been defeated.")
        elif opponent.health <= 0:
            print("The wizard {opponent.name} has been defeated by {self.name}!")        
    
    def special_2(self, opponent):
        """rage - does more damage but also takes damage from recklessness"""
        opponent.health -= 50
        self.health -= 20
        print(f"{self.name} attacks with reckless abandon, doing 50 damage to {opponent.name}, but taking 20 points to themselves.")
        
    
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
     
    def special_1(self, opponent):
        """firebolt"""
        opponent.health -= 35
        print(f"{self.name} launches a firebolt for 35 damage.")
        
    def special_2(self, opponent):
        """lightening bolt"""
        opponent.health -= 30
        print(f"{self.name} shoots lightening at {opponent.name} and does 30 damage.")
        

# Create Rogue class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)
        
    def special_1(self, opponent):
        """bow shot"""
        opponent.health -= 30
        print(f"{self.name} shoots their bow for 30 damage.")
        
    def special_2(self, opponent):
        """backstab"""
        opponent.health -= 30
        print(f"{self.name} attacks from behind for 30 damage.")
        
    

# Create Assassin class 
class Assassin(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health=120, attack_power=25)
        
    def special_1(self, opponent):
        """Ambush"""
        opponent.health -= 30
        print(f"{self.name} attacks from the shadows for 30 damage.")
        
    def special_2(self, opponent):
        """double attack - attacks with two daggers"""
        opponent.health -= 40
        print(f"{self.name} attacks {opponent.name} twice for 20 damage each.")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue") 
    print("4. Assassin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Rogue(name)  
    elif class_choice == '4':
        return Assassin(name) 
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_1(wizard)
        elif choice == '3':
            player.special_2(wizard)
        elif choice == '4':
            player.health_potion()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()