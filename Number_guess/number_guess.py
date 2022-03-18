import random

print("Enter lower number: ")
a=int(input())
print("Enter upper range number: ")
b=int(input())

print("You have three chances to guess.")

for i in range(3):
    print("Please enter the your guess number: ")
    d = int(input())

    g = random.randint(a, b)
    if d==g:
        print("You won the game in {} guess".format(i+1))
        break
    elif i<2:
        print("Try again: ")

    else:
        print("You have exceeded the guess limit number")







