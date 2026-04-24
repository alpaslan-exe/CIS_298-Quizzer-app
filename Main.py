from quiz_engine import QuizConfig, run_quiz
from us_states_quiz import US_STATES_CONFIG


QUIZZES = {
    "1": QuizConfig(
        title="Countries of the World",
        csv_file="countries_capitals.csv",
        answer_column="country",
        prompt="Enter a country",
        time_limit_seconds=15 * 60,
        aliases={
            "USA": "United States",
            "US": "United States",
            "United States of America": "United States",
            "UK": "United Kingdom",
        },
    ),
    "2": QuizConfig(
        title="Capitals of the World",
        csv_file="countries_capitals.csv",
        answer_column="capital",
        prompt="Enter a capital",
        time_limit_seconds=20 * 60,
        aliases={
            "Washington D.C.": "Washington DC",
            "Washington, D.C.": "Washington DC",
        },
    ),
    "3": US_STATES_CONFIG,
    "4": QuizConfig(
        title="US State Capitals",
        csv_file="state_capitals.csv",
        answer_column="capital",
        prompt="Enter a state capital",
        time_limit_seconds=10 * 60,
    ),
}


def print_menu():
    print("\nChoose which quiz you'd like to try:")
    print("1. Countries of the World (15 minutes)")
    print("2. Capitals of the World (20 minutes)")
    print("3. US States (5 minutes)")
    print("4. US State Capitals (10 minutes)")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice in QUIZZES:
            run_quiz(QUIZZES[choice])
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
