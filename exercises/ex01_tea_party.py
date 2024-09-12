"""This program plans the cost expected and the quantity of tea bags and snacks needed for the amount of guests that are input for a tea party."""

__author__: str = "730744035"


def main_planner(guests: int) -> None:
    """Function that calls all other functions and creates the printed output"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints a sentence for amount of guest with guests as a string
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # prints amount of tea bags with use of function tea_bags() as a string and using keyword arguments
    print(
        "Treats: " + str(treats(people=guests))
    )  # prints amount of treats as a string with with use of treats() and setting its perameters people equal to guests (keyword arguments)
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # prints the cost in dollars by connecting the parameters of cost() to the functions tea_bags() and treats() that each have keyword arguments from people to guests
    return None  # my identions look weird very time that I save the code


def tea_bags(people: int) -> int:
    """Determines the amount of tea bags needed based on the amount of people input by the user."""
    return people * 2  # returns the number of tea bags needed (2 for each person)


def treats(people: int) -> int:
    """function to determine the amount of treats needed based off of the amount of tea
    each guest will have"""
    return int(
        tea_bags(people=people) * 1.5
    )  # calls to tea_bags using a keyword argument and then multiplies by 1.5 to return the amount of treats needed as an integer


def cost(tea_count: int, treat_count: int) -> float:
    """Function that detemines the total costs for the tea party"""
    return (tea_count * 0.50) + (treat_count * 0.75)  # returns total cost as a float


if (
    __name__ == "__main__"
):  # this makes the code easily runnable and user friendly by showing a prompt where only an integer is needed to be typed
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
