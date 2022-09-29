# camara_calibration

This is a simple program just to put in pratic the knowledge. We want to find the intrinsic matrix K and extrinsic matrix [R T] of a camera
so in order to do that, I just follow this steps
1) Took a picture with the desired camera of a well know object, with some random points in it. The idea is to measure this points coordinates in the world coordinate frame and in the image by pixels. 
2)Wrote all the coordinates in the world coordinate frame and in the image. To the image I just measure it by the plt lib that allows us to see the coordinates just by passing the mouse. After that I create the Pw np array - a [13,3] array with the (xw yw zw) of every point in the world coordinate frame and; and the Pi np array - a [13,2] with the pixels of the same indexed points in the image that I took.

3) We know that:
p_img = K * [R T] * p_world
(we need to add 1 at p_img and p_world, we do that bc we use homogeneous coordinates (2D->3D), K * [R T] = P), we can wirte that to each point and them solve the system to P as a variable (P has 12 coordinates)
after reoorginazing the matrix we have: A * P = 0
we need to find this matrix A, which is just a little of Linear Algebra

4)After retriving A from p_img and p_world, we can find P, what is done in function get_P
the main Idea is that A*P = 0, we want to find the P that makes this happen. there is a good fact that we can use, is that the matrix P acts on homogeneous coordinates, so it isnt affected by any scalar, therefore we can set the scale of P, so we force ||P||^2 = 1. Why? Bc now we have:
we want to minimize A*P = 0 so that ||P||^2 = 1, that is, the same as minimize ||A*P||^2, and that is
min (P_T * A_T * A * P) such that P_T * P = 1
thats a well known problems and we can define a loss function L(P,x)
L(P,x) = P_T * A_T * A * P - x * (P_T * P -1)
and wanna minimizes L, so we take the derivitati in p and we have the eigenvalue problem
so we just create a function that give us the eigenvector associated to the min eigenvalue, and ther is our P

5)we know that P = K * [R T],that is easily solved
 we find K and R by P[:3, :3] with QR decomposition (since R is orthonormal and K is upper triangle)
T can be easly retrived by the last column of P and K^-1
