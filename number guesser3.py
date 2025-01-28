import random
#From lines 3 to 36 defines the game class
class Game:
    #__init__ initialises the game with tries of 10 and range of numbers 1 to 100 and generates cpu_num
    def  __init__(self, tries=10, number_range =(1,100)):
        self.tries = tries
        self.number_range = number_range
        #number_range [0] accesses the 1 from number_range list and number_range[1] accesses the 100 from the list 
        self.cpu_num = random.randint(self.number_range[0], self.number_range[1])
        self.attempts = 0
    #Checks the user's guess and returns a hint based on the user     
    def get_hint(self,guess):
        if guess < self.cpu_num:
            return "Too Low!"
        elif guess > self.cpu_num:
            return "Too High!"
        else: 
            return "Correct"
    #Defining the main game loop which runs until the user guesses number correctly or runs out of tries. 
    def play(self):
        print("Welcome to the game!")
        input("Press any key to begin")
        
        while self.attempts < self.tries:
            self.attempts =+ 1
            #Uses input validation to ensure a correct number is entered. This uses range[0] and range[1] as number_range is a list going from 0 to 100 
            try:
                user_guess = int(input(f"Attempt {self.attempts}: Guess the number between {self.number_range[0]} and {self.number_range[1]}: "))
            except ValueError:
                print("Please enter a valid number. ")
                continue
            if user_guess == self.cpu_num:
                print("You Win!")
                break
            else:
                print(self.get_hint(user_guess))
            if self.attempts == self.tries:
                print("You lose! The correct numnber was: ", self.cpu_num)
                break

game=Game()

game.play()