import math

def read_file(file):
    G, instruction = {}, ""

    with open(file, mode="r") as f:
        content = f.read().split("\n")
        instruction = content[0]

        for i in range(2, len(content)):
            key, values = content[i].replace(" ", "").replace("(", "").replace(")", "").split("=")
            G[key] = values.split(",")

    return G, instruction

def get_steps(file):
    G, instruction = read_file(file)

    positions = [k for k in G.keys() if k[-1] == "A"]
    steps = 0
    n = len(instruction)

    steps_pos = []

    for act_pos in positions:
        steps = 0
        while act_pos[-1] != "Z":
            act_pos = G[act_pos][0 if instruction[steps % n] == "L" else 1]
            steps += 1
        steps_pos.append(steps)
    
    return math.lcm(*steps_pos)