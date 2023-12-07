t = input().split(":")[1].strip().split(" ")
ti = ""
for i in range(len(t)):
    if t[i] != "":
        ti += t[i]
t = int(ti)


print(t)
# t = int(t)
d = input().split(":")[1].strip().split(" ")
di = ""
for i in range(len(d)):
    if d[i] != "":
        di += d[i]
d = int(di)
print(d)

total = 0

w = 0
for j in range(1, t):
    s = j
    r = t-j
    if d < s*r:
        w += 1
print(w)