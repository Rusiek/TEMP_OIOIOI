import zad1

class Node:
  def __init__(self):
    self.val = None
    self.next = None


def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q

    return p


def list2tab(l):
    t = []
    while l!=None:
        t.append(l.val)
        l = l.next

    return t


k = int(input())
data = input()

data = data.rsplit(" ")
for i in range(len(data)):
    if data[i].rfind(".") == -1:
        data[i] = int(data[i])
    else:
        data[i] = float(data[i])
    
data    =   tab2list(data)
output  =   zad1.SortH(data, k)
output  =   list2tab(output)
data.sort()

for i in data:
    print(i, end=" ")
