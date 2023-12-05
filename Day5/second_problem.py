def add_information(line, map_conv):
    nums = list(map(int, line.split(" ")))

    map_conv[nums[1]] = [nums[-1], nums[0]]

def get_information(file, maps):
    i = -1
    to_solve = None

    with open(file, mode="r") as f:
        for line in f.readlines():
            if line.startswith("seeds:"):
                to_solve = list(map(int, line.split(":")[1].strip(" ").strip("/n").split(" ")))
            elif line == "\n":
                if i >= 0:
                    map_conv = maps[i]
                    minimum = 0
                    sorteed_keys = list(sorted(map_conv.keys()))
                    for k in sorteed_keys:
                        if k != minimum:
                            map_conv[minimum] = [k - minimum, minimum]
                        minimum = k + map_conv[k][0]

                    map_conv[minimum] = [10**9, minimum]
                i += 1
            elif line[0].isdigit():
                add_information(line, maps[i])

    return [(to_solve[i], to_solve[i+1]) for i in range(0, len(to_solve), 2)]

def calculate_intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start < end:
        return start, end
    else:
        return None

def get_minimum_location(file):
    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = {}, {}, {}, {}, {}, {}, {} 
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

    to_solve = get_information(file, maps)
    for map in maps:
        print(map)
    print(to_solve)
    for map_rep in maps:
        new_to_solve = []
        for element, range_element in to_solve:
            for k, (range, start) in map_rep.items():
                intersection = calculate_intersection((element, element + range_element -1), (k, k + range -1))
                if intersection != None:
                    new_to_solve.append((start + intersection[0] - k, intersection[1] - intersection[0] +1))
       
        to_solve = new_to_solve
        
    return min([l[0] for l in to_solve])