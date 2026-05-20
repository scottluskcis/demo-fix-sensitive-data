def get_message(name):
    return f"Hello, {name}!"

def hello():
    who_are_you = input("Who are you? ")

    message = get_message(who_are_you)
    return message


if __name__ == "__main__":
    print(hello())
