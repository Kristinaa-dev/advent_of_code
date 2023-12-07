t = input().split(":")[1].strip().split(" ")
t = [int(x) for x in t if x != ""]

d = input().split(":")[1].strip().split(" ")
d = [int(x) for x in d if x != ""]


total = 1
for i in range(len(t)):
    w = 0
    for j in range(1, t[i]):
        s = j
        r = t[i]-j
        if d[i] < s*r:
            w += 1
        # print(w)
    total *= w
print(total)