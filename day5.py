# file = open('input.txt', 'r')
file = open('input_test.txt', 'r')

lines = [line.split() for line in file]
lines.append([])

seeds = list()
seed_to_soil = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()

for seed in lines[1][1:]:
    seeds.append(int(seed))

print('test')
what_now = ''
for line in lines:
    if line == "seed-to-soil map:":
        what_now = "seed_to_soil"
    elif line == "soil-to-fertilizer map:":
        what_now = "soil_to_fertilizer"
    elif line == "fertilizer-to-water map:":
        what_now = "fertilizer_to_water"
    elif line == "water-to-light map:":
        what_now = "water_to_light"
    elif line == "light-to-temperature map:":
        what_now = "light_to_temperature"
    elif line == "temperature-to-humidity map:":
        what_now = "temperature_to_humidity"
    elif line == "humidity-to-location map:":
        what_now = "humidity_to_location"

soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()


def find_mapping(current_numbers, mapping):
    for map in mapping:
        list_temp = range(map[0],map[2])
    
    return current_numbers
    
