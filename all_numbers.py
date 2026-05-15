import pandas as pd
import time
import sys
import os
import csv

BOLD = '\033[1m'
END = '\033[0m'

def file_exists(file_path = "numbers_head/brain_extension.csv"):
    """Return file_path or None"""
    if os.path.exists(file_path):
        return file_path
    else:
        return None

def typewriter_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() # Move to a new line at the end

def intro_text():
    typewriter_print("Welcome to all the numbers in your head.")
    time.sleep(1)

def make_csv(file_path = "numbers_head/brain_extension.csv"):
    # make csv at location file_path with only column names number and meaning
    df = pd.DataFrame(columns=['number', 'meaning'])
    df.to_csv(file_path, index=False)


def first_time():
    print("")
    typewriter_print("Woohoo, seems like it's your first time here.")
    typewriter_print("I'm going to make a file called brain_extension.csv")
    typewriter_print("DON'T DELETE IT! That's where we'll store all these numbers.")
    print("")
    typewriter_print(". . . ", 0.1)
    print("")
    typewriter_print("I know they're in your head anyway, but still.")
    make_csv()

def is_num_in_brain(df, num):
    # check if there is already an entry with number "num"
    # return meaning list or empty list
    if num in df['number'].values:
        meaning = df.loc[df['number'] == num, 'meaning'].values
        return meaning
    return []

def add_row_and_save(df, num, meaning, file_path):
    df = pd.concat([df, pd.DataFrame({'number': [num], 'meaning': [meaning]})], ignore_index=True)
    df.to_csv(file_path, index=False)

def new_input(df,file_path):
    print("")
    num = int(input("Type your number and then press enter! Only digits :p \n"))
    print("")
    # check if it exists already
    num_in_brain = is_num_in_brain(df, num)
    if len(num_in_brain)>0:
        typewriter_print(f"Looks like you already have {num} in your computer brain.")
        if len(num_in_brain) == 1:
            typewriter_print(f"Seems like {num} is {num_in_brain[0]}")
            print("Do you want to:")
            print("(1) Replace the old one.")
            print("(2) Nevermind, I just want to keep the old one. Guess I added this already.")
            print("(3) Let's keep both!")
            repetition_choice = input("Pick one and hit enter.")
            if repetition_choice == "1":
                typewriter_print(f"So true. And now you're saying that {num} is . . . ?")
                meaning = input("(Give a little description and then hit enter. \n")
                # first remove the other one
                df = df[df['number']!= num] 
                add_row_and_save(df, num, meaning, file_path)
                return

            elif repetition_choice=="2":
                print("Okay sounds good. Let's try again if you want.")
                print("whoopsies need to fix this part! redirects wrong way oopsies")
                return

            else:
                typewriter_print(f"Yes we love multiple meanings. And now you're saying that {num} is also . . . ?")
                meaning = input("(Give a little description and then hit enter. \n")
                add_row_and_save(df, num, meaning, file_path)
                return
        else:
            typewriter_print("Woah, this number means so many things. Seems like it's: ")
            for item in num_in_brain:
                print(item)
            print("")
            typewriter_print("I'll give you so many options. Do you want to:")
            print("(1) Only keep the newest meaning you're about to give me.")
            print("(2) Overwrite one of them only.")
            print("(3) Let's keep all of em! Yay.")
            repetition_choice = input("Pick one and hit enter.")
            
            if repetition_choice == "1":
                typewriter_print(f"So true. And now you're saying that {num} is . . . ?")
                meaning = input("(Give a little description and then hit enter. \n")
                # first remove the other one
                df = df[df['number']!= num] 
                add_row_and_save(df, num, meaning, file_path)
                return

            elif repetition_choice == "2":
                print ("Which one do you want to overwrite. Type (1) if it's the first line I printed, etc.")
                overwrite_choice = input()
                delete_meaning = num_in_brain[int(overwrite_choice)-1]
                df = df[~(df['number']== num & df['meaning']== delete_meaning)]

                add_row_and_save(df, num, meaning, file_path)
                return

            # miiltiple meanings
    else:
        print("")
        typewriter_print(f"Cool, and {num} is . . .? \n")
        meaning = input("(Give a little description and then hit enter. \n")
        add_row_and_save(df, num, meaning, file_path)
        return


def add_number():
    print("")
    print("")
    typewriter_print(f"{BOLD}YAS! Let's add some #s.{END}")
    
    if file_exists() is None:
        first_time()
        # now ready to continue on
    
    file_path = file_exists()
    # need to pull in full csv so that for each new number, we can check if it's already there. maybe use df
    df = pd.read_csv(file_path)
    new_input(df, file_path)
    typewriter_print("Wahoo! Consider your number logged in your external brain!")



def view_numbers(file_path= "numbers_head/brain_extension.csv"):
    typewriter_print("LOL I'll make a more fun way to scroll through and search for numbers but for now you just get them all!")
    if file_exists() is None:
        print("LOL you haven't even added any numbers yet!!")
    else:
        df = pd.read_csv(file_path)
        for index, row in df.iterrows():
            print(f"Number: {row['number']}, Meaning: {row['meaning']}")

if __name__ == "__main__":
    add_or_review = intro_text()
    keep_looping=True
    while keep_looping:
        typewriter_print("Would you like to:")
        print("(1) Add new numbers.")
        print("(2) Review your numbers")
        print("")
        time.sleep(0.5)
        add_or_review = input("Type 1 or 2 to continue, and then press enter \n \n ")

        if add_or_review=="1":
            add_number()
            typewriter_print("Do you wanna:")
            print("(1) Add another number. You're so strong.")
            print("(2) Let's look at all my beautiful numbers and meanings instead!")
            print("(3) I'm done!!!!! Get me out of here. ")
            choice = input()

            if choice == "1":
                add_number()

            elif choice == "2":
                view_numbers()

            else: 
                typewriter_print("Okay thank u for contributing to your epic external brain!")
                keep_looping = False
                


        else:
            print("")
            view_numbers()
            print ("Okay yay you've seen your numbers... do you want to start again (1) or exit (2)")
            choice = input()
            if choice == "1":
                keep_looping = True
            elif choice == "2":
                keep_looping = False
