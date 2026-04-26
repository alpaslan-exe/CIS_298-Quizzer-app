# CIS 298 Quizzer App

A timed command-line quiz game for practicing geography facts. The app uses CSV
data files and the `colorama` Python library to provide colored score feedback.

## Features

- Countries of the World quiz, 15 minute timer
- Capitals of the World quiz, 20 minute timer
- US States quiz, 5 minute timer
- US State Capitals quiz, 10 minute timer
- Duplicate answer detection, score percentages, and missed-answer previews
- Case-insensitive answer matching with punctuation and accent normalization

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Main.py
```

The app still runs without `colorama`, but installing the requirements enables
colored output.

## Tests

```bash
python -m unittest
```

## Project Files

- `Main.py`: menu and quiz selection
- `quiz_engine.py`: shared CSV loading, answer matching, timing, and scoring
- `us_states_quiz.py`: US states quiz wrapper
- `countries_capitals.csv`: country and capital data
- `state_capitals.csv`: US state and capital data

## Development Log

Record real work only. Each row should match an actual commit and actual time
spent by the listed contributor.

| Date | Contributor | Time Spent | Commit | What Was Accomplished |
| --- | --- | ---: | --- | --- |
| 2026-04-26 | AI-assisted maintenance | ~1 hour | Pending local changes | Built the shared quiz engine, wired all four quiz modes, added setup instructions, and added unit tests. |

## Team Evaluations

Each team member should commit their own evaluation using the course format.
Use real participation details rather than generated or backdated entries.
