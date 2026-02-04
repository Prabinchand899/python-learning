
'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.    ''' 



import random
rule_dict  = {
    's' : -1,
    'w' : 0,
    'g' : 1
}

user = input("Enter 's' for snake, 'w' for water and 'g' for gun: ")
userch = rule_dict[user]

compch = random.choice(['s','w','g'])
print(f"Computer choose: {compch}")
comp = rule_dict[compch]

if userch == comp:
    print("It's a tie!")
elif (userch == 1 and comp == -1) or (userch == 0 and comp==1) or (userch == -1 and comp == 0):
    print("You win!")
else:
    print("you lose!")

