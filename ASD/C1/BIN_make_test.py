import random

# Testy mini
test_num = 1000
for test in range(test_num):

    file = open(f"BIN/BINa_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("5\n")
    x = random.randint(1, 10)
    tab = [random.randint(-50, 50) for _ in range(x)]
    tab.sort()
    for i in tab:
        file.write(str(i))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(3):
        file.write(f"{str(random.randint(-50, 50))}\n")
    for i in range(2):
        file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()


test_num = 20
for test in range(test_num):

    file = open(f"BIN/BINb_{'{:0>2}'.format(str(test))}.in", "w+")
    file.write("50\n")
    x = 10 ** 4
    tab = [random.randint(-10**9, 10**9) for _ in range(x)]
    tab.sort()
    for i in tab:
        file.write(str(i))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(30):
        file.write(f"{str(random.randint(-10**9, 10**9))}\n")
    for i in range(20):
        file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()

test_num = 1
for test in range(test_num):

    file = open(f"BIN/BINc_.in", "w+")
    file.write(f"{10 ** 5}\n")
    x = 10 ** 5
    tab = [random.randint(-10**9, 10**9) for _ in range(x)]
    tab.sort()
    for i in tab:
        file.write(str(i))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(6 * 10 ** 4):
        file.write(f"{str(random.randint(-10**9, 10**9))}\n")
    for i in range(4 * 10 ** 4):
        file.write(f"{str(tab[random.randint(0, x - 1)])}\n")

    file.close()