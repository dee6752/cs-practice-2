import numpy as np
values=[12, 14.5, 11, 13, 15.5, 10.5]
width=3
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.asarray(values,dtype=float)
    if (arr.size !=0)and(arr.size % width==0):
        return arr.reshape(arr.size//width, -1).tolist()
    else:
        return []
def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    selected = arr[np.ix_(rows, columns)]
    return selected.tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    return [round(float(x), 6) for x in means]

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    rng = np.ptp(col_data)
    return round(float(rng), 6)
