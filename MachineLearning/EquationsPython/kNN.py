data = {
    '1': {'x1': 3.4, 'x2': 2.1, 'x3': 3.8, 'y': 0, 'distance': 0},
    '2': {'x1': -9.2, 'x2': 2.9, 'x3': 0, 'y': 1, 'distance': 0},
    '3': {'x1': 6.1, 'x2': 2, 'x3': 4.4, 'y': 0, 'distance': 0}
}

def euclideanDistance(x1, y1, x2, y2, x3, y3):
    return ((x1 - y1) ** 2 + (x2 - y2) ** 2 + (x3 - y3) ** 2) ** 0.5

def kNN(data, k, x1, x2, x3):
    for i in data:
        print(f'Calculating distance for value: {i}, x: {x1, x2, x3}, y: {data[i]["x1"], data[i]["x2"], data[i]["x3"]}')
        distance = euclideanDistance(data[i]['x1'], x1, data[i]['x2'], x2, data[i]['x3'], x3)
        data[i]['distance'] = distance
        print(f'value: {i}, distance: {round(distance, 4)}')

    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['distance'])}
    nearest = list(data.items())[:k]
    print(f'Nearest {k} in order: {nearest}')
    print(f'Nearest {k} distances: {[round(i[1]["distance"], 4) for i in nearest]}')
    print(f'Nearest {k} values: {[i[0] for i in nearest]}')

    labels = []
    for i in nearest:
        labels.append(i[1]['y'])
    print(f'Labels: {labels}')

kNN(data, 1, -4.5, 3.7, -1)
