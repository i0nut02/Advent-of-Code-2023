def get_oasi_history(history):
    steps = [list(map(int, history.strip(" ").split(" ")))]
    i = 0

    while True:
        for el in steps[i]:
            if el != 0:
                break
        else:
            break

        steps.append([steps[i][j] - steps[i][j-1] for j in range(1, len(steps[i]))])
        i += 1
    
    last = 0
    for i in range(len(steps) -2, -1, -1):
        last = steps[i][0] - last
    return last

def get_oasis_histories(file):
    res = 0
    with open(file, mode="r") as f:
        for line in f.readlines():
            res += get_oasi_history(line)
    return res