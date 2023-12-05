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
                i += 1
            elif line[0].isdigit():
                add_information(line, maps[i])

    return to_solve

def get_minimum_location(file):
    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = {}, {}, {}, {}, {}, {}, {} 
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

    to_solve = get_information(file, maps)

    res = float("inf")
    for seed in to_solve:
        act_val = seed
        for map_rep in maps:
            for k, (range, start) in map_rep.items():
                if k <= act_val and k + range > act_val:
                    act_val = start + act_val - k
                    break

        res = min(act_val, res)

    return res            