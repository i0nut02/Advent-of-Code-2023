def find_line_calibration(line):
    last = None
    first = None

    for char in line:
        if char.isdigit():
            last = char
            if first == None:
                first = char
    
    return int(first + last) if first != None else 0

def find_lines_calibration(file):
    calibrations = 0

    with open(file, mode="r") as f:
        for line in f.readlines():
            calibrations += find_line_calibration(line)
    return calibrations