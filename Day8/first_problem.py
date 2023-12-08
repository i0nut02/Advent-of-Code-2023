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

    act_pos = "AAA"
    steps = 0
    n = len(instruction)

    while act_pos != "ZZZ":
        act_pos = G[act_pos][0 if instruction[steps % n] == "L" else 1]
        steps += 1
    return steps