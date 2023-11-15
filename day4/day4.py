from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day4-input.txt'

with open(file, "r") as f:
    assignments = f.read().split("\n")

section_range = []
for line in assignments:
    num_range = line.split(",")
    for elf in num_range:
        section_range.append(elf.split("-"))

group_section = []
for i in section_range:
    elf_start = i[0]
    elf_end = i[1]
    section_id = list(range(int(elf_start), int(elf_end)+1))
    group_section.append(section_id)

# https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/
counter = 0
part2_counter = 0
for g in  range(0, len(group_section), 2):
    if set(group_section[g]).issubset(set(group_section[g+1])) or set(group_section[g+1]).issubset(set(group_section[g])):
        counter +=1
    if set(group_section[g]).intersection(set(group_section[g+1])) or set(group_section[g+1]).intersection(set(group_section[g])):
        part2_counter +=1

print("Fully overlapping assignments: ", counter)
print("Part2 - overlapping assignments: ", part2_counter)