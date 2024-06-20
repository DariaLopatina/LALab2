import numpy as np

matrix = np.array([[4, 2],
                   [1, 3]])

def values(matrix):
    values, vectors = np.linalg.eig(matrix)
    print(values, vectors)
    for i in range(len(values)):
        Av = matrix @ vectors[:, i]
        λv = values[i] * vectors[:, i]
        print(Av)
        print(λv)

        if np.allclose(Av, λv):
            print(True)
        else:
            print(False)

values(matrix)



