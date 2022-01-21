from card_util import print_board, create_hand
from const.default import *
from hand_ranking import hand_score


for _ in range(100000):
    hand = create_hand()
    print_board(hand)
    player_hands = []
    for p in range(players):
        player_hand = hand[2 * p:2 * p + 2] + hand[board_length - table:board_length]
        player_hands.append(sorted(player_hand))
        print(f"Hand score: {hand_score(player_hands[p])}")
