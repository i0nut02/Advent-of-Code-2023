def calculate_distances(file):
    M = None
    with open (file) as f:
        M = f.read().split("\n")
    
    rows = []
    for i in range(len(M)):
        empty = True
        for j in range(len(M[0])):
            if M[i][j] == "#":
                empty = False
        if empty:
            rows.append(i)
    
    for n, i in enumerate(rows):
        M = M[:i + n] + ["." * len(M[0])] + M[i + n:]
    
    colums = []
    for j in range(len(M[0])):
        empty = True
        for i in range(len(M)):
            if M[i][j] == "#":
                empty = False
        if empty:
            colums.append(j)
    
    for n, j in enumerate(colums):
        for i in range(len(M)):
            M[i] = M[i][:j+n] + "." + M[i][j+n:]
    
    galasies = [(i, j) for i in range(len(M)) for j in range(len(M[0])) if M[i][j] == "#"]

    return sum([abs(x1 - x2) + abs(y1 - y2) for j, (y1, x1) in enumerate(galasies) for i, (y2, x2) in enumerate(galasies) if i > j])