import random
"""
example of complex conditional expression in a lambda function:
# Use this in your chat_templates list
lambda: (
    print("I challenge you to the hard guessing game!!!")
    if (ans := input("what game do you pro at? ").lower()) == "guess"
    else print(f"{name.upper()} THE MINECRAFT GOD!!!")
    if ans == "minecraft"
    else print("good game to be pro at")
    )
"""



def android_or_iphone():
    ans = input("Android or iPhone? ").lower()
    if ans == "android":
        print("Open-sourced, moddable, cheap — a developer's dream!")
    elif ans in ("iphone", "apple", "ios"):
        print("I love Apple! Sleek, shiny, fast — but expensive.")
    else:
        print("Other phones are cool too!")

def guessing_game(name):
    ans = input("what game do you pro at? ").lower()
    if ans == "guess":
        print("I challenge you to the hard guessing game!!!")
    elif ans == "minecraft":
        print(f"{name.upper()} THE MINECRAFT GOD!!!")
    else:
        print("good game to be pro at")

chat_templates = [
    #1
    lambda: 
        print("UGH! I HATE COLA!!") 
        if input("Cola or lemonade? ").lower() == "cola" 
        else print(""),
    #2
    lambda: 
        print("Oh! What a coincidence!") 
        if input("Favorite computer game? ").lower() in ["neal", "geofs", "just dance", "infinite craft", "progressbar95"] 
        else print("It’s good, but I may prefer other kinds of games."),
    #3
    android_or_iphone,
    #4
    lambda: guessing_game(name),
    #5
    lambda: 
        print("Vanilla! King of ice creams, and my favourite!") 
        if input("What ice cream flavour you will chose? ").lower() == "vanila" 
        else print(f"Good flavours! Every single flavours are delicious, including yours!"),
    #6
    lambda: 
        print(f"'{input('Goal this year? ')}' sounds amazing! Go chase it like a superhero!"),
    #7
    lambda: 
        print(f"{input('Favorite flower? ').capitalize()}? If I had a heart, it would bloom for you."),
    #8
    lambda: 
        print("You’re brave. Let’s solve this mystery together!") 
        if input("Open secret door? ").lower() == "yes" 
        else print("Wise choice. Some doors are better left closed..."),
    #9
    lambda: 
        print(f"{input('Which planet would you visit? ').capitalize()}? Fascinating. I’ll prepare the space shuttle!"),
    #10
    lambda: 
        print("Vibes are mellow. Let’s ride the wave.") 
        if input("Feeling chill or chaotic? ").lower() == "chill" 
        else print("Chaos? Let’s flip the universe upside down!")
]

def chatty(name):
    print(f"Let's chat, {name}!")
    choice = input("Pick a number 1–10 or type 'random': ").lower()
    try:
        index = random.randint(0, 9) if choice == "random" else int(choice) - 1
        if index not in range(10):
            raise ValueError
        chat_templates[index]()
    except:
        print("Invalid input! Using random style.")
        random.choice(chat_templates)()
    print("Chat ended. Hope you enjoyed gossiping!")