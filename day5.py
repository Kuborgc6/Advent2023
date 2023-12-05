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

