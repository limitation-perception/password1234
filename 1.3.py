def input_data():
    n = int(input())
    data = {}
    for i in range(n):
        name = input().split(' ')
        if name[0] not in data:
            data[name[0]] = [0, 0]
        data[name[0]][0] += 1
        data[name[0]][1] += int(name[1])
    return data

def sort_data(data):
    data_sorted = []
    res = [*data.items()]
    for i in range(len(res)):
        data_sorted.append(res[i][0])
    return data_sorted


def output_data(s_data, c_data):
    n = len(s_data)
    for i in range(n):
        print(s_data[i], c_data[s_data[i]][0], c_data[s_data[i]][1])
    return None

if __name__ == '__main__':
    print("Input:")
    data_complete = input_data()
    sorted_data = sort_data(data_complete)
    sorted_data.sort()
    print(" ")
    print("Output:")
    output_data(sorted_data, data_complete)



