persons = [
    { "name": "Alice", "age": 30, "identifier": "492-40-1123", "identfier_type": "SSN" },
    { "name": "Bob", "age": 25, "identifier": "098-88-3822", "identfier_type": "SSN" },
    { "name": "Charlie", "age": 35, "identifier": "345-11-3423", "identfier_type": "SSN" },
]

def print_persons():
    print("Known persons:")
    for person in persons:
        print(f"- {person['name']}")

def get_message(name):
    for person in persons:
        if person["name"].lower() == name.lower().strip():
            return f"Hello, {person['name']}! Your age is {person['age']} and your {person['identfier_type']} is {person['identifier']}."

    return f"Hello, {name}!"

def hello():
    print_persons()
    
    who_are_you = input("Who are you? ")

    message = get_message(who_are_you)
    return message


if __name__ == "__main__":
    print(hello())
