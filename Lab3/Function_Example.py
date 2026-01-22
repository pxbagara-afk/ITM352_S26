# An example of creating and using your own function
# Name: Paul Bagara
# Date: January 22, 2026

def greet_user(name):
    """Function to greet the user by name which is passed in.
    In addition we want to print a welcome message that includes the day of the week.
    """
    message= "hello " + name + "!"
    return message

user_name= input("Please enter your name: ")
greeting_message= greet_user(user_name)
print(greeting_message)
