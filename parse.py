import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set_style("darkgrid")


def rolling_average(row_time: int, num_rolling:int):
    rolling_time = np.convolve(row_time, np.ones(num_rolling)/num_rolling, mode="same")
    return rolling_time


file_name = "only_time.csv"
with open(file_name, "r") as f:
    times = f.readlines()

# ヘッダを削除
times.pop(0)

# DNF を削除
times = [float(s.rstrip("\n")) for s in times if not s.startswith("DNF")]
times = np.array(times)

times_rolling = rolling_average(times, 5)

print(f"mean: {np.mean(times)}")

plt.plot(times)
plt.plot(times_rolling)
plt.show()

""" plt.hist(times, bins=100, density=True)
plt.show()
"""
