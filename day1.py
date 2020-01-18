import math


def get_fuel(mass):
  fuel = math.floor(mass / 3) - 2

  if fuel <= 0:
      return 0

  return fuel + get_fuel(fuel)


with open('day1_input', 'r') as f:
    total_fuel = 0
    for line in f:
        total_fuel += get_fuel(int(line))
    print(total_fuel)