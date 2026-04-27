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

## Team Evaluation
| Name         | Contribution                                    | Score |
|--------------|-------------------------------------------------|-------|
| MohammadNour | Pulled Data contributed to Colorizing the tests |   5/5 |
| Zhaglas      | Built Menu interface, QC                        |   5/5 |
| Alpaslan     | Maintained github, integrated data pipelines.   |   5/5 |

## Log
| Person        | Feature area                                                                 | time |
|---------------|------------------------------------------------------------------------------|----------------------|
| MohammadNour  | early scaffolding, README/content, US states quiz files, dependency/file setup | 24.5 hours           |
| Alpaslan      | shared quiz engine, refactor, normalization, tests, integration, managed git  | 23.8 hours           |
| Zhaglas       | menu loop, quiz dispatch, `.gitignore`, quality-control/support work + QA testing | 20.7 hours           |

Total: 69.0 hours
