def win(player, i, j, k):
    return board[i] == board[j] == board[k] == player

def count_wins(key, player):
    if wins[0][key] == -1:
        opp = 3 - player
        if (win(opp, 0, 1, 2) or win(opp, 3, 4, 5) or win(opp, 6, 7, 8) or
            win(opp, 0, 3, 6) or win(opp, 1, 4, 7) or win(opp, 2, 5, 8) or
            win(opp, 0, 4, 8) or win(opp, 2, 4, 6)):
            wins[opp - 1][key] = 1
            wins[player - 1][key] = 0
        else:
            wins[0][key] = wins[1][key] = 0
            for i in range(9):
                if board[i] == 0:
                    board[i] = player
                    new_key = key + player * p3[i]
                    count_wins(new_key, opp)
                    wins[0][key] += wins[0][new_key]
                    wins[1][key] += wins[1][new_key]
                    board[i] = 0

wins = [[-1] * 19683 for _ in range(2)]
board = [0] * 9
p3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]

count_wins(0, 1)
for _ in range(int(input())):
    key = sum(p3[i] * '.XO'.find(c) for i, c in enumerate(input()))
    print(wins[0][key], wins[1][key])