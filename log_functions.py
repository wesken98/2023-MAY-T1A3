import csv
from colored import fg, bg, attr

bold = attr('bold')
reset = attr('reset')
underline = attr('underlined')

# Asking user to add elements to the calorie log to track progress throughout the day
def add_log(file_name):
    print(f"\n{bold}Add to log{reset}:")
    log_title = input("Please enter 'workout' or 'food' you would like to input: ")

  # Can also use log_title.upper/lower  
    if (log_title == "workout" or (log_title == "Workout")):
        try:
            workout = input("What kind of workout would you like to record: ")           
            calorie = int(input("How many estimated calories did you burn: "))
            with open(file_name, "a") as log_file:
                writer = csv.writer(log_file)
                writer.writerow([workout, -calorie])
        except ValueError as e:
            print(f"\n{underline}Please input a whole numeric value{reset}")
            add_log(file_name)
   # food gives positive calories while workouts are converted to negative values 
    elif (log_title == "food" or (log_title == "Food")):
        try:
            food = input("What food would you like to record: ")
            calorie = int(input("How many estimated calories in your meal: "))
            with open(file_name, "a") as log_file:
                writer = csv.writer(log_file)
                writer.writerow([food, calorie])
        except ValueError as e:
            print(f"\n{underline}Please input a whole numeric value{reset}")
            add_log(file_name)
        

    else:
        print(f"\n{underline}Invalid selection - Please select 'workout' or 'food'{reset}")

# If mistake made in log, user has the ability to remove elements to provide accuracy but must be precise with which element
def remove_log(file_name):
    print(f"\n{bold}Remove from log{reset}:")
    view_log(file_name)
    log_title = input("Remove the workout or food you would like to remove: ")
    log_lists = []

    with open(file_name, "r") as log_file:
        reader = csv.reader(log_file)
        for row in reader:
            if (log_title != row[0]):
                log_lists.append(row)
        print(f"\nYou have successfully removed {log_title}")
    with open(file_name, "w") as log_file:
        writer = csv.writer(log_file)
        writer.writerows(log_lists)
# User is able to view elements added to the log and show calories gained/burned
def view_log(file_name):
    print(f"\n{bold}Review log{reset}:")
    with open(file_name, "r") as log_file:
        reader = csv.reader(log_file)
        reader.__next__()
        for row in reader:
            row[1] = int(row[1])
            if (row[1] <= 0):
                row[1] = -row[1]
                print(f"You burned {row[1]} calories doing {row[0]}")
            else:
                print(f"You consumed {row[1]} calories eating {row[0]}")

# Tracks calories of data recorded by users
def calorie_log(file_name):
    print(f"\n{bold}Calorie progress{reset}:")
    # Gives a guide as to the limit user is ideally aiming for based off of NHS but could be more precise depending on other factors like weight and age
    print("Generally, the recommended daily calorie intake is 2,000 for women and 2,500 for men")
    gender = input("Please enter the initial of which gender you identify with (M/F): ")
    view_log(file_name)
    with open(file_name, "r") as log_file:
        reader = csv.reader(log_file)
        reader.__next__()
        sum = 0
        for column in reader:
            column[1] = int(column[1])
            sum = sum + (column[1])
            
    if (gender == "M" or (gender == "m")): 
        if (sum <= 2500):
            print(f"\nYou have a cumulation of {bold}{sum} {reset}calories. {bold}You are currently in a calorie deficit!{reset}")
        else:
            print(f"\nYou have a cumulation of {bold}{sum}{reset} calories. {bold}You are currently in a calorie surplus!{reset}")
    elif (gender == "F" or (gender == "f")): 
        if (sum <= 2000):
            print(f"\nYou have a cumulation of {bold}{sum} {reset}calories. {bold}You are currently in a calorie deficit!{reset}")
        else:
            print(f"\nYou have a cumulation of {bold}{sum}{reset} calories. {bold}You are currently in a calorie surplus!{reset}")
    else: 
        print(f"\n{underline}Invalid selection - Please select M or F{reset}")        
