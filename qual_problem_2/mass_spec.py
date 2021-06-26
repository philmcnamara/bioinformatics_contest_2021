from bisect import bisect_left
from pathlib import Path
import numpy as np

base_path = Path.home()

with open(base_path / "input_test.txt", "r") as infile, open(base_path / "output_test.txt", "w") as outfile:
    num_tests = int(infile.readline().strip("\n").strip("\r").rstrip(" "))
    for test in range(num_tests):
        m, a, s = infile.readline().strip("\n").strip("\r").rstrip(" ").split(" ")

        # dictionaries map masses and adducts to their ids
        masses = dict(enumerate([float(i) for i in infile.readline().strip("\n").strip("\r").rstrip(" ").split(" ")], 1))
        adducts = dict(enumerate([float(i) for i in infile.readline().strip("\n").strip("\r").rstrip(" ").split(" ")], 1))
        obs_signals = [float(i) for i in infile.readline().strip("\n").strip("\r").rstrip(" ").split(" ")]

        result = []

        exp_signal_dict = {}
        
        # max possible size is m * a
        exp_signal_list = np.empty(shape=int(m) * int(a), dtype=float)

        index = 0
        for m in masses:
            for a in adducts:
                # need to round since we are using floats
                exp_signal = round(masses[m] + adducts[a], 6)
                # add all non-zero masses to the expected signal list
                if exp_signal > 0:
                    exp_signal_dict[exp_signal] = (m, a)
                    exp_signal_list[index] = exp_signal
                    index += 1

        # remove unused indices due to negative mass combinations of m and a
        exp_signal_list = exp_signal_list[:index]
        exp_signal_list.sort()

        # finding closest value in sorted list is best accomplished with bisect
        for obs_signal in obs_signals.values():
            pos = bisect_left(exp_signal_list, obs_signal)
            # last value case
            if pos == len(exp_signal_list):
                val = exp_signal_list[pos - 1]
                outfile.write(" ".join(str(i) for i in exp_signal_dict[val]) + "\n")
            else:
                val_1 = exp_signal_list[pos]
                val_2 = exp_signal_list[pos - 1]
                # decide between the best values on either side of pos
                if abs(val_2 - obs_signal) < abs(val_1 - obs_signal):
                    outfile.write(" ".join(str(i) for i in exp_signal_dict[val_2]) + "\n")
                else:
                    outfile.write(" ".join(str(i) for i in exp_signal_dict[val_1]) + "\n")