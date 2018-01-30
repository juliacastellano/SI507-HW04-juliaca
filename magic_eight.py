import random

answers=["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes","Most likely", "Outlook good", "Yes" , "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good","Very doubtful"]

def ask_user():
    user_input = ""

    while user_input != "quit":
        user_input = input("What is your question?")

        if user_input[-1] == "?":
            print(random.choice(answers))
        elif user_input == "quit":
            print("Quitting now")
            break
        else:
            print("I'm sorry, I can only answer questions.")



ask_user()
# Write code that checks if user input is a question (i.e., ends in a ‘?’) and, if not,
# prints “I’m sorry, I can only answer questions.” (or something similar)
# Edit the program so that it keeps asking for user input until the user inputs “quit”
