from MMD_S import funkcja

data = input()

data = data.rsplit(" ")
for i in range(len(data)):
    data[i] = int(data[i])

print(funkcja(data))
