def get_input():
    t = int(input())
    query_data, query_tab = [], []
    for _ in range(t):
        query_data.append(input().rsplit(" "))
        query_tab.append(input().rsplit(" "))
        query_data[-1] = (int(query_data[-1][0]), int(query_data[-1][1]))
        for i in range(len(query_tab[-1])):
            query_tab[-1][i] = int(query_tab[-1][i])

    return t, query_data, query_tab

def boolean(x):
    if x:
        return "Yes"
    else:
        return "No"

# function should return a boolean for a single query!
def function(n, k, tab):
    # Enter code here
    return True

if __name__ == "__main__":
    data = get_input()
    for i in range(data[0]):
        print(boolean(function(data[1][i][0], data[1][0][1], data[2][i])))