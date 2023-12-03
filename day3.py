result = 0
a = []

while True:
    inp = input()
    if inp == "end":
        break
    a.append(inp)
    


def search(i,j,tmp_j):

    if i < len(a)-1:
        for k in range(j, tmp_j+1):
            if a[i+1][k] != "." and a[i+1][k].isnumeric() == False:
                return True
        if j != 0:
            if a[i][j-1] != "." and a[i][j-1].isnumeric() == False:
                return True
            if a[i+1][j-1] != "." and a[i+1][j-1].isnumeric() == False:
                return True
        if tmp_j != len(a[i])-1:
            if a[i][tmp_j+1] != "." and a[i][tmp_j+1].isnumeric() == False:
                return True
            if a[i+1][tmp_j+1] != "." and a[i+1][tmp_j+1].isnumeric() == False:
                return True
            
    if i > 0:
        for k in range(j, tmp_j+1):
            if a[i-1][k] != "." and a[i-1][k].isnumeric() == False:
                return True
        if j != 0:
            if a[i-1][j-1] != "." and a[i-1][j-1].isnumeric() == False:
                return True
            if a[i][j-1] != "." and a[i][j-1].isnumeric() == False:
                return True
        if tmp_j != len(a[i])-1:
            if a[i-1][tmp_j+1] != "." and a[i-1][tmp_j+1].isnumeric() == False:
                return True
            if a[i][tmp_j+1] != "." and a[i][tmp_j+1].isnumeric() == False:
                return True
    
    return False

n = ""
i = 0
b = "2"
while i < len(a):
    j = 0
    while j < len(a[i]):
        if a[i][j].isnumeric():
            tmp_j = j
            while a[i][tmp_j] in "0123456789":
                n += a[i][tmp_j]
                tmp_j += 1
                if tmp_j == len(a[i]):
                    break
            s = search(i, j, tmp_j-1)
            # if n == "35":
            #     print(s,i,j,tmp_j-1)
            j = tmp_j-1
        if n != "":
            if s == True:
                result += int(n)    

        n = ""
        j += 1
        # j = j + tmp_j - j
        # print(j)
    i += 1
print(result)

# print(search(0,0,2))