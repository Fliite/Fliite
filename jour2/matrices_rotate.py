def create_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(i*n+j+1)
    return matrix

def show_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print('')

#function that rotates a matrix 90 degrees clockwise

def rotate_mat(mat):
    #create an empty matrix
    new_mat = create_matrix(len(mat))
    #fill the new matrix with the values of the old one
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new_mat[j][len(mat)-i-1] = mat[i][j]
    return new_mat


#call rotate_mat() and show_mat() to display the rotated matrix
#execute it n times to rotate it n times from 1 to 4

def rotate_n_times(mat, n):
    for i in range(n):
        mat = rotate_mat(mat)
        print('Rotation', i+1)
        show_mat(mat)
        print('')

# definit le main

def main():
    #create a 3x3 matrix
    mat = create_matrix(5)
    #display the matrix
    show_mat(mat)
    print('')
    #rotate the matrix 4 times
    rotate_n_times(mat, 4)


if __name__ == '__main__':
    main()