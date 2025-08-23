# Exercice 5: déchet polluant 

N,M = list(map(int,input().split()))
stck = list(map(int,input().split()))
chargement = ""
def findMax(s):
    i = 0
    for j in range(len(s)):
        if s[j]>s[i]:
            i = j
    return s.pop(i)

for k in range(M):
    chargement += " "+str(findMax(stck))

print(chargement[1:])
