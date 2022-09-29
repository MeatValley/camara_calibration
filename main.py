import numpy as np
import camera_calibration_utils as cc


p_img = np.array([
    [253.2, 337.8],
    [82.3, 351.1],
    [389.3, 371.6],
    [334.2, 141.1],
    [62.7, 378.7],
    [27.1, 106.4],
    [537.4, 363.3],
    [511.6, 274.6],
    [589, 122.4],
    [337.2, 328.9],
    [75.5, 287],
    [241.9, 368.9],
    [307.5, 515] 
    ]
)

p_world = np.array([
    [0, 2.7, 7],
    [0, 15, 3],
    [4.5, 0, 5],
    [0, 0, 14],
    [0, 17.8, 0],
    [0, 17.8, 14],
    [22.5, 0, 0],
    [15, 0, 7.5],
    [22.5, 0, 14],
    [8, 0, 1],
    [0, 15, 6],
    [0, 5, 5],
    [0, 0, 0]
    ]
)

# cc.read_img('Well_know_obj.png')


A = cc.generate_matrix_A(p_img, p_world)

P = cc.get_P(A)
K = cc.get_intrinsic_matrix(p_img, p_world)

print(K)

# for i in range(3):
#     for j in range(3):
#         format_float = "{:.2f}".format(K[i][j])
#         print(format_float, end="")
#         print("  ", end="")
        