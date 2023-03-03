# note to self: add a GUI to this project (a way to look at this project without the terminal - everything is viewable by the screen) - use TK opensource

# =====importing libraries===========
'''This is the section where you will import libraries'''

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#I open the user file and allow student to login
usernames = []
passwords = []
with open('user.txt', 'r+') as f:
    for lines in f:
        temp = lines.strip('\n').split(', ')

        usernames.append(temp[0])
        passwords.append(temp[1])

# student enters their username
user_name = input("Please enter your username: ")

# if the students username is not in usernames list below code will print
while not user_name in usernames:
    print("Invalid username")
    user_name = input("Please enter your username: ")

# this variable tells us the position of the username in the list and so is a double check that the username is present in the list
position = usernames.index(user_name)

# request a password from user
pass_word = input("Please enter your password: ")

while pass_word != passwords[position]:
    pass_word = input("Please enter your password: ")

# welcome the user
print(f"Welcome {user_name}")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - view statistics
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        # below section makes sure only admins are able to add new users to program

        # if admin is logged in then they can add a new user (new username + new password)
        if user_name == 'admin':

            user_name1 = input("Please enter your username")
            pass_word1 = input("Please enter your password")

            pass_word_confirmation = input("Please re-enter your password to confirm")

            if pass_word1 != pass_word_confirmation:
                print("Your password entries do not match!")

            # if entered username already exists then then below error message will print
            if user_name1 in usernames:
                print("This username already exists!")

            else:

                f = open('user.txt', 'a')
                f.write(f"\n{user_name1}, {pass_word1}")
                f.close()

        else:
            print("You do not have admin privileges required to add a new user.")


    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        # prompt student to enter their new task details
        task_user = input("Please enter the username of the person who this task is assigned to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter a description of the task: ")
        task_due = input("Please enter the date this task is due: ")
        current_date = input("Please enter today's date: ")
        task_completion = "No"

        # add the new task to the tasks txt file
        with open('tasks.txt', 'a') as file:
            output = f'\n{task_user}, {task_title}, {task_description}, {task_due}, {current_date}, {task_completion}'
            print(output)
            tasks_contents = file.write(output)
            print("You have added the task!")


    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        # open and read the tasks file
        tasks_read = open('tasks.txt', 'r+')

        data = tasks_read.readlines()

        # make the output formatted nicely using a combination of special characters and new-line characters.
        for pos, line in enumerate(data):
            split_data = line.split(",")

            output = f'—————————————[{pos}]—————————————————\n'
            output += '\n'
            output += f'Assigned to:  \t\t{split_data[0]}\n'
            output += f'Task: \t\t\t\t{split_data[1]}\n'
            output += f'Description: \t\t{split_data[2]}\n'
            output += f'Due Date: \t\t\t{split_data[3]}\n'
            output += f'Assigned Date: \t\t{split_data[4]}\n'
            output += f'Task Complete?: \t{split_data[5]}\n'
            output += '\n'
            output += f'Use taskManager.py to assign each team member with appropriate tasks\n'
            output += '——————————————————————————————————\n'
            print(output)

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        # open and read the tasks file
        tasks_read = open('tasks.txt', 'r')

        data = tasks_read.readlines()

        # output will only print tasks which contain a username which matches the currently logged-in user
        for pos, line in enumerate(data):
            split_data = line.split(", ")
            if split_data[0] == user_name:
                output = f'—————————————————[{pos}]————————————————\n'
                output += '\n'
                output += f'Assigned to: \t\t{split_data[0]}\n'
                output += f'Task: \t\t\t\t{split_data[1]}\n'
                output += f'Description: \t\t{split_data[2]}\n'
                output += f'Due Date: \t\t\t{split_data[3]}\n'
                output += f'Assigned Date: \t\t{split_data[4]}\n'
                output += f'Task Complete?: \t{split_data[5]}\n'
                output += '\n'
                output += '————————————————————————————————————\n'
                print(output)

    elif menu == 's':

        # I print the length of the tasks and length of users from each file to get each total
        tasks_read = open('tasks.txt', 'r')

        data = tasks_read.readlines()

        number_of_tasks = len(data)

        print(f"The total number of tasks in this file is: {number_of_tasks}")

        users_read = open('user.txt', 'r')

        user_data = users_read.readlines()

        number_of_users = len(user_data)
        print(f"The total number of users in this file is: {number_of_users}\n")

    # this option allows user to exit menu
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # if user enters an invalid choice at the menu stage below will print and program will loop back to menu
    else:
        print("You have made a wrong choice, Please Try again")