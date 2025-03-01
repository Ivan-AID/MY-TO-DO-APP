print("Welcome to my todo app")

tasks = []
# an infinite loop is created using the "while loop"
while True:
    # user input
    user_choice = int(input("Choose from the options below:\n"
    "1. Add\n"
    "2. View\n"
    "3. Edit\n"
    "4. Delete\n"
    "5. Clear\n"
    "6. Exit\n"))

    if user_choice == 1:
        # add task 
        user_task = input("Enter task:\n")
        tasks.append(user_task)
        print(f"{user_task} added succesfully!!!")
    elif user_choice == 2:
        if not tasks:
            print("List is empty!!!" )
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task}")
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        print("List succesfully cleared!!!")
        tasks.clear()
    elif user_choice == 6:
        print("Exitting the program")
        exit()
    else:
        print("Invalid option, please try again!!!")


