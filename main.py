from card_util import write_results
from const.default import *
from hand_ranking import hand_management


for i in range(ranks):
    for j in range(i, ranks):
        if j == i:
            result = hand_management(i, j+ranks, runs)
            pair_name = results_folder + str(ranks_symbols[j]) + str(ranks_symbols[i]) + ".txt"
            write_results(result, pair_name)
        else:
            suited_result = hand_management(i, j, runs)
            suited_name = results_folder + str(ranks_symbols[j]) + str(ranks_symbols[i]) + "s.txt"
            write_results(suited_result, suited_name)

            result = hand_management(i, j+ranks, runs)
            name = results_folder + str(ranks_symbols[j]) + str(ranks_symbols[i]) + ".txt"
            write_results(result, name)
