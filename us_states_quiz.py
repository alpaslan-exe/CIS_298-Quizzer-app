import csv
import time
from colorama import Fore, init

init(autoreset=True)

def load_states():
    states = []

    with open("state_capitals.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) > 0:
                states.append(row[0].strip())

    return states


def run_us_states_quiz():
    states = load_states()

    if not states:
        print("No states were loaded.")
        return

    all_states = set()
    for state in states:
        all_states.add(state.lower())

    correct_answers = set()

    time_limit = 300
    start_time = time.time()

    print("\n=== US States Quiz ===")
    print("Start typing states now! (type 'exit' to quit)\n")

    while True:
        elapsed_time = time.time() - start_time
        time_left = int(time_limit - elapsed_time)

        if time_left <= 0:
            print("\nTime is up!")
            break

        print(f"Time left: {time_left} seconds")
        answer = input("Enter a state: ").strip().lower()

        if answer == "exit":
            print("Exiting quiz...")
            break

        if answer in all_states:
            if answer in correct_answers:
                print("You already got that one.\n")
            else:
                correct_answers.add(answer)
                print("Correct!\n")
        else:
            print("That is not a correct state name.\n")

    print("=== Quiz Over ===")
    print(f"You got {len(correct_answers)} out of {len(all_states)} states.")

    percentage = (len(correct_answers) / len(all_states)) * 100

    if percentage >= 70:
        print(Fore.GREEN + f"Your score: {percentage:.0f}%")
        print(Fore.GREEN + "Great job!")
    else:
        print(Fore.RED + f"Your score: {percentage:.0f}%")
        print(Fore.RED + "Keep practicing!")