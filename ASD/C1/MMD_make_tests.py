import random

# Testy mini
test_num = 1000
for test in range(test_num):

    file = open(f"MMD/MMDa_{'{:0>3}'.format(str(test))}.in", "w+")
    x = random.randint(1, 10)
    for i in range(x):
        file.write(f"{str(random.randint(-50, 50))}")
        if i != x - 1:
            file.write(" ")
    
    file.close()

# Testy maxi
test_num = 1
for test in range(test_num):
    
    file = open(f"MMD/MMDb.in", "w+")
    x = 10 ** 7
    for i in range(x):
        file.write(f"{str(random.randint(-10 ** 8, 10 ** 8))}")
        if i != x - 1:
            file.write(" ")
    
    file.close()