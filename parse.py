import scipy as sp
import matplotlib.pyplot as plt

header = input().split(",")
times = sp.array([])

for i in range(6145):
    times = sp.append(times, input.split(","))

print(times[:, -1])
