from BIN_S import funkcja

q = int(input())
data = input()
data = data.rsplit(" ")
for i in range(len(data)):
    data[i] = int(data[i])

for query in range(q):
    n = int(input())
    print(funkcja(data, n))
