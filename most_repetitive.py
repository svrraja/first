from collections import Counter

L1 = [1, 2, 2, 3, 2, 3, 4, 5]

counter = Counter(L1)
most_common = counter.most_common(1)[0]  # (element, count)

print(f"The most repetitive element is {most_common[0]} (appeared {most_common[1]} times).")