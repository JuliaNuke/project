import os
import sys

from collections import defaultdict

if len(sys.argv) < 2:
    print("Provide path to directory")
    exit(1)

def get_upper_10(number):
    multiply = 10
    while number % multiply != number:
        multiply *= 10
    return multiply

target_dir = sys.argv[1]
result = defaultdict(int)

for item in os.listdir(target_dir):
    if os.path.isdir(item):
        continue
    file = os.path.join(target_dir, item)
    file_stats = os.stat(file)
    key = get_upper_10(file_stats.st_size)
    result[key] += 1

print(result)
