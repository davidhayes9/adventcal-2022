from pprint import pprint
import copy

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day5/day5-input.txt'

with open(file, "r") as f:
    crates = f.read().split("\n\n")

lines = crates[0].split("\n")

# create list of integers that represent the string index of the stacks of crates
num_index = []
for i in range(1, 10):
    num_str = str(i)
    num_index.append(lines[-1].index(num_str))

mydict = {}
for i in range(1, 10):
    mydict[i] = []

#https://stackoverflow.com/a/55484739
dict_key = 0
# for loop will start at the first string index and then iterate through the rest
for index in num_index:
    dict_key += 1

    #at the string index, iterate through the lines (except the last line)
    for i in range(7,-1, -1):

        # exclude empty spaces
        if lines[i][index] != " ":
            mydict[dict_key].append(lines[i][index])

pprint(mydict)

# sort the move instructions for the crates
move_lines = crates[1].splitlines()

move_list = []
list_counter = 0
# iterate through each line
for moves in move_lines:
    counter = 0
    move_list.insert(list_counter, [])

    while counter < len(moves):

        #record the position of the first digit
        if moves[counter].isdigit():
            start = counter
            while counter < len(moves) and moves[counter].isdigit():
                counter += 1
            end = counter
            move_list[list_counter].append(moves[start:end])
        else:
            counter += 1
    list_counter +=1


def moveCrates(flag):

    #work with copys of mydict, so the changes done in exercise part one 
    #does not impact the changes that need to be done in part two
    deep_copy1 = copy.deepcopy(mydict)
    deep_copy2 = copy.deepcopy(mydict)

    if flag == 1:
        newdict = deep_copy1
    if flag == 2:
        newdict = deep_copy2

    for i in move_list:
        move_count = int(i[0])
        move_from = int(i[1])
        move_to = int(i[2])
        move_pos = len(newdict[move_from]) - move_count

        for j in range(move_count):
            if flag == 1:
                value = newdict[move_from].pop()
            elif flag == 2:
                value = newdict[move_from].pop(move_pos)
            newdict[move_to].insert(len(newdict[move_to]), value)
    
    print(f"The crates that end up on top of each stack for part {flag} are: ")
    top_crates = ''
    for i in range(1, len(newdict)+1):
        top_crates += newdict[int(i)][-1]
    print(top_crates)

moveCrates(1)
moveCrates(2)