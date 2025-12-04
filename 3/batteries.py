def battery():
    sum = 0
    with open('numbers.txt') as f:
        lines = f.readlines()
        for line in lines:
            maxes = []
            indexes = [-1]
            for i in range(11, -1, -1):
                if i > 0:
                    ordered  = sorted(line.strip()[indexes[-1]+1:-i], reverse=True)
                else:
                    ordered = sorted(line.strip()[indexes[-1] + 1:], reverse=True)
                maxes.append(ordered[0])
                indexes.append(line.index(maxes[-1], indexes[-1] + 1))
            sum += int(''.join(maxes))

    return sum
print(battery())
