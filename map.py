import random

def getfriendlyneighbors(m,c,t):
    return list(set().intersection(getneighbors(m, t), allofcolor(m, c)))

def getneighbors(m,t): #takes position
    width = len(m.split("\n")[0])+1
    return [t-1, t+1, t-width, t+width]

def allofcolor(m,c):
    out = []
    for i in range(len(m)):
        if m[i] == c:
            out.append(i)
    return out

def randomland(m):
    return randomcond(m,lambda tile: tile not in "0\n" )

def rlandneighbor(m,t): #takes position
    while True:
        pos = random.choice(getneighbors(m,t))
        if 0 <= pos < len(m) and m[pos] not in "0\n":
            return pos

def randomunclaimed(m):
    return randomcond(m,lambda tile: tile == "1" )

def randomcond(m,c):
    while True:
        pos = random.randint(0,len(m)-1)
        if c(m[pos]):
            return pos