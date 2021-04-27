import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set_style("darkgrid")


def rolling_average(row_time: int, num: int):
    rolling_time = np.convolve(row_time, np.ones(num)/num, mode="same")
    # TODO: 内包リストみたいなのとかで、多分一行でフィルタできると思う
    rolling_time[:num-1] = np.NaN
    rolling_time[1-num:] = np.NaN
    return rolling_time


file_name = "only_time.csv"

with open(file_name, "r") as f:
    times = f.readlines()

# ヘッダを削除
times.pop(0)

# DNF を削除
# TODO: 削除するんじゃなくて np.NaN でreplace した方が良いんじゃない？
times = [float(s.rstrip("\n")) for s in times if not s.startswith("DNF")]

# 添字をどこ以降から取るか
id_start = len(times) - 1000
times = np.array(times[id_start:])

times_rolling = rolling_average(times, 12)
times_rolling_12 = rolling_average(times, 50)

print(f"mean: {np.mean(times)}")

plt.title("3×3 averages")
plt.plot(times, label="row")
plt.plot(times_rolling, label="ao5")
plt.plot(times_rolling_12, label="ao100")
plt.legend()
plt.savefig("scores.png", dpi=1000)

""" plt.hist(times, bins=100, density=True)
plt.show()
"""
