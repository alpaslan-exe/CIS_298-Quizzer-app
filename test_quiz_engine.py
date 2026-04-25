import csv
import tempfile
import unittest
from pathlib import Path

from quiz_engine import QuizConfig, build_answer_key, format_time, normalize_answer


class QuizEngineTests(unittest.TestCase):
    def test_normalize_answer_ignores_case_spacing_and_accents(self):
        self.assertEqual(normalize_answer("  São-Paulo  "), "sao paulo")

    def test_format_time_uses_minutes_and_seconds(self):
        self.assertEqual(format_time(65), "01:05")

    def test_build_answer_key_adds_aliases(self):
        with tempfile.TemporaryDirectory() as directory:
            csv_path = Path(directory) / "answers.csv"
            with csv_path.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["country", "capital"])
                writer.writeheader()
                writer.writerow({"country": "United States", "capital": "Washington DC"})

            config = QuizConfig(
                title="Test",
                csv_file=str(csv_path),
                answer_column="country",
                prompt="Answer",
                time_limit_seconds=60,
                aliases={"USA": "United States"},
            )

            answers = build_answer_key(config)

        self.assertEqual(answers["usa"], "United States")
        self.assertEqual(answers["united states"], "United States")


if __name__ == "__main__":
    unittest.main()
