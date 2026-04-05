import json

def task() -> float:
    file = "input.json"
    with open(file) as f:
       data = json.load(f)
       product = [item["score"] * item["weight"] for item in data]
       sum = 0
       for total in product:
           sum = sum + total
    return round(sum, 3)
print(task())
