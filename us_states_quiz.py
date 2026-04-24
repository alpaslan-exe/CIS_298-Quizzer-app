from quiz_engine import QuizConfig, run_quiz

US_STATES_CONFIG = QuizConfig(
    title="US States Quiz",
    csv_file="state_capitals.csv",
    answer_column="state",
    prompt="Enter a state",
    time_limit_seconds=5 * 60,
)


def run_us_states_quiz():
    run_quiz(US_STATES_CONFIG)
