from BIN_S import funkcja

q = int(input())

for query in range(q):
    data = input()

    data = data.rsplit(" ")
    for i in range(len(data)):
        data[i] = int(data[i])

    print(funkcja(data))
