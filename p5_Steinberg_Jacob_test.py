# p5_Steinberg_Jacob_test.py
# Jacob Steinberg
# Homework 2 - Problem 5

import unittest
import os
from datetime import datetime

from p5_Steinberg_Jacob import (
    read_observations,
    station_statistics,
    station_outliers,
    write_statistics
)


class TestWeatherStationAnalyzer(unittest.TestCase):

    def create_file(self, filename, text):
        with open(filename, "w") as file:
            file.write(text)

    def test_multiple_stations(self):
        filename = "test_weather.txt"

        self.create_file(
            filename,
            "Miami,09:00:00 AM 04/20/2026,80.0\n"
            "Orlando,10:00:00 AM 04/20/2026,75.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertIn("Miami", observations)
        self.assertIn("Orlando", observations)
        self.assertEqual(errors, [])

        os.remove(filename)

    def test_negative_temperature(self):
        filename = "test_negative.txt"

        self.create_file(
            filename,
            "Miami,09:00:00 AM 04/20/2026,-25.5\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(observations["Miami"][0][1], -25.5)
        self.assertEqual(errors, [])

        os.remove(filename)

    def test_duplicate(self):
        filename = "test_duplicate.txt"

        self.create_file(
            filename,
            "Miami,09:00:00 AM 04/20/2026,80.0\n"
            "Miami,09:00:00 AM 04/20/2026,85.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(len(observations["Miami"]), 1)
        self.assertEqual(len(errors), 1)

        os.remove(filename)

    def test_invalid_range(self):
        filename = "test_range.txt"

        self.create_file(
            filename,
            "Miami,09:00:00 AM 04/20/2026,200.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertNotIn("Miami", observations)
        self.assertEqual(len(errors), 1)

        os.remove(filename)

    def test_statistics(self):
        observations = {
            "Miami": [
                (datetime(2026, 4, 20, 9), 70.0),
                (datetime(2026, 4, 21, 9), 80.0),
                (datetime(2026, 4, 22, 9), 90.0)
            ]
        }

        statistics = station_statistics(observations)

        self.assertEqual(
            statistics["Miami"],
            (70.0, 90.0, 80.0)
        )

    def test_outliers(self):
        observations = {
            "Miami": [
                (datetime(2026, 4, 20, 9), 70.0),
                (datetime(2026, 4, 21, 9), 80.0),
                (datetime(2026, 4, 22, 9), 90.0)
            ],
            "Orlando": [
                (datetime(2026, 4, 20, 9), 90.0),
                (datetime(2026, 4, 21, 9), 80.0),
                (datetime(2026, 4, 22, 9), 70.0)
            ]
        }

        outliers = station_outliers(observations)

        self.assertIn("Miami", outliers)
        self.assertNotIn("Orlando", outliers)

        date, temperature, mean = outliers["Miami"]

        self.assertEqual(
            date,
            datetime(2026, 4, 22, 9)
        )
        self.assertEqual(temperature, 90.0)
        self.assertEqual(mean, 80.0)

    def test_sorted_output(self):
        filename = "test_statistics.txt"

        statistics = {
            "Orlando": (60.0, 80.0, 70.0),
            "Miami": (70.0, 90.0, 80.0),
            "Boca Raton": (65.0, 85.0, 75.0)
        }

        write_statistics(filename, statistics)

        with open(filename, "r") as file:
            lines = file.readlines()

        self.assertEqual(
            lines,
            [
                "Boca Raton,65.0,85.0,75.0\n",
                "Miami,70.0,90.0,80.0\n",
                "Orlando,60.0,80.0,70.0\n"
            ]
        )

        os.remove(filename)

    def test_missing_file(self):
        with self.assertRaises(OSError):
            read_observations(
                "file_that_does_not_exist.txt"
            )


if __name__ == "__main__":
    unittest.main()
