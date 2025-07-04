from manual_version import sort_dicts_by_key
from copilot_version import sort_by_key

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Original:", people)
print("Manual Sort:", sort_dicts_by_key(people, "age"))
print("AI Sort (in-place):", sort_by_key(people.copy(), "age"))
