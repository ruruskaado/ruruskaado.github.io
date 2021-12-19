# First creation (v1.0): 14/05/2021 - 15/05/2021
# Modified: 16/05/2021 - 19/12/2021
# v2.0 (aka "The Day When I Properly Learned About Lists"): 19/12/2021

import random
import time

startValue = ''
result = ''
count = ''
symbols = ['+', '-', '*', '/', '**', '//', '%', '^']
counting = 0
pathing = ''
listed = []
numbers = '+0'



print("Disorder of Operations Machine")
time.sleep(2)
print("Calculates stuff without using the order of operations.\nWork in progress.")
time.sleep(2)
print("=======================================================\n")

time.sleep(3)
while startValue.isnumeric() == False:
    startValue = int(input("Please enter a starting value.\n> "))
    if startValue.isnumeric() == False:
        print("Sorry, try again.")

while result.isnumeric() == False:
    result = int(input("Please enter the end velue.\n>"))
    if count.isnumeric() == False:
        print("Sorry, try again.")

while count.isnumeric() == False:
    count = input("How many operations will be used in the final value?\n(Note: this number includes starting value.)\n>")
    if count.isnumeric() == False:
        print("Sorry, try again.")

print("For this next input, 'your numbers' should be written with math operators in front of a number, for example:\n+2     (plus two)\n-2     (minus two)\n*2     (times two)\n/2     (divided by two)\n**2    (to the power of two)\n//2    (floored by two. google it)\n%2     (modulo two)\n^2     (I forgot what this does but it works sooo)")
while counting == 0:
    print("Please enter your numbers, separated by new lines, or type q if you're ready:\n")
    numbers = input()
    numbers = numbers.replace(' ', '')

    if numbers != "q" and (numbers.startswith(tuple(symbols)) == True and (numbers[1:].isnumeric() == True or (numbers[0:1].replace('*', '', 1).replace('/', '', 1) + numbers[2:]).isnumeric() == True)):
        listed.append(numbers)
    elif numbers != "q" and (numbers.startswith(tuple(symbols)) == False):
        print("Please put a symbol at the start your input.")
    elif numbers == 'q':
        answer = input(str(listed) + "\n\nIs this correct? (y/n): ")
        if answer == 'y':
            break
        else:
            print("error")
    else:
        print("errorororor")
    


while 0 == 0:
    pathway = random.sample(listed, count)
    while counting < count and pathing != result:
        if counting == 0:
            path = str(startValue) + pathway[counting]
            pathing = eval(path)
        else:
            path = path + pathway[counting]
            pathing = eval(str(pathing) + pathway[counting])

        counting = counting + 1
        if counting == count:
            print('')
            counting = 0
            break

        print(path, "=", pathing)

        if pathing == result:
            print("\nWe found it!\n", path, "=", result)
            break
        else:
            None
