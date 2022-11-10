
with open('input.txt') as f:
    raw_input = f.read()
depth_measurements = [eval(depth) for depth in raw_input.split('\n') if depth != '']

window_size = 3
prev_window_sum = sum(depth_measurements[0:window_size])
number_of_increments = 0
for idx in range(1, len(depth_measurements) - window_size + 1):
    curr_window_sum = sum(depth_measurements[idx:idx+window_size])
    if curr_window_sum > prev_window_sum:
        print(f"{idx}-{idx+window_size}: {curr_window_sum} > {prev_window_sum}")
        number_of_increments += 1
    prev_window_sum = curr_window_sum

print(number_of_increments)
