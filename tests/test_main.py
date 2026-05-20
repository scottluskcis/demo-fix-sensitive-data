from main import get_message, hello, print_persons


def test_get_message_matches_known_person():
    assert (
        get_message("Alice")
        == "Hello, Alice! Your age is 30 and your SSN is 492-40-1123."
    )


def test_get_message_matches_case_insensitive_and_trimmed_input():
    assert (
        get_message("   aLiCe   ")
        == "Hello, Alice! Your age is 30 and your SSN is 492-40-1123."
    )


def test_get_message_unknown_person_returns_name_greeting():
    assert get_message("World") == "Hello, World!"


def test_hello_uses_input_and_returns_message(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Bob")
    assert hello() == "Hello, Bob! Your age is 25 and your SSN is 098-88-3822."


def test_print_persons_prints_expected_output(capsys):
    print_persons()

    captured = capsys.readouterr()
    assert captured.out == (
        "----------------------------------------\n"
        "Known persons:\n"
        "- Alice\n"
        "- Bob\n"
        "- Charlie\n"
        "----------------------------------------\n"
    )


def test_print_persons_includes_all_known_names(capsys):
    print_persons()

    output = capsys.readouterr().out
    for name in ["Alice", "Bob", "Charlie"]:
        assert f"- {name}\n" in output
