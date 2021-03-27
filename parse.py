import numpy as np
import matplotlib.pyplot as plt

file_name = "only_time.csv"
with open(file_name, "r") as f:
    times = f.readlines()

# ヘッダを削除
times.pop(0)

# DNF を削除
times = [float(s.rstrip("\n")) for s in times if not s.startswith("DNF")]

times = np.array(times)

print(f"mean: {np.mean(times)}")
plt.plot(times)
plt.show()
plt.hist(times)
plt.show()
