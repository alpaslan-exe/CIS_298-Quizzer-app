from us_states_quiz import run_us_states_quiz

while True:
    print("\nChoose which quiz you'd like to try:")
    print("1. Countries of the World (15 minutes)")
    print("2. Capitals of the World (20 minutes)")
    print("3. US States (5 minutes)")
    print("4. US State Capitals (10 minutes)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        print("Countries quiz not added yet.")
    elif choice == "2":
        print("Capitals quiz not added yet.")
    elif choice == "3":
        run_us_states_quiz()
    elif choice == "4":
        print("US state capitals quiz not added yet.")
    elif choice == "5":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")