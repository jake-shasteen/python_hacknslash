import sys
from character import Character
from monster import Dragon, Goblin, Troll

class Game:
    def setup( self ):
        self.player = Character()
        self.monsters = [
                Goblin(),
                Troll(),
                Dragon()
                ]
        self.monster = self.get_next_monster()

    def get_next_monster( self ):
        try:
            return self.monsters.pop(0)
        except IndexError: #no more monsters!
            return None

    def monster_turn( self ):
        if self.monster.attack():
            if self.player.dodge():
                print("The {} swipes at you, but you dodge out of the way.".format( self.monster.__class__.__name__ ))
            else:
                print("The {} swipes at you, drawing blood!".format( self.monster.__class__.__name__ ))
                self.player.hit_points -= 1
        else:
            print("The {} tries to hit you, but misses.".format( self.monster.__class__.__name__ ))


    def player_turn( self ):
        choice = input("[A]ttack, [R]est, or [Q]uit? ").lower()

        if choice in 'arq':
            if choice == 'a': #attack
                if self.player.attack(): 
                    if self.monster.dodge(): #monster dodged
                        print("The {} dodged out of the way of your {}!".format( self.monster.__class__.__name__, self.player.weapon ))
                    else: #hit
                        print("You hit the {} with your {}!".format( self.monster.__class__.__name__, self.player.weapon ))
                        self.monster.hit_points -= 1
                else: #miss
                    print("You miss with your {}.".format( self.player.weapon ))
            elif choice == 'r': #rest
                self.player.rest()
            elif choice == 'q': #quit
                sys.exit() #exit program
        else: #player did not choose an approved choice
            return self.player_turn() #loop back to choice

    def cleanup( self ):
        if self.monster.hit_points <= 0:
            self.player.experience += 1
            print("You slew the {} and gained an experience!".format( self.monster.__class__.__name__ ))
            self.monster = self.get_next_monster()


    def __init__( self ):
        self.setup()

        while self.player.hit_points and ( self.monster or self.monsters ):
            print( self.player )
            print( self.monster )
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
                print("You win!")
        elif self.monsters or self.monster:
                print("You lose!")


