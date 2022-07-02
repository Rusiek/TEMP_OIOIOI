def get_input():
    temp = input().rsplit(" ")
    n, k = int(temp[0]), int(temp[1])

    a, t = input().rsplit(" "), input().rsplit(" ")
    for i in range(n):
        a[i], t[i] = int(a[i]), int(t[i])

    return n, k, a, t

# function should return an integer
def function(n, k, a, t):
    # Enter code here
    return 0

if __name__ == "__main__":
    data = get_input()
    print(function(data[0], data[1], data[2], data[3]))
