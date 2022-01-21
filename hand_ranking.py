from card_util import *
from const.score import *


def flush_score(hand):
    flush_counter = count_flush(hand)
    for i in range(len(flush_counter)):
        if flush_counter[i] >= flush_length:
            j = 0
            while j < len(hand):
                if hand[j] < ranks*i or hand[j] >= ranks*(i+1):
                    hand.remove(hand[j])
                else:
                    j += 1
            sorted_hand = sorted([x % ranks for x in hand], reverse=True)
            straight_bound = is_straight(sorted_hand)
            if straight_bound != 0:
                if is_ace(straight_bound):
                    return royal_flush_bonus + i
                else:
                    return straight_flush_bonus + i + suits*straight_bound
            score = flush_bonus + card_score(sorted_hand, flush_length)
            return score

    return 0


def card_score(sorted_count_hand, c):
    try:
        numbers_hand = [x[0] for x in sorted_count_hand]
    except TypeError:
        numbers_hand = sorted_count_hand
    total = 0
    for i in range(c):
        total += pow(ranks, c-i-1)*numbers_hand[i]
    return total


def hand_score(hand):
    potential_flush_score = flush_score(hand)
    if potential_flush_score >= straight_flush_bonus:
        if potential_flush_score >= royal_flush_bonus:
            print(f"Royal flush of {suit_symbols[potential_flush_score-royal_flush_bonus]}")
            return potential_flush_score
        else:
            print(f"{ranks_symbols[int((potential_flush_score-straight_flush_bonus)/suits)]}{suit_symbols[potential_flush_score%suits]} straight flush")
            return potential_flush_score
    sorted_hand = hand_count(hand)
    straight_bound = is_straight(sorted_hand)
    if sorted_hand[0][1] == 4:
        print(f"Quads {ranks_symbols[sorted_hand[0][0]]} with {ranks_symbols[sorted_hand[1][0]]}")
        return quads_bonus + card_score(sorted_hand, 2)
    elif sorted_hand[0][1] == 3:
        if sorted_hand[1][1] > 1:
            print(f"{ranks_symbols[sorted_hand[0][0]]} full of {ranks_symbols[sorted_hand[1][0]]}")
            return full_house_bonus + card_score(sorted_hand, 2)
        else:
            ret = set_bonus + card_score(sorted_hand, 3)
            if potential_flush_score > ret:
                print("Flush")
                return potential_flush_score
            elif straight_bound != 0:
                print(f"{ranks_symbols[straight_bound]}-high straight")
                return straight_bonus + straight_bound
            else:
                print(f"Set of {ranks_symbols[sorted_hand[0][0]]} with {ranks_symbols[sorted_hand[1][0]]} and {ranks_symbols[sorted_hand[2][0]]}")
                return ret
    elif potential_flush_score != 0:
        print("Flush")
        return potential_flush_score
    elif straight_bound != 0:
        print(f"{ranks_symbols[straight_bound]}-high straight")
        return straight_bonus + straight_bound
    elif sorted_hand[0][1] == 2:
        if sorted_hand[1][1] == 2:
            print(f"Two pairs, {ranks_symbols[sorted_hand[0][0]]} and {ranks_symbols[sorted_hand[1][0]]}, with {ranks_symbols[sorted_hand[2][0]]}")
            return two_pairs_bonus + card_score(sorted_hand, 3)
        else:
            print(f"Pair of {ranks_symbols[sorted_hand[0][0]]} with {ranks_symbols[sorted_hand[1][0]]}, {ranks_symbols[sorted_hand[2][0]]}, {ranks_symbols[sorted_hand[3][0]]}")
            return pair_bonus + card_score(sorted_hand, 4)
    else:
        print(f"No points. Hand is {ranks_symbols[sorted_hand[0][0]]}, {ranks_symbols[sorted_hand[1][0]]}, {ranks_symbols[sorted_hand[2][0]]}, {ranks_symbols[sorted_hand[3][0]]}, {ranks_symbols[sorted_hand[4][0]]}")
        return card_score(sorted_hand, 5)
