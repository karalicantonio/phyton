secret = 17

guess = int(input("Pogodi broj izmedju 10 i 20: "))

if guess == secret:
    print("Bravo pogodio si tocan broj.")
else:
    print("Oprosti nisi pogodio broj , tvoj broj nije: ") +str(guess)