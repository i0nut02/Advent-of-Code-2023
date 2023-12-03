BAG_ELEMETS = {"red": 0, "green": 0, "blue":0}

def add_set(set, bag_el):
    for takes in set.split(","):
        takes = takes.strip(" ").strip("\n")

        num = takes.split(" ")[0]
        color = takes.split(" ")[1]

        bag_el[color] += int(num)

def define_possible_bag(bag):
    contents = bag.split(":")[1]
    res = 1
    bag_el = BAG_ELEMETS.copy()

    for set in contents.split(";"):
        bag_set_el = BAG_ELEMETS.copy()
        add_set(set, bag_set_el)

        for k, v in bag_set_el.items():
            bag_el[k] = max(bag_el[k], v)
        
    for v in bag_el.values():
        res *= v
    return res

def define_possible_bags(file):
    res = 0
    with open(file, mode="r") as f:
        for line in f.readlines():
            res += define_possible_bag(line)
    return res

print(define_possible_bags("Day2/input_problem.txt"))