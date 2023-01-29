x = [int(e) for e in input().split()]
n = int(input())
rot_last= x[-n:]
rot_first= x[:-n]

slice_first = x[:n]
slice_last = x[n:]


print(rot_last + rot_first)
print(slice_last + slice_first)

