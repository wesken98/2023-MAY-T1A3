import csv
from colored import fg, bg, attr

def add_log(file_name):
    print(f"\n{attr('bold')}Add to log{attr('reset')}:")
    log_title = input("Please enter 'workout' or 'food' you would like to input: ")
    
    if (log_title == "workout"):
        workout = input("What kind of workout would you like to record: ")
        calorie = int(input("How many estimated calories did you burn: "))
        with open(file_name, "a") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([workout, -calorie])
    
    elif (log_title == "food"):
        food = input("What food would you like to record: ")
        calorie = int(input("How many estimated calories in your meal: "))
        with open(file_name, "a") as log_file:
            writer = csv.writer(log_file)
            writer.writerow([food, calorie])

    else:
        print("Invalid selection")


def remove_log(file_name):
    print(f"\n{attr('bold')}Remove from log{attr('reset')}:")
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

def view_log(file_name):
    print(f"\n{attr('bold')}Review log{attr('reset')}:")
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


def calorie_log(file_name):
    print(f"\n{attr('bold')}Calorie progress{attr('reset')}:")
    print("Generally, the recommended daily calorie intake is 2,000 for women and 2,500 for men")
    view_log(file_name)
    with open(file_name, "r") as log_file:
        reader = csv.reader(log_file)
        reader.__next__()
        sum = 0
        for column in reader:
            column[1] = int(column[1])
            sum = sum + (column[1])
            
    if (sum <= 2000):
        print(f"\nYou have a cumulation of {attr('bold')}{sum} {attr('reset')}calories. {attr('bold')}You are currently in a calorie deficit!{attr('reset')}")
    else:
        print(f"\nYou have a cumulation of {attr('bold')}{sum}{attr('reset')} calories. {attr('bold')}You are currently in a calorie surplus!{attr('reset')}")
            
