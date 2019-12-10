import math
total_fuel = 0
with open("mass.txt",'r') as f:
  for cnt, line in enumerate(f):
    mass = float(line)
    required_fuel = int(math.floor(mass/3))-2
    total_fuel += required_fuel
print(total_fuel)
