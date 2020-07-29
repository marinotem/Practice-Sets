x = ''
high = 100
low = 0

while x != 'c':
    guess = (high + low)//2
    print('Is your number: ' + str(guess) + '?')
    x = input("If guess is too high input 'h'. If guess is too low input 'l'. If guess is correct input 'c': ")
    if x == 'h':
        high = guess
    elif x == 'l':
        low = guess
    elif x == 'c':
        break
    else:
        print("Error, I do not understand your input. Please only use 'h', 'l', or 'c'.")
print('Your number is: ' + str(guess))