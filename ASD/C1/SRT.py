from SRT_S import funkcja

data = input()

data = data.rsplit(" ")
for i in range(len(data)):
    data[i] = int(data[i])

output = funkcja(data)
for i in output:
    print(i, end=" ")
