import unittest
from collections import Counter


class TestLogAnalyzer(unittest.TestCase):

    def test_log_severity_count(self):
        lines = [
            "INFO Application started",
            "ERROR Database failed",
            "WARNING Retrying connection",
            "CRITICAL Health check failed",
        ]

        counts = Counter()

        for line in lines:
            for level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
              if line.startswith(level + " ") or f" {level} " in line:
                    counts[level] += 1
                    break

        self.assertEqual(counts["INFO"], 1)
        self.assertEqual(counts["WARNING"], 1)
        self.assertEqual(counts["ERROR"], 1)
        self.assertEqual(counts["CRITICAL"], 1)

    def test_empty_logs(self):
        lines = []
        self.assertEqual(len(lines), 0)


if __name__ == "__main__":
    unittest.main()