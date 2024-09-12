"""My first Challenge Question!"""

__author__ = "730744035"


def mimic(message: str) -> str:
    """Take the input and repeat it back to you"""
    return message


def main() -> None:
    """print results of calling mimic"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
