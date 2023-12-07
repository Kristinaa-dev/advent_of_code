from collections import OrderedDict

pool = 0
a = {}
b = {}
c = {}
d = {}
e = {}
f = {}
g = {}

def five(s):
    if len(set(s)) == 1:
        return True
    return False

def four(s):
    s = list(s)
    s.sort()
    if s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return True
    return False

def full(s):
    if len(set(s)) == 2:
        return True
    return False
def three(s):
    if len(set(s)) == 3:
        s = list(s)
        s.sort()
        if s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
            return True
    return False

def two(s):
    if len(set(s)) == 3:
        return True
    return False

def one(s):
    if len(set(s)) == 4:
        return True
    return False

def high(s):
    if len(set(s)) == 5:
        return True
    return False
    




for i in range(0,5):
    inp = input().split(" ")
    if five(inp[0]):
        a.update({inp[1]:inp[0]})
    elif four(inp[0]):
        b.update({inp[1]:inp[0]})
    elif full(inp[0]):
        c.update({inp[1]:inp[0]})
    elif three(inp[0]):
        d.update({inp[1]:inp[0]})
    elif two(inp[0]):
        e.update({inp[1]:inp[0]})
    elif one(inp[0]):
        f.update({inp[1]:inp[0]})
    else:
        g.update({inp[1]:inp[0]})
    
        
crds = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
crds = crds[::-1]




print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
    
    
cnt = 1
g_sort = []
# for i in range(len(g)):
#     if g[i][0] == "S":
#         pool += 1
# print(e.sort())
# e = sorted(e, key=lambda x: x[0])



sorted_e = OrderedDict(sorted(e.items()))
print(sorted_e)