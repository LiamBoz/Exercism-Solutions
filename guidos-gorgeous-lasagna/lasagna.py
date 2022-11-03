"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO: define the 'preparation_time_in_minutes()' function
def preparation_time_in_minutes(NUMBER_OF_LAYERS):
    """this function determines the preparation time
    in minutes based on the number of layers
    """
#       and consider using 'PREPARATION_TIME' here
    return NUMBER_OF_LAYERS*2

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(NUMBER_OF_LAYERS, elapsed_bake_time):
    """this function finds the total elapsed time based on number of
    layers and the elapsed bake time already
    """
    return NUMBER_OF_LAYERS*2 + elapsed_bake_time
