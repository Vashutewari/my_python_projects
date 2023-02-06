import random


def game(comp, you):
    if comp == you:
        return None
    elif comp == "rock":
        if you == "scissor":
            return False
        elif you == "paper":
            return True
    elif comp == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True
    elif comp == "scissor":
        if you == "rock":
            return True
        elif you == "paper":
            return False


# print("enter rock,paper,scissor")

rand_num = random.randint(1, 3)

if rand_num == 1:
    comp = "rock"
elif rand_num == 2:
    comp = "paper"
else:
    comp = "scissor"
you = input("enter :  rock , paper, scissor : ")
a = game(comp, you)
print("comp entered", comp)
print("you entered ", you)
if a == None:
    print("game is tie")
elif a==True:
    print("you win")
else:
    print("you lost,Comp win!!!")
