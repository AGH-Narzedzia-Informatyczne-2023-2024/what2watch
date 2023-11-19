def ask_about_humor():
    print("Let's talk about humor!")
    humor_response = input("How would you describe your sense of humor? ")
    print(f"Great! It sounds like you have a {humor_response} sense of humor.")

def ask_movie_preferences():
    print("\nNow, let's talk about movies.")
    genre_response = input("What movie genre do you enjoy the most? ")
    print(f"Nice choice! {genre_response} movies are always interesting.")

    watch_preference = input("Do you prefer watching movies at home or in the cinema? ")
    if watch_preference.lower() == "home":
        print("Watching movies at home is cozy and convenient!")
    elif watch_preference.lower() == "cinema":
        print("Going to the cinema is a fantastic experience!")

def main():
    print("Welcome to the Humor and Movies Questionnaire!")
    ask_about_humor()
    ask_movie_preferences()

if __name__ == "__main__":
    main()