from random import randint
import time
add=randint(1,6)+randint(1,6)
global previousguess
previousguess=-1
def ToCompareGuess(userguess):
    if (add==userguess):
        print("\n\tCONGRATULATIONS ",Username ,"you win the game")
        time.sleep(5)
        exit()
        
    else :
        print("\n\OOPs",Username ,"YOU GUESS THE WRONG SUM ")
        time.sleep(2)
       
    
def Input():
     global previousguess
     try:
         userguess=int(input("Guess the value of sum  :"))
         while (userguess==previousguess):
             print("You entered same value again!")
             userguess=int(input("Try another value   :"))
        
         while  (userguess<2 or userguess>12):
            print("Not possible !!!! Sum should be in range(2-12)\n ")
            userguess=int(input("Please guess the proper value of sum : "))
        
     except:
        print("Sum can be an integer number only \n guess the sum again")
        userguess=int(input("enter the value of sum"))
        while  (userguess<2 or userguess>12):
             print("Not possible !!!! Sum should be in range(2-12)\n ")
             userguess=int(input("Please guess the proper value of sum  :"))
     previousguess=userguess
     ToCompareGuess(userguess)
        
    

print ("\n Welcome to the 'NUMBER GUESS' game  ")
Username =input("\nEnter your Name  : ")
print (Username ,"\n\n\t<Here are  few rules :>")
print("1.The computer will roll a pair of dice and add the numbers that appears on the dice\n2.you have guess the numbers")
print("3.If you guess the correct sum you will win the game.Each wrong choice deduct your one chance")
print ("4.You will be given 4 chances ")
time.sleep(4)
print ("So lets begin the game. \n\n\tALL THE BEST",Username)
time.sleep(4)
for i in range (4):
    print ("\nChance ",i+1)
    Input()
print("\nSORRY YOU ARE OUT OF CHANCES \n\t COMPUTER WINS THE GAME ")
print ("\nThe sum was --> ",add)
    
    

        
    

