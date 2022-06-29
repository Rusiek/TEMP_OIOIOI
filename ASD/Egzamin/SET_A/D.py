def get_input():
    t = int(input())
    query = [input().rsplit(" ") for _ in range(t)]
    for i in range(t):
        query[i] = (int(query[i][0]), int(query[i][1]))
    return t, query

# function should return an integer for a single query!
def function(query):
    # Enter code here
    return 0

if __name__ == "__main__":
    data = get_input()
    for i in range(data[0]):
        print([function(data[1][i]) for i in range(data[0])])