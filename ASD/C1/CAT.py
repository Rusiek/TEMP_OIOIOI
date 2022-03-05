from CAT_S import funkcja

q = int(input())
data = input()
data = data.rsplit(" ")
for i in range(len(data)):
    data[i] = int(data[i])

for i in range(q):
    x = int(input())
    print(funkcja(data, x))