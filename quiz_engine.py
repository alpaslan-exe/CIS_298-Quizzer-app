from __future__ import annotations

import csv
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

try:
    from colorama import Fore, Style, init
except ImportError:  # pragma: no cover - fallback keeps the app runnable without deps
    class _NoColor:
        GREEN = ""
        RED = ""
        YELLOW = ""
        CYAN = ""
        BRIGHT = ""
        RESET_ALL = ""

    Fore = Style = _NoColor()

    def init(*_args, **_kwargs):
        return None


init(autoreset=True)

PROJECT_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class QuizConfig:
    title: str
    csv_file: str
    answer_column: str
    prompt: str
    time_limit_seconds: int
    success_threshold: float = 0.7
    aliases: dict[str, str] = field(default_factory=dict)


def normalize_answer(answer: str) -> str:
    cleaned = unicodedata.normalize("NFKD", answer.strip().lower())
    cleaned = "".join(char for char in cleaned if not unicodedata.combining(char))
    cleaned = cleaned.replace(".", "")
    cleaned = cleaned.replace(",", "")
    cleaned = cleaned.replace("-", " ")
    return " ".join(cleaned.split())


def load_answers(csv_file: str, answer_column: str) -> dict[str, str]:
    path = PROJECT_DIR / csv_file
    answers: dict[str, str] = {}

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if answer_column not in (reader.fieldnames or []):
            raise ValueError(f"Column '{answer_column}' was not found in {csv_file}.")

        for row in reader:
            display_answer = (row.get(answer_column) or "").strip()
            if display_answer:
                answers[normalize_answer(display_answer)] = display_answer

    return answers


def format_time(seconds: int) -> str:
    minutes, remainder = divmod(max(seconds, 0), 60)
    return f"{minutes:02d}:{remainder:02d}"


def build_answer_key(config: QuizConfig) -> dict[str, str]:
    answers = load_answers(config.csv_file, config.answer_column)

    for alias, official_answer in config.aliases.items():
        official_key = normalize_answer(official_answer)
        if official_key in answers:
            answers[normalize_answer(alias)] = answers[official_key]

    return answers


def run_quiz(config: QuizConfig) -> None:
    answer_key = build_answer_key(config)

    if not answer_key:
        print(Fore.RED + "No quiz answers were loaded.")
        return

    official_answers = set(answer_key.values())
    correct_answers: set[str] = set()
    start_time = time.time()

    print(Style.BRIGHT + f"\n=== {config.title} ===")
    print(f"Type as many answers as you can. Enter 'exit' to quit early.\n")

    while len(correct_answers) < len(official_answers):
        time_left = config.time_limit_seconds - int(time.time() - start_time)

        if time_left <= 0:
            print(Fore.YELLOW + "\nTime is up!")
            break

        answer = input(f"[{format_time(time_left)}] {config.prompt}: ")
        normalized_answer = normalize_answer(answer)

        if normalized_answer == "exit":
            print(Fore.YELLOW + "Exiting quiz...")
            break

        if normalized_answer in answer_key:
            official_answer = answer_key[normalized_answer]

            if official_answer in correct_answers:
                print(Fore.YELLOW + "You already got that one.\n")
            else:
                correct_answers.add(official_answer)
                print(Fore.GREEN + f"Correct: {official_answer}\n")
        else:
            print(Fore.RED + "That answer is not in this quiz.\n")

    print_results(config, official_answers, correct_answers)


def print_results(
    config: QuizConfig, official_answers: set[str], correct_answers: set[str]
) -> None:
    total = len(official_answers)
    score = len(correct_answers)
    percentage = (score / total) * 100 if total else 0
    passed = percentage >= config.success_threshold * 100
    color = Fore.GREEN if passed else Fore.RED

    print(Style.BRIGHT + "\n=== Quiz Over ===")
    print(f"You got {score} out of {total} answers.")
    print(color + f"Your score: {percentage:.0f}%")

    if score < total:
        missed = sorted(official_answers - correct_answers)
        preview = ", ".join(missed[:15])
        suffix = "..." if len(missed) > 15 else ""
        print(Fore.CYAN + f"Missed answers: {preview}{suffix}")
