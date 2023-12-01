NUMBERS = {"one": "1", "two": "2", "three": "3", 
           "four": "4", "five": "5", "six": "6", 
           "seven": "7", "eight": "8", "nine": "9"}

LENGHTS = [3, 4, 5]

def find_line_calibration(line):
    last = None
    first = None
    n = len(line)

    for i, char in enumerate(line):
        if char.isdigit():
            last = char
            if first == None:
                first = char
        else:
            for l in LENGHTS:
                if i + l <= n:
                    if line[i: i + l] in NUMBERS:
                        last = NUMBERS[line[i: i + l]]
                        if first == None:
                            first = NUMBERS[line[i: i + l]]
                        break
    
    return int(first + last) if first != None else 0

def find_lines_calibration(file):
    calibrations = 0

    with open(file, mode="r") as f:
        for line in f.readlines():
            calibrations += find_line_calibration(line)
    return calibrations