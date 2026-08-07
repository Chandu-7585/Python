"""Generate welcome text messages enriched with random poet names and quotes."""

import random
from typing import Dict, List

POETS: List[Dict[str, str]] = [
    {
        "name": "William Wordsworth",
        "quote": "Fill your paper with the breathings of your heart.",
    },
    {
        "name": "Emily Dickinson",
        "quote": "Hope is the thing with feathers that perches in the soul.",
    },
    {
        "name": "Langston Hughes",
        "quote": "Hold fast to dreams, for if dreams die, life is a broken-winged bird.",
    },
    {
        "name": "Maya Angelou",
        "quote": "You will face many defeats in life, but never let yourself be defeated.",
    },
    {
        "name": "Robert Frost",
        "quote": "The best way out is always through.",
    },
    {
        "name": "Rumi",
        "quote": "Let yourself be silently drawn by the strange pull of what you really love.",
    },
]


def choose_random_poet() -> Dict[str, str]:
    """Return a randomly selected poet and their quote."""
    return random.choice(POETS)


def generate_welcome_message(user_name: str) -> str:
    """Generate a welcome message for the given user name.

    The returned message includes a randomly selected poet and an inspiring quote.
    """
    if not user_name or not user_name.strip():
        raise ValueError("User name must be a non-empty string.")

    poet = choose_random_poet()
    return (
        f"Welcome, {user_name}! "
        f"Here's a warm greeting inspired by {poet['name']}: \"{poet['quote']}\""
    )


def main() -> None:
    """Run the welcome message generator from the command line."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a warm welcome message with a random poet quote."
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="Friend",
        help="Name of the person to welcome.",
    )
    args = parser.parse_args()

    print(generate_welcome_message(args.name))


if __name__ == "__main__":
    main()
