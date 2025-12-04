def combolock():
    password = 0
    current_number = 50
    with open('savefile.txt') as f:
        lines = f.readlines()
        for line in lines:
            direction = line[0:1]
            number = int(line[1:])
            if direction == 'L':
                mover = -1
            else:
                mover = 1
            while number != 0:
                current_number += mover
                if current_number == 0 or current_number == 100:
                    password += 1
                current_number %= 100
                number -= 1
    print(password)
combolock()