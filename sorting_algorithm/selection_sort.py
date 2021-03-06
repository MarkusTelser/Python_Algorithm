import time


def sort(array):
    print("Selection sort running...")
    start = time.time()
    result = array.copy()
    for i in range(0, len(result) - 1):
        paste = i
        for j in range(i + 1, len(result)):
            if result[j] < result[paste]:
                paste = j
        x, y = result[i], result[paste]
        result[i], result[paste] = y, x
    end = time.time()
    print("Selection sort finished")
    return result, end - start
