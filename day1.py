from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day1-input.txt'

with open(file, "r") as f:
    elf_cals = f.read()

cal_array = elf_cals.split("\n\n")

#create dict for total cals per elf
dict_total_cal = {}

for elf in range(len(cal_array)):
    items = cal_array[elf]
    item = items.splitlines()

    total = 0
    
    for cal in item:
        total += int(cal)
    
    elf_name = 'Elf ' + str(elf + 1)

    dict_total_cal[elf_name] = total


# sort dict by largest value 
sorted_dict_total_cal = sorted(dict_total_cal.items(), key=lambda item: item[1])

top_three_elf_cals = list(sorted_dict_total_cal)[-3:]

print(top_three_elf_cals)

total_three_cals = 0

for key, value in top_three_elf_cals:
    total_three_cals += value

print("Total cals from top three elves: ", total_three_cals)