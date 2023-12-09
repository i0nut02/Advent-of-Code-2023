def get_oasi_history(history):
    step = list(map(int, history.strip(" ").split(" ")))
    res = 0

    while True:
        for el in step:
            if el != 0:
                break
        else:
            break

        res += step[-1]
        step = [step[j] - step[j-1] for j in range(1, len(step))]
        i += 1
    
    return res

def get_oasis_histories(file):
    res = 0
    with open(file, mode="r") as f:
        for line in f.readlines():
            res += get_oasi_history(line)
    return res