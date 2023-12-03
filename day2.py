cnt = 0
# l = []
for i in range(1,101):

    inp = input()
    inp = inp.split(":")
    inp = inp[1]
    inp = inp.split(";")
    # print(inp)
    c = True
    r = 0
    g = 0
    b = 0
    for k in inp:
        t = k.split(",")
        for j in range(len(t)):
            a = t[j].strip().split(" ")
            if a[1] == "red":
                r = max(r, int(a[0]))
            elif a[1] == "green":
                g = max(g, int(a[0]))
            elif a[1] == "blue":
                b = max(b, int(a[0])) 
            # print(r,g,b)
    cnt += (r*g*b)
print(cnt)