"Day 2: Rock Paper Scissors"

with open('day2.txt', 'r') as f:
    lines = f.readlines()

rounds = [(l[0], l[2]) for l in lines]

def round_score(opponent, me):
    i_opponent = ['A', 'B', 'C'].index(opponent)
    i_me = ['X', 'Y', 'Z'].index(me)
    result = (i_me - i_opponent + 1) % 3  # 0 -> lose / 1 -> draw / 2 -> win
    score = result * 3 + (i_me + 1)
    return score

# Part one: total score (XYZ is move)
scores = [round_score(opp, me) for (opp, me) in rounds]
print('Total score obtained (one): ', sum(scores))

# Part two: total score (XYZ is outcome)
def my_move(opponent, result):
    i_opponent = ['A', 'B', 'C'].index(opponent)
    result = ['X', 'Y', 'Z'].index(result)
    i_move = (result + i_opponent - 1) % 3
    return ['X', 'Y', 'Z'][i_move]

scores = [round_score(opp, my_move(opp, res)) for (opp, res) in rounds]
print('Total score obtained (two): ', sum(scores))