s = 0
n = ""
ok = False

posx = (-1, -1, -1, 0, 1, 1, 1, 0)
posy = (-1, 0, 1, 1, 1, 0, -1, -1)

def issymbol(x):
    return x!='.' and not ( x in [str(i) for i in range(10)] )


with open("input.txt") as file:
    M = file.read().splitlines()
    for i,sublist in enumerate(M):
        for j,val in enumerate(sublist):
            if M[i][j].isdigit():
                n+=M[i][j]
                if ok is False:
                    for k in range(8):
                        try:
                            if issymbol(M[i + posx[k]][j + posy[k]]): ok = True
                        except: continue
            else:
                if ok is True: s+=int(n)
                n = ""
                ok = False
print(s)