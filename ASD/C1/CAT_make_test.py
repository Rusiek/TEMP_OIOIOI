import random

# Testy mini
test_num = 1000
for test in range(test_num):

    file = open(f"CAT/A/CATa_{'{:0>3}'.format(str(test))}.in", "w+")
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
            file.write(f"{str(random.randint(1, 20))}\n")
        else:
            rand1 = random.randint(0, x - 1)
            rand2 = random.randint(0, x - 1)
            file.write(f"{str(abs(tab[rand1] - tab[rand2]))}\n")

    file.close()


test_num = 20
for test in range(test_num):

    file = open(f"CAT/B/CATb{'{:0>2}'.format(str(test))}.in", "w+")
    file.write("50\n")
    x = 2 * 10 ** 3
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
            file.write(f"{str(random.randint(1, 10**9))}\n")
        else:
            rand1 = random.randint(0, x - 1)
            rand2 = random.randint(0, x - 1)
            file.write(f"{str(abs(tab[rand1] - tab[rand2]))}\n")

    file.close()

test_num = 1
for test in range(test_num):

    file = open(f"CAT/C/CATc_.in", "w+")
    file.write(f"{10 ** 3}\n")
    x = 10 ** 5
    tab = [random.randint(-10**9, 10**9) for _ in range(x)]
    tab.sort()
    for i in range(len(tab)):
        file.write(str(tab[i]))
        if i != x - 1:
            file.write(" ")
    
    file.write("\n")
    for i in range(10 ** 3):
        a = random.randint(0, 1)
        if a == 0:
            file.write(f"{str(random.randint(1, 10**9))}\n")
        else:
            rand1 = random.randint(0, x - 1)
            rand2 = random.randint(0, x - 1)
            file.write(f"{str(abs(tab[rand1] - tab[rand2]))}\n")

    file.close()