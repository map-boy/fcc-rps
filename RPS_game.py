# RPS_game.py

import random

def play(player1, player2, num_games=1000, verbose=False):
    p1_wins = 0
    p2_wins = 0
    ties = 0
    prev1 = ""
    prev2 = ""

    for _ in range(num_games):
        move1 = player1(prev2)
        move2 = player2(prev1)

        if verbose:
            print(f"Player1: {move1}  Player2: {move2}")

        if move1 == move2:
            ties += 1
        elif (move1 == "R" and move2 == "S") or \
             (move1 == "P" and move2 == "R") or \
             (move1 == "S" and move2 == "P"):
            p1_wins += 1
        else:
            p2_wins += 1

        prev1, prev2 = move1, move2

    win_rate = p1_wins / num_games * 100
    print(f"Player1 win rate: {win_rate:.2f}%")
    return win_rate

# Bot definitions
def quincy(prev_play):
    moves = ["R", "P", "S"]
    if not hasattr(quincy, "index"):
        quincy.index = 0
    move = moves[quincy.index % len(moves)]
    quincy.index += 1
    return move

def abbey(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return "R"

    most_common = max(set(opponent_history), key=opponent_history.count)
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common]

def kris(prev_play):
    if not hasattr(kris, "opponent_history"):
        kris.opponent_history = []

    if prev_play:
        kris.opponent_history.append(prev_play)

    if len(kris.opponent_history) < 1:
        return "R"
    else:
        return kris.opponent_history[-1]

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return "R"

    last_three = opponent_history[-3:]
    guess = max(set(last_three), key=last_three.count)
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[guess]
