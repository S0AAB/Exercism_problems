"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    list = [number, number+1, number+2]
    return list
    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    list = rounds_1+rounds_2
    return list
    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False
    pass


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    average = 0.0
    if (len(hand) == 0):
        average
    else:
        average = (sum(hand)/(len(hand)))
    return average
    pass


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    print("-------------------------")
    average = (card_average(hand))
    print("AVERAGE:", average)
    v1 = ((hand[0]+hand[-1])/2)
    print("V1=", v1)
    v2 = (hand[int(len(hand)/2)])
    print("V2=", v2)
    if (v1 == average or v2 == average):
        print("True")
        return True
    else:
        return False

    pass


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    oddlist = []

    for i in range(0, len(hand), 2):
        oddlist.append(hand[i])

    if (card_average(hand) == card_average(oddlist)):
        return True
    else:
        return False

    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if (hand[-1] == 11):
        hand[-1] = (hand[-1]*2)
    return hand

    pass
