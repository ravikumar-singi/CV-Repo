import numpy as np


def directlineartransformation(worldpoints, picpoints):
    xyz = np.asarray(worldpoints)
    uv = np.asarray(picpoints)
    count_points = np.shape(xyz)[0]
    A = []
    for i in range(count_points):
        x = xyz[i, 0]
        y = xyz[i, 1]
        z = xyz[i, 2]
        u = uv[i, 0]
        v = uv[i, 1]
        A.append([x, y, z, 1, 0, 0, 0, 0, -u*x, -u*y, -u*z, -u])
        A.append([0, 0, 0, 0, x, y, z, 1,  -v*x, -v*y, -v*z, -v])

    A = np.asarray(A)
    U, S, V = np.linalg.svd(A)
    H = V[11, :]
    H = H.reshape(3, 4)
    H = H/H[2, 3]
    return H


def main():
    worldpoints = [[0, 36, 0], [0, 0, 36], [36, 0, 0], [0, 72, 0], [36, 36, 0],
                   [36, 72, 0], [0, 0, 72], [36, 0, 36]]
    picturepoints = [[4859.28, 1376.08], [4716.33, 2432.86], [3838.23, 2371.66], [
        4900.12, 543.923], [4032.23, 1319.92], [4057.76, 508.16], [4649, 2780], [3700.39, 2698.33]]
    outputmatrix = directlineartransformation(worldpoints, picturepoints)
    print(outputmatrix)


main()
