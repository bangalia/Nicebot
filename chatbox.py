from random import choice
def get_bot_response(user_response):
    bot_response_good = ["Awesome!","Woohoo!","I'm really happy to hear that"]
    bot_response_bad = ["Sorry to hear that","I hope things perk up"]

    if user_response == "good" or "great":
        return choice(bot_response_good)
    elif user_response == "bad":
        return choice(bot_response_bad) 

def bot_cool(user_interest):
    bot_cool_yes = ["A smile is the same in all languages"]
    bot_cool_no = ["Okay, talk to you soon!"]

    if user_interest == "yes":
        return bot_cool_yes
    else: 
        return bot_cool_no 
        
        


print("Hello and Welcome to Nicebot")
print("Please enter how your day has been so far")

user_response = ""

while True:
    user_response = input("How has your day been so far?:")

    if user_response == "done":
        break






