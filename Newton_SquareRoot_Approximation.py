n = 25

threshold = 0.001
approximation = n/2     # Start with some or other guess at the answer
count = 0

while True:
    count += 1
    better = float(approximation + n/approximation) / 2
    if abs(approximation - better) < threshold:
        print("better %s" % better)
        break
    approximation = better

print("Count %s" % count)
