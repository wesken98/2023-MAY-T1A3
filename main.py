# Some elements and headers highlighted and bolden
from colored import fg, bg, attr

from log_functions import add_log, remove_log, calorie_log, view_log

color = fg('yellow_4a')
bold = attr('bold')
reset = attr('reset')
underline = attr('underlined')

print(f"{bold}{underline}Welcome to your calorie log of the day{reset}")
print(f"An easy way of tracking your calorie intake and exertion throughout the day")

# CSV Structure
# Workout/food, calories
# Strawberries,100
# Gym,-200
file_name = "list.csv"

# Check if file exists
try:
    log_file = open(file_name, "r")
    log_file.close()
    print(f"{attr('hidden')}In try block {reset}")
#If it does not we can create
except FileNotFoundError as e:
    log_file = open(file_name, "w")
    log_file.write("Workout/food,calories\n")
    log_file.close()
    print("In except block")


# Creates a guide for user to select what action they would like to take to manipulate the log
def create_menu():
    print(f"{color}{bold}Enter 1 {reset}to add a new item to your log")
    print(f"{color}{bold}Enter 2 {reset}to remove an item from your log")
    print(f"{color}{bold}Enter 3 {reset}to view progress of calories")
    print(f"{color}{bold}Enter 4 {reset}to review log")
    print(f"{color}{bold}Enter 5 {reset}to exit{reset}")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""
# Continues program until user selects 5
while user_choice != "5":
    user_choice = create_menu()

    if(user_choice == "1"):
        add_log(file_name)
    elif(user_choice == "2"):
        remove_log(file_name)
    elif(user_choice == "3"):
        calorie_log(file_name)
    elif(user_choice == "4"):
        view_log(file_name)
    elif (user_choice == "5"):
        continue
    else: 
        print(f"\n{underline}Invalid selection - Please select a numeric value (1-5){reset}")

    input(f"\nPress enter to continue....")

print(f"\nThanks for using your log")