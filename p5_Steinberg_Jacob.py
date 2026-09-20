# p5_Steinberg_Jacob.py
# Jacob Steinberg
# Homework 2 - Problem 5
# Weather Station Analyzer

import sys
from datetime import datetime


def read_observations(filename):
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            parts = line.split(",")

            # Check for malformed lines
            if len(parts) != 3:
                errors.append((line_number, "Malformed line"))
                continue

            station = parts[0].strip()
            date_string = parts[1].strip()
            temperature_string = parts[2].strip()

            if station == "":
                errors.append((line_number, "Invalid station"))
                continue

            # Convert date
            try:
                date = datetime.strptime(
                    date_string,
                    "%I:%M:%S %p %m/%d/%Y"
                )
            except ValueError:
                errors.append((line_number, "Invalid date"))
                continue

            # Convert temperature
            try:
                temperature = float(temperature_string)
            except ValueError:
                errors.append((line_number, "Invalid temperature"))
                continue

            # Check temperature range
            if temperature < -100.0 or temperature > 150.0:
                errors.append((line_number, "Temperature out of range"))
                continue

            # Check for duplicate station/date
            key = (station, date)

            if key in seen:
                errors.append((line_number, "Duplicate station/date"))
                continue

            seen.add(key)

            if station not in observations:
                observations[station] = []

            observations[station].append((date, temperature))

    # Sort observations chronologically
    for station in observations:
        observations[station].sort(key=lambda item: item[0])

    return observations, errors


def station_statistics(observations):
    statistics = {}

    for station in observations:
        temperatures = []

        for date, temperature in observations[station]:
            temperatures.append(temperature)

        minimum = min(temperatures)
        maximum = max(temperatures)
        mean = sum(temperatures) / len(temperatures)

        statistics[station] = (minimum, maximum, mean)

    return statistics


def station_outliers(observations):
    statistics = station_statistics(observations)

    return {
        station: (
            observations[station][-1][0],
            observations[station][-1][1],
            statistics[station][2]
        )
        for station in observations
        if observations[station][-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    with open(filename, "w") as file:
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]

            file.write(
                f"{station},{minimum:.1f},{maximum:.1f},{mean:.1f}\n"
            )


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python p5_Steinberg_Jacob.py "
            "input_file output_file"
        )
        return

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        observations, errors = read_observations(input_filename)

        statistics = station_statistics(observations)
        outliers = station_outliers(observations)

        print("Statistics:")
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]

            print(
                f"{station}: min={minimum:.1f}, "
                f"max={maximum:.1f}, mean={mean:.1f}"
            )

        print("\nOutliers:")
        for station in sorted(outliers):
            date, temperature, mean = outliers[station]

            print(
                f"{station}: {date}, "
                f"temperature={temperature:.1f}, "
                f"mean={mean:.1f}"
            )

        if errors:
            print("\nErrors:")
            for line_number, message in errors:
                print(f"Line {line_number}: {message}")

        write_statistics(output_filename, statistics)

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    main()
