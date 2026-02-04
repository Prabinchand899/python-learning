

'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore
 whenever the game() function breaks the Hi-score.'''



def game():
    # Dummy implementation of the game function
    import random
    return random.randint(0, 1000)

current_score = game()

with open("Hi-score.txt", "r") as f:
    hi_score_str =f.read().strip() or "0"
    hi_score = int(hi_score_str)
    if current_score > hi_score:
        with open("Hi-score.txt", "w") as f:
            f.write(str(current_score))
            print("You beat the hi-score!")
    
    else:
        print("You did not beat the hi-score.")


    