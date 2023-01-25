"Day 1: Calorie counting"

all_cals = []
with open('day1.txt', 'r') as f:
    elf_cals = 0
    for line in f:
        if line == '\n':
            all_cals.append(elf_cals)
            elf_cals = 0
        else:
            elf_cals += int(line)

# Part one: max calories
max_cals = max(all_cals)
print('Maximum calories carried by a single elf: ', max_cals)

# Part two: sum of top three
top_cals = []
for i in range(3):
    max_cals = max(all_cals)
    top_cals.append(max_cals)
    all_cals.pop(all_cals.index(max_cals))
print('Calories being carried by top three elves: ', sum(top_cals))
