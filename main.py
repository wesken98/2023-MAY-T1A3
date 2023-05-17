from colored import fg, bg, attr

from log_functions import add_log, remove_log, calorie_log, view_log

print(f"{attr('bold')}{attr('underlined')}Welcome to your calorie log of the day{attr('reset')}")
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
    print(f"{attr('hidden')}In try block{attr('reset')}")
#If it does not we can create
except FileNotFoundError as e:
    log_file = open(file_name, "w")
    log_file.write("Workout/food,calories\n")
    log_file.close()
    print("In except block")



def create_menu():
    print(f"{fg('yellow_4a')}{attr('bold')}Enter 1 {attr('reset')}to add a new item to your log")
    print(f"{fg('yellow_4a')}{attr('bold')}Enter 2 {attr('reset')}to remove an item from your log")
    print(f"{fg('yellow_4a')}{attr('bold')}Enter 3 {attr('reset')}to view progress of calories")
    print(f"{fg('yellow_4a')}{attr('bold')}Enter 4 {attr('reset')}to review log")
    print(f"{fg('yellow_4a')}{attr('bold')}Enter 5 {attr('reset')}to exit{attr('reset')}")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

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
        print("Invalid selection")

    input("Press enter to continue....")

print(f"\nThanks for using your log")