import numpy as np


def reshape_rows(values, width):
    arr = np.asarray(values, dtype=float)
    if width <= 0 or arr.size % width != 0:
        return []
    return arr.reshape(-1, width).round(6).tolist()


def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    return arr[np.ix_(rows, columns)].round(6).tolist()


def column_means(matrix):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return []
    return arr.mean(axis=0).round(6).tolist()


def column_range(matrix, column):
    arr = np.asarray(matrix, dtype=float)
    if arr.size == 0:
        return 0.0
    col = arr[:, column]
    return round(float(col.max() - col.min()), 6)