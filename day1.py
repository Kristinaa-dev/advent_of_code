total = 0

# def find(s):
#     f = -1
#     i = 0
#     lst = -1
#     fst = -1
#     words = ["one","two","three","four","five","six","seven","eight","nine"]
#     if len(s) < 5:
#         for j in words:
#             if j in s:
#                 word = words.index(j)
#                 if fst == -1:
#                     fst = word+1
#                 lst = word+1
                
#     for i in range(len(s)-4):
#         print(i,s[i],fst)
#         if s[i] in ["1","2","3","4","5","6","7","8","9"]:
#             print(s[i],fst)
#             if fst == -1:
                
#                 print("FUCK YOu")
#                 fst = int(s[i])
#             lst = int(s[i])
#         for j in words:
#             if j in s[i:i+5]:
#                 word = words.index(j)
#                 if fst == -1:
#                     fst = word+1
#                 lst = word+1

#     for i in range(len(s)-4, len(s)):
#         if s[i] in ["1","2","3","4","5","6","7","8","9"]:
#             if fst == -1:
#                 fst = int(s[i])
#             lst = int(s[i])   
#     return str(fst), str(lst)
# print(find("2ones3dasd"))
    
def find(s):
    s = (s.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine"))
    fst = -1
    lst = -1
    
    for i in range(len(s)):
        if s[i] in ["1","2","3","4", "5", "6", "7", "8","9"]:
            fst = s[i]
    s = s[::-1]
    for i in range(len(s)):
        if s[i] in ["1","2","3","4", "5", "6", "7", "8","9"]:
            lst = s[i]
    return fst, lst
while True:
    inp = input()
    if inp == "STOP":
         break
    n = find(inp)
    # print(n)
    n = n[0] + n[-1]
    total += int(n)
    
print(total)


import re

with open("input") as f:
    data = f.read().strip()


def calibration(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)


data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)
print(calibration(data))
