
def generate_matrix(rows, cols, min_value, max_value):
    import numpy as np
    
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - rows // 2)**2 + (j - cols // 2)**2)
            cell = np.random.randint(min_value, max_value + 1)*(1 - (distance/max(rows, cols))*0.5)
            matrix[i, j] = max(round(cell, 2), 0)

    return matrix

matrix_data = generate_matrix(8, 8, 8, 10)
print(matrix_data)


