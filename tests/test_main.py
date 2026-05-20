from main import get_message, hello


def test_get_message_matches_known_person():
    assert (
        get_message("Alice")
        == "Hello, Alice! Your age is 30 and your SSN is ***-**-1123."
    )


def test_get_message_matches_case_insensitive_and_trimmed_input():
    assert (
        get_message("   aLiCe   ")
        == "Hello, Alice! Your age is 30 and your SSN is ***-**-1123."
    )


def test_get_message_unknown_person_returns_name_greeting():
    assert get_message("World") == "Hello, World!"


def test_hello_uses_input_and_returns_message(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Bob")
    assert hello() == "Hello, Bob! Your age is 25 and your SSN is ***-**-3822."
