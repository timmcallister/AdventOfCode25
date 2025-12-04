def battery():
    sum = 0
    with open('numbers.txt') as f:
        lines = f.readlines()
        for line in lines:
            maxes = []
            indexes = [0]
            for i in range(13, 1, -1):
                ordered  = sorted(line.strip()[indexes[-1]+1:-i], reverse=True)
                maxes.append(ordered[0])
                indexes.append(line.index(maxes[-1]))

    return sum
print(battery())