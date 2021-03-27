import numpy as np
import matplotlib.pyplot as plt
import time

file_name = input()
with open(file_name, "r") as f:
    times = f.readlines()

for i, line in enumerate(times):
    l = line.rstrip("\n").split(",")
    print(f"\r {l}      ", end="")
    time.sleep(1)
