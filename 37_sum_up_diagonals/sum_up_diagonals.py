m1 = [
     [1,   2],
     [30, 40],
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def sum_up_diagonals(matrix):
    length = len(matrix)
    sum = 0
    for i in range(length):
        sum += matrix[i][i]
        sum += matrix[-i][length -1 -i]
    print(sum)
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> sum_up_diagonals(m1)
        73


        >>> sum_up_diagonals(m2)
        30
    """
sum_up_diagonals(m1)
sum_up_diagonals(m2)

# tested, works