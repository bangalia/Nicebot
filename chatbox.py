from random import choice


def get_bot_response(user_response):
    bot_response_good = ["Awesome!", "Great!", "I'm happy to hear that!"]
    bot_response_bad = ["Sorry to hear that", "Oh no", "I hope things perk up"]

    if "good" in user_response:
        return choice(bot_response_good)
    elif user_response == "bad":
        return choice(bot_response_bad)
    else:
        return choice(bot_response_bad)
   

print("Hello and Welcome to Nicebot")
print("Please enter how your day has been so far")

user_response = ""

while True:
    user_response = str(input("How has your day been?"))

    if user_response == "done":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)