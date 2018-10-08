import random
list=['rock','paper','scissors']
play='yes'
print("welcome to tic tack toe game ")
while (play=='yes'):
    computerchoice=random.choice(list)
    print("\tCHOICES-->")
    print("\n1.ROCK\n2.PAPER\n3.SCISSORS")
    try:
             userchoice=int(input("Enter your choice :"))
             while  (userchoice<1 or userchoice>3):
                
                userguess=int(input("please select from option(1-3):\n "))
    except:
            print("Invalid choice \n ")
            userchoice=int(input("Enter again :"))
            while  (userchoice<1 or userchoice>3):
                
                userchoice=int(input("please select from option(1-3):\n "))
    Userchoice=list[userchoice-1]
    print("\n Computer's choice is :",computerchoice)
    if(Userchoice==computerchoice):
        print("\Ohh its a TIE")
    elif(Userchoice=='rock' and computerchoice=='paper'):
        print("\nSorry ! you loose")
    elif(Userchoice=='rock' and computerchoice=='scissors'):
        print("\nCongratulations! you won")
    elif(Userchoice=='paper' and computerchoice=='scissors'):
        print("\nSorry ! you loose")
    elif(Userchoice=='paper' and computerchoice=='rock'):
        print("\nCongratulations! you won")            
    elif(Userchoice=='scissors' and computerchoice=='rock'):
        print("\nSorry ! you loose")
    elif(Userchoice=='scissors' and computerchoice=='paper'):
        print("\nCongratulations! you won")        
        
    play=input("\nenter yes to play again")
    play=play.lower()
print(" \n\tExiting game")

     
