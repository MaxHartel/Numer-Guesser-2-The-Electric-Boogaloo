import random

print("""This is the random number guesser. Think of a number in your head from
1 - 100 and the program will guess what it is. If the number the program returns
is too high enter the number "1". If the number the program returns is too low
enter the number "2". If the program guesses your number enter "3".
Type "4" to continue""")

firstInput = input(" ")
firstInput = int(firstInput)


if(firstInput == 4):

    rand = 50
    x = 0
    y = 100
    count = 0
    while True:
        print(rand)
        count += 1
        inputX = input(" ")
        inputX = int(inputX)
        if(inputX == 1):
            y = rand -1
        if(inputX == 2):
            x = rand + 1
        if(inputX == 3):
            print(" It took "+ str(count) + " tries to guess your number")
            break;
        
        rand = int((x + y)/2)







    
