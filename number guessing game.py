secret_word="vashu"
guess=""
out_ofguesses=False
num_ofGuesses=3
guess_count=0
while guess!=secret_word and not(out_ofguesses):
    if guess_count<num_ofGuesses:
        guess=input("enter :")
        guess_count=guess_count+1
    else :
        out_ofguesses=True  
if out_ofguesses:
    print("you lose")    
else:
    print("you win")
    