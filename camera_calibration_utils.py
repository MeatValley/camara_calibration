import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as LA

def read_img(name):
    """used to measure p_img using the mouse :P
        input: the paht to the image
        retur: 
    
    """

    img = cv2.imread(name)

    plt.subplot(111),plt.imshow(img)
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    print(img.shape)
    plt.show()


def generate_matrix_A(p_img, p_world):
    """takes the both coordinates to find the matrix A used to solve the problem

        p_img = Parameters * p_world

        --------
        Parameters:
        p_img: np array with the coordinates of the points maked in the image
        p_world: np array with the coordinates of the same points in the world frame

        output: the matrix A as a np.matrix
    """
    A = []
    for i in range(len(p_img)):
        a_i = np.append(p_world[i], [1])
        b_i = [0,0,0,0]
        b_i = np.append(b_i, a_i)
        temp1 = p_img[i][0] * (-1.) * a_i
        temp2 = p_img[i][1] * (-1.) * a_i
        b_i = np.append(b_i, temp2)
        a_i = np.append(a_i, [0,0,0,0])
        a_i = np.append(a_i, temp1)

        A = np.append(A, [[a_i]])
        A = np.append(A, [[b_i]]) 

        # for j in range(len(a_i)):
        #     format_float = "{:.2f}".format(a_i[j])
        #     print(format_float, end="")
        #     print("   ", end="")
        
        # print(" ")

        # for j in range(len(a_i)):
        #     format_float = "{:.2f}".format(b_i[j])
        #     print(format_float, end="")
        #     print("  ", end="")
        # print(" ")

    A = np.reshape(A, (26,12))
    A = np.asmatrix(A)

    return A

def get_P(A):
    """solve the eigenvalue proble A_tranposal * A * p = lambda * p
        which minimizes the loss function L(p, lambda)
        the p we want is the eigenvector with smallest eigenvalue
        input: Matrix A
        output: eigenvector corresponding to the smallest eigenvalue of A* A_Transposal
    """
    A_T = A.getT()
    AAT = np.matmul(A_T, A)
    eigenvalues, eigenvectors = LA.eig(AAT)
    min = np.amin(eigenvalues)
    i=0
    for eigenvalue in eigenvalues:
        if min == eigenvalue:
            p = eigenvectors[i]
        i+=1
    return p

def get_intrinsic_matrix(p_img, p_world):
    A = generate_matrix_A(p_img, p_world)
    P = get_P(A)
    K,R = np.linalg.qr(P[:3,:3])
    return R
    
def get_extrinsic_matrix(p_img, p_world):
    A = generate_matrix_A(p_img, p_world)
    P = get_P(A)
    K,R = np.linalg.qr(P[:3,:3])

    T = K.I * P[:,3]
    for i in range(len(T)):
        R = np.append(R[i],T[i])
    return R




a = np.matrix('1 2 0 1; 3 4 3 0; 3 4 3 0')
print(a[:,3])
