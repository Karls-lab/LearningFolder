# MSE equation in python
# this equation includes the 1/2n factor instead of 1/n

data = {
    "actual": [399.9, 329.9, 369, 350.4],
    "predicted": [401.5, 320.7, 375.2, 348.5]
}

def mse(data):
    n = len(data["actual"])
    sum = 0
    for i in range(n):
        sum += (data["actual"][i] - data["predicted"][i]) ** 2
    return (1 / (2 * n)) * sum

print(mse(data))