rounds = [1,2,3,4,5]
number = 0

def list_contains_round(rounds,number):
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

print(list_contains_round(rounds,number))