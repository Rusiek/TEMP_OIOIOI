from doctest import OutputChecker
import zad1

class Node:
    def __init__(self):
        self.val    =   None
        self.next   =   None

def list2tab(l):
    output = []

    while l != None:
        output.append(l.val)
        l = l.next

    return output

def tab2list(tab):
    head        =   Node()
    head.val    =   tab[0]
    temp        =   head

    for i in range(1, len(tab)):
        temp.next   =   Node()
        temp        =   temp.next
        temp.val    =   tab[i]

    return head


k = int(input())
data = input()

data = data.rsplit(" ")
for i in range(len(data)):
    if data[i].rfind(".") == -1:
        data[i] = int(data[i])
    else:
        data[i] = float(data[i])
    
linked_list     =   tab2list(data)
linked_list     =   zad1.SortH(linked_list, k)
output          =   list2tab(linked_list)

for i in output:
    print(i, end=" ")
