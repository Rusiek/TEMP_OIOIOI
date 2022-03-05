import random

# Testy mini
test_num = 1000
for test in range(test_num):

    file = open(f"BIN/A/BINa_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("5\n")
    x = random.randint(1, 10)
    tab = [random.randint(-50, 50) for _ in range(x)]
    tab.sort()
    for i in range(len(tab)):
        file.write(str(tab[i]))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(5):
        a = random.randint(0, 1)
        if a == 0:
            file.write(f"{str(random.randint(-50, 50))}\n")
        else:
            file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()


test_num = 20
for test in range(test_num):

    file = open(f"BIN/B/BINb_{'{:0>2}'.format(str(test))}.in", "w+")
    file.write("50\n")
    x = 10 ** 4
    tab = [random.randint(-10**9, 10**9) for _ in range(x)]
    tab.sort()
    for i in range(len(tab)):
        file.write(str(tab[i]))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(50):
        a = random.randint(0, 1)
        if a == 0:
            file.write(f"{str(random.randint(-10**9, 10**9))}\n")
        else:
            file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()

test_num = 1
for test in range(test_num):

    file = open(f"BIN/C/BINc_.in", "w+")
    file.write(f"{10 ** 5}\n")
    x = 10 ** 5
    tab = [random.randint(-10**9, 10**9) for _ in range(x)]
    tab.sort()
    for i in range(len(tab)):
        file.write(str(tab[i]))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(10 ** 5):
        a = random.randint(0, 1)
        if a == 0:
            file.write(f"{str(random.randint(-10**9, 10**9))}\n")
        else:
            file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()