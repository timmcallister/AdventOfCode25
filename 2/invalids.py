def invalid():
    with open('data.txt') as f:
        rawdata = f.read()
        data = rawdata.split(',')
        sum = 0
        for d in data:
            numbers = d.split('-')
            num1, num2 = int(numbers[0]), int(numbers[1])
            
            
            for i in range(num1, num2, 1):
                strtype = str(i)
                end = len(strtype)
                found = False

                for j in range(1, end, 1):
                    if found:
                        break
                    x = 0
                    y = x + j
                    while y < len(strtype):
                        prev = strtype[x:y]
                        x = x + j
                        y = x + j
                        if y - 1 < len(strtype):
                            curr = strtype[x:y]
                            if curr != prev:
                                break
                            if y == len(strtype):
                                sum += i
                                found = True
    return sum
print(invalid())