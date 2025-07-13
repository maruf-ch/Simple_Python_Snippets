import os
import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)
    
    hiscore = 0
    if os.path.exists("hiscore.txt"):
        with open("hiscore.txt") as f:
            content = f.read()
            if content.strip():
                hiscore = int(content)
    
    print(f"Your score: {score}")
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("New high score! 🎉")
    else:
        print(f"High score remains: {hiscore}")
    
    return score

game()
