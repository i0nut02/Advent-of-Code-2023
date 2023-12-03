BAG_ELEMETS = {"red": 12, "green": 13, "blue":14}

def add_set(set, bag_el):
    for takes in set.split(","):
        takes = takes.strip(" ").strip("\n")
        num = takes.split(" ")[0]
        color = takes.split(" ")[1]
        bag_el[color] -= int(num)

def define_possible_bag(bag):
    contents = bag.split(":")[1]
    
    for set in contents.split(";"):
        bag_el = BAG_ELEMETS.copy()

        add_set(set, bag_el)
        
        for v in bag_el.values():
            if v < 0:
                return 0
            
    return int(bag.split(":")[0].split(" ")[1])

def define_possible_bags(file):
    res = 0
    with open(file, mode="r") as f:
        for line in f.readlines():
            res += define_possible_bag(line)
    return res

print(define_possible_bags("Day2/input_problem.txt"))