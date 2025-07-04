def sort_by_key(data, key):
    data.sort(key=lambda x: x[key])
    return data

if __name__ == "__main__":
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_people = sort_by_key(people.copy(), "age")  # ✅ Fixed here
    print("AI-sorted:", sorted_people)
