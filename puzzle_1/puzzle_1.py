
with open('input.txt') as f:
    raw_input = f.read()
depth_measurements = [eval(depth) for depth in raw_input.split('\n') if depth != '']

depth_increments = [idx + 1 for idx, prev_depth in enumerate(depth_measurements[:-1])
                    if prev_depth < depth_measurements[idx+1]]
print(len(depth_increments))
