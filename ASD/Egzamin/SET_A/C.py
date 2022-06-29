def get_input():
    n = int(input())
    tab = input().rsplit(" ")
    for i in range(n):
        tab[i] = int(tab[i])
    return n, tab

def print_output(tab):
    for i in tab:
        print(i, end = " ")

# function should return an array where
# on i-th position is an anwser when the i-th
# student was the first one caught by the teacher
def function(n, tab):
    # Enter code here
    return [0]

if __name__ == "__main__":
    data = get_input()
    print_output(function(data[0], data[1]))