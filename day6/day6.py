from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2022/day6/day6-input.txt'

with open(file, "r") as f:
    radio_signal = list(f.read())


def findStartMessage(char_group_size):

    for index in range(len(radio_signal)):
        if index+4 <= len(radio_signal)-1:
            #create set as it will remove duplicates
            char_set = set(radio_signal[index:index+char_group_size])
            #print(len(char_set), char_set, index, index+4)
            #if set size is equal to the number of distinct characters needed than we found the start marker as no duplicates were detected
            if len(char_set) == char_group_size:
                print(f'The start-of-packet marker is at {index+char_group_size} for {char_group_size} distinct characters')
                break
            else:
                # if duplicate was found, then clear my set so the next part of my list can become a set
                char_set.clear()

#part 1
findStartMessage(4)
#part 2
findStartMessage(14)