import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        info = []
        for line in reader:
            info.append(line)
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
