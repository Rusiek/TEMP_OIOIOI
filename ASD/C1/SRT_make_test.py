import random

# Testy mini
test_num = 1000
for test in range(test_num):

    file = open(f"SRT/SRTa_{'{:0>3}'.format(str(test))}.in", "w+")
    x = random.randint(1, 10)
    for i in range(x):
        file.write(f"{str(random.randint(-50, 50))}")
        if i != x - 1:
            file.write(" ")
    
    file.close()

# Testy O(n^2)
test_num = 20
for test in range(test_num):

    file = open(f"SRT/SRTb_{'{:0>2}'.format(str(test))}.in", "w+")
    x = 10 ** 4
    for i in range(x):
        file.write(f"{str(random.randint(-10 ** 9, 10 ** 9))}")
        if i != x - 1:
            file.write(" ")
    
    file.close()

# Testy O(n*log(n))
test_num = 1
for test in range(test_num):

    file = open(f"SRT/SRTc.in", "w+")
    x = 4 * 10 ** 6
    for i in range(x):
        file.write(f"{str(random.randint(-10 ** 9, 10 ** 9))}")
        if i != x - 1:
            file.write(" ")
    
    file.close()