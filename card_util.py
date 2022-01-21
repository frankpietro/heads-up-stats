from const.default import *
from random import randint


def create_hand():
    hand_array = []
    for _ in range(board_length):
        card = randint(0, suits*ranks - 1)
        while card in hand_array:
            card = randint(0, suits*ranks - 1)

        hand_array.append(card)

    return hand_array


def card_string(card):
    return ranks_symbols[card % ranks] + suit_symbols[int(card / ranks)]


def print_board(board):
    for p in range(players):
        print(f"Player {p+1}: {card_string(board[2*p])}-{card_string(board[2*p+1])}")

    table_string = ""
    for i in range(table):
        if i != 0:
            table_string += "-"

        table_string += card_string(board[board_length - table + i])

    print(f"Table: {table_string}")


def is_ace(card):
    return card % ranks == ranks - 1


def is_lower_than_ten(card):
    return card % ranks < ranks - 5


def is_straight(hand):
    sorted_hand = []
    try:
        i = 0
        while i < len(hand):
            if hand[i][1] == 0:
                hand = hand[0:i]
                sorted_hand = sorted([x[0] for x in hand], reverse=True)
            else:
                i += 1
    except TypeError:
        sorted_hand = hand

    if sorted_hand[0] == ranks - 1:
        sorted_hand.append(-1)

    count = 1
    for i in range(1, len(sorted_hand)):
        if sorted_hand[i] == sorted_hand[i-1] - 1:
            count += 1
        else:
            count = 1

        if count == straight_length:
            return 4 + sorted_hand[i]

    return 0


def hand_count(hand):
    hand_numbers = sorted([int(c % ranks) for c in hand])
    count_array = [0]*ranks
    for h in hand_numbers:
        count_array[h] += 1

    sorted_count_array = sorted(enumerate(count_array), key=lambda x: (x[1], x[0]), reverse=True)

    return sorted_count_array


def count_flush(hand):
    flush_numbers = sorted([int(c / ranks) for c in hand])
    flush_array = [0]*suits
    for h in flush_numbers:
        flush_array[h] += 1

    return flush_array
