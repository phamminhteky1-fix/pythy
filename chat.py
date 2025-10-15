def chatty(name):
    print(f"Let's chat, {name}!")
    choice = input("Pick a number 1–10 or type 'random': ").lower()

    if choice == "random":
        choice = str(random.randint(1, 10))

    if choice == "1":
        answer = input("Cola or lemonade? ").lower()
        if answer == "cola":
            print("UGH! I HATE COLA!!")
        else:
            print("Mmh hmm, great choice.")

    elif choice == "2":
        game = input("Favorite computer game? ").lower()
        if game in ["neal", "geofs", "just dance", "infinite craft", "progressbar95"]:
            print("Oh! What a coincidence!")
        else:
            print("It’s good, but I may prefer other kinds of games.")

    elif choice == "3":
        phone = input("Android or iPhone? ").lower()
        if phone == "android":
            print("Open-sourced, moddable, cheap — a developer's dream!")
        else:
            print("I love Apple! Sleek, shiny, fast — but expensive.")

    elif choice == "4":
        best_game = input("Game you play best? ").lower()
        if best_game == "guess":
            print("I challenge you to the hard guessing game!")
        else:
            print("Good game to be pro at.")

    elif choice == "5":
        genre = input("Action or comedy movies? ").lower()
        if genre == "action":
            print("Explosions! Car chases! Over-the-top drama!")
        else:
            print("Laughs are great... unless the jokes are recycled.")

    elif choice == "6":
        goal = input("Goal this year? ")
        print(f"'{goal}' sounds amazing! Go chase it like a superhero!")

    elif choice == "7":
        flower = input("Favorite flower? ").capitalize()
        print(f"{flower}? If I had a heart, it would bloom for you.")

    elif choice == "8":
        door = input("Open secret door? ").lower()
        if door == "yes":
            print("You’re brave. Let’s solve this mystery together!")
        else:
            print("Wise choice. Some doors are better left closed...")

    elif choice == "9":
        planet = input("Which planet would you visit? ").capitalize()
        print(f"{planet}? Fascinating. I’ll prepare the space shuttle!")

    elif choice == "10":
        mood = input("Feeling chill or chaotic? ").lower()
        if mood == "chill":
            print("Vibes are mellow. Let’s ride the wave.")
        else:
            print("Chaos? Let’s flip the universe upside down!")

    else:
        print("Invalid input!")
        chatty(name)