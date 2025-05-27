# RPS.py

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    # Frequency counter
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1

    # Predict the opponent's most frequent move
    predicted_move = max(freq, key=freq.get)

    # Counter it
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
