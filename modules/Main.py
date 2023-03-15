from contextlib import ExitStack
import time
import random
from tkinter import *
from PIL import ImageTk, Image

# Create App Layout
# Lottery = Tk()
# Lottery.geometry('800x360')
# Lottery.title('Lottery Number Generator')
# Lottery.iconbitmap("ticket.ico")

# 4 numbers per 3 slots use 3 list to store the numbers


class Existing_Lottery:
        
     def lottery_info():
        number_slot_1 = [[], [], [], []]
        number_slot_2 = [[], [], [], []]
        number_slot_3 = [[], [], [], []]
        print ("Write your last lottery numbers")
        print ("Please enter 4 numbers for the first slot")
        for i in range(4):
            number_slot_1[i] = input("Enter number: ").strip()
            if number_slot_1[i] == "" or number_slot_1[i] == " " or len(number_slot_1[i]) >= 2: 
                number_slot_1[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Please enter 4 numbers for the second slot")
        for i in range(4):
            number_slot_2[i] = input("Enter number: ").strip()
            if number_slot_2[i] == "" or number_slot_2[i] == " " or len(number_slot_2[i]) >= 2:
                number_slot_2[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Please enter 4 numbers for the third slot")
        for i in range(4):
            number_slot_3[i] = input("Enter number: ").strip()
            if number_slot_3[i] == "" or number_slot_3[i] == " " or len(number_slot_3[i]) >= 2:
                number_slot_3[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Your last lottery numbers are: {} {} {}".format(number_slot_1, number_slot_2, number_slot_3))
        
        print("Calculating...")
        time.sleep(1.5)
        print("calculating....")
        time.sleep(0.5)
        print("calculating.....")
        print("Your new numbers are: {} {} {}".format(random.choice(number_slot_1), random.choice(number_slot_2), random.choice(number_slot_3)))
        print("Good Luck, with your new numbers!")

class Lottery:
    def random_generator(): 
        a, b, c, d = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) 
        print("Random Number Generator is running!")
        print(f"Your random numbers are: {a} {b} {c} {d} \n", end="", flush=True, file=open("output.txt", "a"), sep=" ")

    def fix_generator():
        a, b, c, d = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) 
        print("Fix Number Generator is running!")
        counter = random.randint(0, 9)
        a, b , c , d = ({(a + counter) /2} , {(b + counter)/2} , {(c + counter) / 2} , {(d + counter)/2})
        print(f"Your fix numbers are: {a} {b} {c} {d} \n", end="", flush=True, file=open("fixput.txt", "a"), sep=" ")


"__init__" == "__main__ "
# Lottery() 
# Lottery.random_generator()
# Lottery.fix_generator()
Existing_Lottery.lottery_info()
# Lottery.fix_generator()
