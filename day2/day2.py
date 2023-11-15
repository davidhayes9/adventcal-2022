from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day2-input.txt'

with open(file, "r") as f:
    rps_strat_guide = f.read()

# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

games = rps_strat_guide.split("\n")

#print(games[0])

rock_shape = 1
paper_shape = 2
scissor_shape = 3

lose_game = 0
draw_game = 3
win_game = 6

total_score = 0
total_games = 0

for x in games:
    game = x.split()
    opponent = game[0]
    myself = game[1]

    if 'A' in opponent and 'X' in myself:
        total_score += rock_shape + draw_game
        total_games += 1
    
    elif 'A' in opponent and 'Y' in myself:
        total_score += paper_shape + win_game
        total_games += 1

    elif 'A' in opponent and 'Z' in myself:
        total_score += scissor_shape + lose_game
        total_games += 1

    elif 'B' in opponent and 'X' in myself:
        total_score += rock_shape + lose_game
        total_games += 1

    elif 'B' in opponent and 'Y' in myself:
        total_score += paper_shape + draw_game
        total_games += 1

    elif 'B' in opponent and 'Z' in myself:
        total_score += scissor_shape + win_game
        total_games += 1

    elif 'C' in opponent and 'X' in myself:
        total_score += rock_shape + win_game
        total_games += 1

    elif 'C' in opponent and 'Y' in myself:
        total_score += paper_shape + lose_game
        total_games += 1

    elif 'C' in opponent and 'Z' in myself:
        total_score += scissor_shape + draw_game
        total_games += 1


print("Total score = ", total_score)
print("Total games = ", total_games)


    
# Part 2
# "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

part2_total_score = 0
part2_total_games = 0

for x in games:
    game = x.split()
    opponent = game[0]
    myself = game[1]

    if 'A' in opponent and 'X' in myself:
        part2_total_score += scissor_shape + lose_game
        part2_total_games += 1
    
    elif 'A' in opponent and 'Y' in myself:
        part2_total_score += rock_shape + draw_game
        part2_total_games += 1

    elif 'A' in opponent and 'Z' in myself:
        part2_total_score += paper_shape + win_game
        part2_total_games += 1

    elif 'B' in opponent and 'X' in myself:
        part2_total_score += rock_shape + lose_game
        part2_total_games += 1

    elif 'B' in opponent and 'Y' in myself:
        part2_total_score += paper_shape + draw_game
        part2_total_games += 1

    elif 'B' in opponent and 'Z' in myself:
        part2_total_score += scissor_shape + win_game
        part2_total_games += 1

    elif 'C' in opponent and 'X' in myself:
        part2_total_score += paper_shape + lose_game
        part2_total_games += 1

    elif 'C' in opponent and 'Y' in myself:
        part2_total_score += scissor_shape + draw_game
        part2_total_games += 1

    elif 'C' in opponent and 'Z' in myself:
        part2_total_score += rock_shape + win_game
        part2_total_games += 1

print("Part 2 Total score = ", part2_total_score)
print("Part 2 Total games = ", part2_total_games)