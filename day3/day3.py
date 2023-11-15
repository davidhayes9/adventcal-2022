from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day3-input.txt'

with open(file, "r") as f:
    rucksack = f.read()

list_rucksack = rucksack.split("\n")

list_dup_items = []

for sack in list_rucksack:
    half_len = int(len(sack) / 2)
    comp1 = sack[0:half_len]
    comp2 = sack[half_len:len(sack)]
    #print(comp1)
    #print(comp2)
    # check if any letter in comp1 is in comp2, and if so add it to my list
    for items in comp1:
        if items in comp2:
            dup_item = items
    list_dup_items.append(dup_item)

#print(list_dup_items)

priority_scale = {}
pri = 1

lower_start = 97
upper_start = 65

# List for my two starting points - i.e. char(97) is lowercase a, char(65) is uppercase A
# https://learncodingfast.com/wp-content/uploads/2020/08/codepoint.png
alpha_starts = [97, 65]

for start in alpha_starts:
    for i in range(start, start + 26):
        priority_scale[chr(i)] = pri
        pri += 1
 
#print(priority_scale)

total_count = 0

for i in list_dup_items:
    if i in priority_scale:
        total_count += priority_scale[i]

print("The sum of the priorities of the duplicate items is ", total_count)

# Part 2

# https://stackoverflow.com/a/15890829
# Group every three entries together (into a list of lists)
# elves = [list_rucksack[x:x+3] for x in range(0, len(list_rucksack), 3)]

elves = []
for x in range(0, len(list_rucksack), 3):
    elves.append(list_rucksack[x:x+3])

badge = 0
list_badges = []

for group in elves:
    sack1 = group[0]
    sack2 = group[1]
    sack3 = group[2]
    #find the letter that exists in all three sacks
    for items in sack1:
        if items in sack2 and items in sack3:
            badge = items
    list_badges.append(badge)

part2_total_count = 0

for i in list_badges:
    if i in priority_scale:
        part2_total_count += priority_scale[i]

print("The sum of the priorities for badges in part 2 is ", part2_total_count)