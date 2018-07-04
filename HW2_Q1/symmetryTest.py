import transposeMatrix

def symmetry_test(x):
    if x == transposeMatrix.to_transpose(x, False):
        print("The matrix is symmetric. AKA self-adjoint.")
    else:
        print("The matrix is not symmetric.")
