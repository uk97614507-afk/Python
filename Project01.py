#User                                        computer
#50-tries=1                                   67
#75-Tries=2
#62-Tries=3
#68-Tries=4
#67-Tries=5


#number guessing game

import random

com = random.randint(1, 100)
tries = 0

while True:
    tries += 1
    hum = int(input("guess your number between 1-100:-"))
    if hum == com:
        print(f"congratulations you have won in {tries} tries!")
        break
    elif hum > com:
        print("sorry wrong guss go lower!")
    elif hum < com:
        print("sorry wrong guess go higher!")