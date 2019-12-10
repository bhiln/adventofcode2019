import math

def calculate_fuel(mass):
  required_fuel = int(math.floor(mass/3))-2
  print (required_fuel)
  if required_fuel <= 0:
    return 0
  else:
    return required_fuel + calculate_fuel(required_fuel)

total_fuel = 0
with open("mass.txt",'r') as f:
  for cnt, line in enumerate(f):
    mass = float(line)
    required_fuel = calculate_fuel(mass)
    total_fuel += required_fuel
print(total_fuel)