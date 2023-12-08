from collections import OrderedDict
        
crds = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
crds = crds[::-1]

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
    

def value(s):
    val = 0
    s = s[::-1]
    for i in range(5):
        # print(crds.index(s[i]))
        val = val + ((crds.index(s[i])+1)*(14**i))
        
    return val



for i in range(0,1000):
    inp = input().split(" ")
    # print(value(inp[0]))
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
    
        
cnt = 1

for key in a.keys():
    v = value(a[key])
    a[key] = v
# sorted_a = OrderedDict(sorted(a.items()))

for key in b.keys():
    v = value(b[key])
    b[key] = v
# sorted_b = OrderedDict(sorted(b.items()))

for key in c.keys():
    v = value(c[key])
    c[key] = v
# sorted_c = OrderedDict(sorted(c.items()))

for key in d.keys():
    v = value(d[key])
    d[key] = v
# sorted_d = OrderedDict(sorted(d.items()))

for key in e.keys():
    v = value(e[key])
    e[key] = v
# sorted_e = OrderedDict(sorted(e.items()))

for key in f.keys():
    v = value(f[key])
    f[key] = v
# sorted_f = OrderedDict(sorted(f.items()))

for key in g.keys():
    v = value(g[key])
    g[key] = v
# sorted_g = OrderedDict(sorted(g.items()))

sorted_a = dict(sorted(a.items(), key=lambda item: item[1]))
sorted_b = dict(sorted(b.items(), key=lambda item: item[1]))
sorted_c = dict(sorted(c.items(), key=lambda item: item[1]))
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_e = dict(sorted(e.items(), key=lambda item: item[1]))
sorted_f = dict(sorted(f.items(), key=lambda item: item[1]))
sorted_g = dict(sorted(g.items(), key=lambda item: item[1]))





if sorted_g != {}:
    g_keys = list(sorted_g.keys())
    for i in range(len(sorted_g)):
        pool = pool + (cnt*int(g_keys[i]))
        cnt += 1
        
if sorted_f != {}:
    f_keys = list(sorted_f.keys())
    for i in range(len(sorted_f)):
        pool = pool + (cnt*int(f_keys[i]))
        cnt += 1
        
if sorted_e != {}:
    e_keys = list(sorted_e.keys())
    for i in range(len(sorted_e)):
        pool = pool + (cnt*int(e_keys[i]))
        cnt += 1
        
if sorted_d != {}:
    d_keys = list(sorted_d.keys())
    for i in range(len(sorted_d)):
        pool = pool + (cnt*int(d_keys[i]))
        cnt += 1

if sorted_c != {}:
    c_keys = list(sorted_c.keys())
    for i in range(len(sorted_c)):
        pool = pool + (cnt*int(c_keys[i]))
        cnt += 1
        
if sorted_b != {}:
    b_keys = list(sorted_b.keys())
    for i in range(len(sorted_b)):
        pool = pool + (cnt*int(b_keys[i]))
        cnt += 1
        
if sorted_a != {}:
    a_keys = list(sorted_a.keys())
    for i in range(len(sorted_a)):
        pool = pool + (cnt*int(a_keys[i]))
        cnt += 1
        
print(pool)