"""Importing in python."""


from lessons import helpers
# from lessons import helpers as hp allows us to shorten hp

# can also import functions and not modules
# from lessons.helpers import powerful
 

def main() -> None:
    """Enterypoint of program."""
    print(helpers.powerful(3, 6))
    print(f"The answer: {helpers.The_answer}")


if __name__ == "__main__":
    main()