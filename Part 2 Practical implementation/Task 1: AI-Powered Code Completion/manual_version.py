def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda item: item[key])

if __name__ == "__main__":
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_people = sort_dicts_by_key(people, "age")
    print("Manually sorted:", sorted_people)
