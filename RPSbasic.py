import random
def collectStringInput():
    collect=input('Plese pick from P(aper), R(ock) and S(tone)\nPlayer: ')
    return collect.capitalize()
R
def generateIntegerValue():
    m=(random.randint(1,4))
    return m

def converIntegerToRPS():
    n=generateIntegerValue()
    if(n==1):
        computer_get='P'
    elif(n==2):
        computer_get='R'
    else:
        computer_get='S'
    return computer_get

def evaluateWinning(a,b):

    if a==b:
        outcome='Tie'
    elif a=='R' and b=='S':
        outcome='Rock smashes scissors. \nYou Win!'
    elif a=='R' and b=='P':
        outcome='Paper covers rock.\nComputer Wins!'
    elif a=='S' and b=='P':
        outcome='Scissors cut paper.\nYou Win!'
    elif a=='S' and b=='R':
        outcome='Rock smashes scissors.\nComputer Wins!'
    elif a=='P' and b=='S':
        outcome='Scissors cut paper.\nComputer Wins!'
    elif a=='P' and b=='R':
        outcome='Paper covers rock,\nYou Wins!'
    return outcome

a=collectStringInput()
b=converIntegerToRPS()

print("Computer's selection: ",b)
print(evaluateWinning(a,b))
