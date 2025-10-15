from packageManager import ensure_package, cleanup_packages

print("Setting up...")

# Ensure required packages
ensure_package("wikipedia")
ensure_package("google-generativeai")

# Now safe to import
import datetime
import webbrowser
import wikipedia
import random
from chat import chatty
from game import guessing_game
from aiFunctions import gemini_chat

# Fallback responses
fallback_responses = [
    "📚 According to my huge amount of dictionaries, I have no idea what you mean.",
    "🎨 Creativity is endless, but to use it against me, it's a big NEVER (Except if you are chatting with Gemini).",
    "👽 Hullo, are you an alien? Please use my language.",
    "🤖 We never accept computer languages in this shell, except if you are changing me."
]

def show_help():
    print("\n📘 HELP MENU")
    print("- time / date: Show current time or date")
    print("- wikipedia [topic]: Get a quick summary")
    print("- open google / open youtube: Launch predefined sites")
    print("- open webpage: Open any URL (include https://)")
    print("- chat: Casual conversation")
    print("- guessing game: Play a guessing game (easy or hard)")
    print("- real ai: Talk to Gemini, Google's AI")
    print("- help: Show this menu")
    print("- exit / quit: Close the assistant\n")

def respond(command, name):
    command = command.lower()

    if any(bye in command for bye in ["bye", "exit", "quit", "goodbye", "see you"]):
        return "exit"

    if "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            print(f"\n📚 Wikipedia summary:\n{summary}\n")
        except:
            print("Couldn't find that topic.")
        return

    if "open webpage" in command:
        webbrowser.open(input("Enter full URL (include https://): "))
        return

    if "guessing game" in command:
        mode = input("Type 1 for hard mode, 0 for easy mode: ")
        guessing_game(hard=(mode == "1"))
        return

    command_map = {
        "time": 
            lambda: 
            print(f"The time is {datetime.datetime.now().strftime('%H:%M')}"),
        "date": 
            lambda: 
            print(f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"),
        "open youtube": 
            lambda: 
            webbrowser.open("https://www.youtube.com"),
        "open google": lambda: webbrowser.open("https://www.google.com"),
        "chat": 
            lambda: 
            chatty(name),
        "help": show_help,
        "real ai": gemini_chat,
        "random error":
            lambda: 
            print(random.choice(fallback_responses)),
        "do you know clippy":
            lambda:
            print("Yes! He's friendly and helpful!"),
        "do you know siri":
            lambda:
            print("Yes! But her soul is getting replaced by ChatGPT"),
        "do you know chatgpt":
            lambda:
            print("Yes! But I may rather chat with Gemini."),
        "do you know cortana":
            lambda:
            print("Yes! She is Clippy's facebook friend, but she is too young to die (Rest in peace!)")
    }
    for key in command_map:
        if key in command:
            command_map[key]()
            return

    print(random.choice(fallback_responses))
    print('So, what about smashing that "help" command?')

# === Startup ===
if __name__ == "__main__":
    print("All functions installed and set up.")
    name = input("👋 Hello! What's your name? ")
    print(f"Nice to meet you, {name}! I'm Pythy, your assistant.")
    show_help()

    while True:
        user_command = input(">> ")
        if respond(user_command, name) == "exit":
            print(f"👋 Bye for now, {name}! Pythy signing off. Stay curious!")
            cleanup_packages()
            break