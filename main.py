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
    "🤖 I'm not sure what that means, but it sounds mysterious.",
    "🧠 That command flew right over my circuits!",
    "💥 Boom! That’s not a valid command, but it sure made an impact.",
    "🎩 I tip my virtual hat to your creativity.",
    "🕵️‍♂️ That’s a secret code I haven’t cracked yet.",
    "📼 Rewinding… nope, still don’t get it.",
    "🛸 That command came from another galaxy.",
    "🎲 Rolling the dice… and it landed on confusion.",
    "📡 Signal lost. Try again, Commander.",
    "🧃 That’s juicy… but not a valid command."
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
        "time": lambda: print(f"The time is {datetime.datetime.now().strftime('%H:%M')}"),
        "date": lambda: print(f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"),
        "open youtube": lambda: webbrowser.open("https://www.youtube.com"),
        "open google": lambda: webbrowser.open("https://www.google.com"),
        "chat": lambda: chatty(name),
        "help": show_help,
        "real ai": gemini_chat,
        "random": lambda: print(random.choice(fallback_responses))
    }

    for key in command_map:
        if key in command:
            command_map[key]()
            return

    print(random.choice(fallback_responses))

# === Startup ===
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