

'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore
 whenever the game() function breaks the Hi-score.'''



def game():
    # Dummy implementation of the game function
    import random
    print("You are playing a game>>>")
    return  random.randint(0, 1000)
    

score = game()



with open("HI-score.txt", "r") as f:
    hiscore = f.read()
    print(f"Your score: {score}")
    print(f"Hi score: {int(hiscore)}")
    if (hiscore==""):
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    else:
        if int(hiscore)>score:
            print("You didn't beat the hi score!")
        elif int(hiscore)==score:
            print("Your didn't beat the hi score!")
        else:
            with open("Hi-score.txt" , "w") as f:
                f.write(str(score))
                print("Congratulations!, you beat the hi score.")



   