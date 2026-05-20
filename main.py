persons = [
    { "name": "Alice", "age": 30, "identifier": "***-**-1123", "identfier_type": "SSN" },
    { "name": "Bob", "age": 25, "identifier": "***-**-3822", "identfier_type": "SSN" },
    { "name": "Charlie", "age": 35, "identifier": "***-**-3423", "identfier_type": "SSN" },
]

def get_message(name):
    for person in persons:
        if person["name"].lower() == name.lower().strip():
            return f"Hello, {person['name']}! Your age is {person['age']} and your {person['identfier_type']} is {person['identifier']}."

    return f"Hello, {name}!"

def hello():
    who_are_you = input("Who are you? ")

    message = get_message(who_are_you)
    return message


if __name__ == "__main__":
    print(hello())
