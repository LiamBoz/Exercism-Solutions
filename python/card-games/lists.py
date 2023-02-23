"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
#from statistics import median
import statistics

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    try:
        if rounds[rounds.index(number)] == number:
            return True
        else:
            return False
    except:
        return False

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_and_last = hand[0] + hand[-1]
    first_avg = first_and_last / 2
    #middle_card = statistics.median(hand)
    middle_card = median(hand)
    true_average = card_average(hand)
    return first_avg == true_average or middle_card == true_average


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_avg = card_average(hand[::2])
    odd_avg = card_average(hand[::1])
    return even_avg == odd_avg


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    else:
        return hand


def median(hand):
    if len(hand)%2 != 0:
        return hand[len(hand)//2]

    else:
        hand_length = len(hand)
        hand_avg = (hand[hand_length//2 - 1] + hand[hand_length//2])/2
        return hand_avg
