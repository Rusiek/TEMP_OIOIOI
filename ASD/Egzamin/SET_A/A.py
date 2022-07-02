def get_input():
    temp = input().rsplit(" ")
    n, q = int(temp[0]), int(temp[1])

    tab = input().rsplit(" ")
    for i in range(n):
        tab[i] = int(tab[i])

    query = [input().rsplit(" ") for _ in range(q)]
    for i in range(q):
        query[i] = (int(query[i][0]), int(query[i][1]))

    return n, q, tab, query

def print_output(data):
    for line in data:
        print(line)

# function should return an array where 
# on i-th position is anwser for i-th query
def function(n, q, tab, query):
    # Enter code here
    return [0]

if __name__ == "__main__":
    data = get_input()
    print_output(function(data[0], data[1], data[2], data[3]))
