import random


def gen_test(string, n, r):
    file = open(string, "w+")
    
    file.write(f"{n}\n")
    for i in range(n):
        x = [random.randint(1, r) for _ in range(2)]
        x.sort()
        file.write(f"{x[0]} {x[1]}")
        if (i != n - 1):
            file.write("\n")
        
    file.close()


test_num    =   100
for i in range(test_num):
    length  =   random.randint(1, 8)
    r       =   9
    gen_test(f"OFF_2\\A\\OFF_2a{'{:0>2}'.format(str(i))}.in", length, r)
        
# test_num    =   100
# for i in range(test_num):
#     length  =   1000
#     r       =   10 ** 6
#     gen_test(f"OFF_2\\B\\OFF_2b{'{:0>2}'.format(str(i))}.in", length, r)

# test_num    =   20
# for i in range(test_num):
#     length  =   2 * 10 ** 4
#     r       =   10 ** 7
#     gen_test(f"OFF_2\\C\\OFF_2c{'{:0>2}'.format(str(i))}.in", length, r)

# test_num    =   20
# for i in range(test_num):
#     length  =   2 * 10 ** 5
#     r       =   10 ** 8
#     gen_test(f"OFF_2\\D\\OFF_2d{'{:0>2}'.format(str(i))}.in", length, r)
