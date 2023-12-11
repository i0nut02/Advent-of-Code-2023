def calculate_distances(file):
    M = None
    with open (file) as f:
        M = f.read().split("\n")
    
    rows = set()
    for i in range(len(M)):
        empty = True
        for j in range(len(M[0])):
            if M[i][j] == "#":
                empty = False
        if empty:
            rows.add(i)
    
    colums = set()
    for j in range(len(M[0])):
        empty = True
        for i in range(len(M)):
            if M[i][j] == "#":
                empty = False
        if empty:
            colums.add(j)
    
    galasies = [(i, j) for i in range(len(M)) for j in range(len(M[0])) if M[i][j] == "#"]

    res = 0
    for i, (y1, x1) in enumerate(galasies):
        for j in range(i+1, len(galasies)):
            y2, x2 = galasies[j]

            intersecY = {k for k in range(min(y1, y2), max(y1, y2))} & rows
            intersecX = {k for k in range(min(x1, x2), max(x1, x2))} & colums

            res += abs(y1 - y2) - len(intersecY) + len(intersecY) * 1_000_000 + abs(x1 - x2) - len(intersecX) + len(intersecX) * 1_000_000
    return res