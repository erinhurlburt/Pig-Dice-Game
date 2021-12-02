from random import randint

class Dice:
    faces = {1: "[ . ]", 2: "[ : ]", 3: "[: .]", 
             4:"[: :]", 5:"[:.:]", 6:"[:::]"}
    
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None
        
    def __str__(self):
        if self.value == None:
            return "Ready to roll!"
        
        elif self.value > 6:
            return "[ "+str(self.value)+" ]"
        
        else:
            return self.faces[self.value]
        
    def roll(self):
        self.value = randint(1,self.sides)
        print(self)


# In[14]:


d = Dice()
d.roll()


# In[23]:


class Pig:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def play(self):
        self.p1.score = 0
        self.p2.score = 0
        while self.p1.score < 100 and self.p2.score < 100:
            self.p1.turn()
            if self.p1.score < 100:
                self.p2.turn()
        if self.p1.score >= 100:
            print('Player 1 wins!')
        elif self.p2.score >= 100:
            print('Player 2 wins!')
        
        


# In[22]:


class Player:
    # taking turns, making choices
    
    def __init__(self, name):
        self.score = 0
        self.name = name
        
    def __str__(self):
        return str(self.name), ": ", str(self.score)
    

    def turn(self):    
        turn = 'Y'
        score = 0

        while turn == 'Y':
            if turn == 'Y':
                roll = d.roll()
                roll_value = d.value
                if roll_value == 1:
                    turn != 'Y'
                    print("You rolled a 1. You get 0 points for this round")
                    score = 0
                    break
                else:
                    score = score + roll_value
    
            if score >= 15:
                turn != 'Y'
                print('Your score is:', score)
                break

        totalscore = score + 0
        self.score += totalscore
        print ('Player 1 total score: ', self.score)
  


# In[17]:


class InteractiveMode(Player):
    
    
    def __init__(self, score):
        self.score = 0
    
    
    def turn(self):
        roll_value = d.value
        totalscore = 0
        score = 0 

        turn_choice = input('Would you like to roll? (Y/N) ')

        while turn_choice == 'Y':
            if turn_choice == 'Y':
                roll = d.roll()
                if d.value != 1:
                    score = score + d.value
                    print('Your score is: ', score)
                if d.value == 1:
                    print("You rolled a 1. You get 0 points for this round")
                    score = 0
                    turn_choice != 'Y'
                    break
                else:
                    turn_choice = input('Would you like to roll? (Y/N)')

                totalscore = score + totalscore
    
        self.score += totalscore
        print ('Player 2 total score: ', self.score)
        


# ## Part Three: Play
# 
# Create a new game object, and simulate or play a game. Methods from one of your classes should provide output that shows what is happening at each step. This is partially satisfied by the `roll` function for `Dice`. You should have additional output for showing whose turn it is, the scores after each turn, and who wins when the game is over.

# In[20]:


# play to 30 to win (for testing)

p1 = Player('Lucy')
p2 = InteractiveMode('Sally')

g1 = Pig(p1, p2)
g1.play()


# In[24]:


# play to 100 to win

p1 = Player('Lucy')
p2 = InteractiveMode('Sally')

g1 = Pig(p1, p2)
g1.play()






