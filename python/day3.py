if __name__ == "__main__":
    with open('../inputs/day3.txt') as f:
        lines = []
        for line in f:
            line = line.split()
            if line:            
                lines.append(line[0])

tree_mult = 1
line_length = len(lines[0])
steps_to_right = [1, 3, 5, 7]
x = 0

for step in steps_to_right:
    num_trees = 0
    x = 0
    for line in lines:
        if line[x] == '#':
            num_trees += 1
        x += step
        if x >= line_length:
            x -= line_length
    print(num_trees)
    tree_mult *= num_trees

odd = False
num_trees = 0
x = 0
for line in lines:
    if odd:
        odd = False
        continue
    else:
        odd = True
    if line[x] == '#':
        num_trees += 1
    x += 1
    if x >= line_length:
        x -= line_length
tree_mult *= num_trees
print(num_trees)
print(tree_mult)
