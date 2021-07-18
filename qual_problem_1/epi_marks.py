from pathlib import Path

base_path = Path.home()

with open(base_path / "input_test.txt", "r") as infile, open(base_path / "output_test.txt", "w") as outfile:
    num_tests = int(infile.readline().strip("\n").strip("\r"))
    for test in range(num_tests):
        all_states = {}
        state_counter = 0
        output = []
        n, l = infile.readline().strip("\n").strip("\r").split(" ")
        inputs = []
        for s in range(int(n)):
            inputs.append(infile.readline().strip("\n").strip("\r"))
        for pos in range(int(l)):
            state = ""
            for s in inputs:
                state += s[pos]
            if state in all_states:
                output.append(all_states[state])
            else:
                state_counter += 1
                all_states[state] = state_counter
                output.append(state_counter)

        outfile.write(str(state_counter) + "\n")
        outfile.write(" ".join([str(i) for i in output]) + "\n")
