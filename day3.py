"Day 3: Rucksack Reorganization"
import string

with open('day3.txt', 'r') as f:
    lines = f.readlines()

alphabet = list(string.ascii_letters)

priorities = []
for line in lines:
    line = line.strip()  # remove newline char
    i_half = int(len(line) / 2)
    set1, set2 = set(line[:i_half]), set(line[i_half:])
    shared_item = set1.intersection(set2).pop()
    prio = alphabet.index(shared_item) + 1  # 'a' equals 1
    priorities.append(prio)

# Part one
print('Sum of priorities of shared items: ', sum(priorities))

# Part two
priorities = []
for i in range(0, len(lines), 3):
    group_lines = [set(l.strip()) for l in lines[i:i+3]]
    badge_item = set.intersection(*group_lines).pop()
    priorities.append(alphabet.index(badge_item) + 1)

print('Sum of priorities of badge items: ', sum(priorities))



