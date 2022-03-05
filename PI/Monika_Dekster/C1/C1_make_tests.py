import random

test_num = 10 ** 3

# F = 1
for test in range(test_num):

    file = open(f"C1/A/C1a_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("1\n")
    
    if test < 100:
        n       = random.randint(0, 10)
        start   = random.randint(-100, 100)
        stop    = random.randint(-100, 100)
    else:
        n       = random.randint(0, 100)
        start   = 200 * (-0.5 + random.random())
        stop    = start + (200 * random.random())

    file.write(f"{n} {round(start, 5)} {round(stop, 5)}")


# F = 2
for test in range(test_num):

    file = open(f"C1/B/C1b_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("2\n")
    
    if test < 100:
        n       = random.randint(1, 10)
        file.write(f"{n}\n")

        for i in range(n): 
            file.write(f"{random.randint(-1000, 1000)} ")

        file.write("\n")

        for i in range(n): 
            file.write(f"{random.randint(-1000, 1000)} ")


    else:
        n       = random.randint(1, 100)
        file.write(f"{n}\n")

        for i in range(n):
            x   = 1000 * random.random()
            file.write(f"{round(x, 5)} ")

        file.write("\n")

        for i in range(n): 
            x   = 1000 * random.random()
            file.write(f"{round(x, 5)} ")


# F = 3
for test in range(test_num):

    file = open(f"C1/C/C1c_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("3\n")
    
    if test < 100:
        n       = random.randint(1, 10)
        file.write(f"{n}\n")

        for i in range(n): 
            file.write(f"{random.randint(-1000, 1000)} ")

        file.write("\n")

        for i in range(n): 
            file.write(f"{random.randint(-1000, 1000)} ")


    else:
        n       = random.randint(1, 100)
        file.write(f"{n}\n")

        for i in range(n):
            x   = 1000 * random.random()
            file.write(f"{round(x, 5)} ")

        file.write("\n")

        for i in range(n): 
            x   = 1000 * random.random()
            file.write(f"{round(x, 5)} ")
    
    
# F = 4
for test in range(test_num):

    file = open(f"C1/D/C1d_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("4\n")
    
    if test < 100:
        n       = random.randint(1, 10)
        s       = random.randint(-10, 10)
        file.write(f"{n} {s}\n")

        for i in range(n): 
            file.write(f"{random.randint(-1000, 1000)} ")


    else:
        n       = random.randint(1, 100)
        s       = 100 * (random.random() - 0.5)
        file.write(f"{n} {round(s, 5)}\n")

        for i in range(n):
            x   = 1000 * random.random()
            file.write(f"{round(x, 5)} ")


# F = 5
for test in range(test_num):

    file = open(f"C1/E/C1e_{'{:0>3}'.format(str(test))}.in", "w+")
    file.write("5\n")
    
    if test < 100:
        n       = random.randint(1, 10)
        start   = random.randint(-500, 500)
        step    = random.randint(-50, 50)
        file.write(f"{n} {start} {step}\n")

    else:
        n       = random.randint(1, 100)
        start   = 1000  * (random.random() - 0.5)
        step    = 100   * (random.random() - 0.5)
        file.write(f"{n} {round(start, 5)} {round(step, 5)}\n")

    