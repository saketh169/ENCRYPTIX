# ROCK,PAPER,SCISSORS
import random 

userscore=0
compscore=0

def draw_game(user,comp):
    print("USER'S CHOICE IS",user)
    print("COMPUTER'S CHOICE IS",comp)
    print("       ")
    print("GAME IS DRAW")
    
def check_win(win,user,comp,userscore,compscore):
    print("USER'S CHOICE IS",user)
    print("COMPUTER'S CHOICE IS",comp)
    print("       ")
    if win==True:
        print("YOU WIN THE GAME")
        userscore+=1
        
    else:
        print("COMPUTER WIN THE GAME")
        compscore+=1
        
    return userscore, compscore
        
    
def play_game(user,comp,userscore,compscore):
    
    win=False #initialization
    if user==comp:
        draw_game(user,comp)
    
    elif user=="rock":
        # paper , scissor
        if comp=='paper':
            win=False
        else:
            win=True
        
    elif user=="paper":
        # rock , scissor
         if comp=='scissors':
             win=False
         else: 
             win=True
         
    else:
         # rock , paper
         if comp=='rock':
             win=False
         else:
             win=True
       
    
    if user != comp:
        userscore, compscore = check_win(win, user, comp, userscore, compscore)
        
    return userscore, compscore
   
def comp_choice():
    choices=[ "rock","paper","scissors"]
    comp=random.choice(choices)
    return comp
  

def user_choice():
    user=input("ENTER USER'S CHOICE:")
    print("       ")
    while(user !="rock" and user !="paper" and user !="scissor"):
        print("invalid choice")
        user=input("ENTER CHOICE AGAIN:")
        print("     ")
    return user
    
 
user=user_choice()
comp=comp_choice()

userscore, compscore = play_game(user, comp, userscore, compscore)
print("       ")
       
print("USER SCORE:" ,userscore)
print("COMP SCORE:" ,compscore)

print("       ")
    
choice=input("Do you want to play the game again:")
if choice=="yes":
    while choice != "no" :
        
         user=user_choice()
         comp=comp_choice()
         userscore, compscore = play_game(user, comp, userscore, compscore)
         print("       ")
         print("USER SCORE:" ,userscore)
         print("COMP SCORE:" ,compscore)
         print("       ")
         choice=input("Do you want to play the game again:")  
         print("       ")
else:
    print("Thanks for playing")