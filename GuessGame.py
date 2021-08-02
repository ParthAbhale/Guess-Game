import random
randNum = random.randint(1,9)
inp = None
chances = 0

print("Welcome To Number Guessing Game")

name = input("Enter Your Name: ")
print(f"Welcome {name} to Our Game of luck,Now you can test Your luck here,Hope You will enjoy the game....")

while chances<=5:
    
    inp = int(input("Guess the Number: "))
    if(inp==randNum):
        print(f"Congratulations! You guessed the right answer in {chances} chances")
        chances = chances + 1
    else:
        if(inp>randNum):
          print("You answer is less than your guess")
          chances = chances + 1
        else:
            print("You answer is more than")
            chances = chances + 1

if(inp!=randNum):
    print("you guessed the wrong answer")

