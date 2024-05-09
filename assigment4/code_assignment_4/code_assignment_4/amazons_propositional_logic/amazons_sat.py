from clause import *

"""
For the n-amazon problem, the only code you have to do is in this file.

You should replace

# your code here

by a code generating a list of clauses modeling the n-amazons problem
for the input file.

You should build clauses using the Clause class defined in clause.py

Here is an example presenting how to create a clause:
Let's assume that the length/width of the chessboard is 4.
To create a clause X_0_1 OR ~X_1_2 OR X_3_3
you can do:

clause = Clause(4)
clause.add_positive(0, 1)
clause.add_negative(1, 2)
clause.add_positive(3, 3)

The clause must be initialized with the length/width of the chessboard.
The reason is that we use a 2D index for our variables but the format
imposed by MiniSAT requires a 1D index.
The Clause class automatically handle this change of index, but needs to know the
number of column and row in the chessboard.

X_0_0 is the literal representing the top left corner of the chessboard
"""




def get_expression(size: int, placed_amazons: list[(int, int)]) -> list[Clause]:
    """
    Defines the clauses for the N-amazons problem
    :param size: length/width of the chessboard
    :param placed_amazons: a list of the already placed amazons
    :return: a list of clauses
    """

    expression = []

    # Contrainte : Chaque ligne doit avoir exactement une amazone
    for row in range(size):
        clause = Clause(size)
        for col in range(size):
            clause.add_positive(row, col)
        expression.append(clause)

    # Contrainte : Chaque colonne doit avoir exactement une amazone
    for col in range(size):
        clause = Clause(size)
        for row in range(size):
            clause.add_positive(row, col)
        expression.append(clause)

    # Contrainte : Aucune nouvelle amazone sur une case déjà occupée
    for amazon in placed_amazons:
        row, col = amazon
        clause = Clause(size)
        clause.add_negative(row, col)
        expression.append(clause)

    # Contrainte : Aucune menace entre les amazones déjà placées
    for i in range(len(placed_amazons)):
        for j in range(i + 1, len(placed_amazons)):
            row1, col1 = placed_amazons[i]
            row2, col2 = placed_amazons[j]

            # Aucune menace sur la même ligne, colonne ou diagonale
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                clause = Clause(size)
                clause.add_negative(row1, col1)
                clause.add_negative(row2, col2)
                expression.append(clause)
    # Contrainte : Déplacements autorisés pour les amazones
    for amazon in placed_amazons:
        row, col = amazon

        # Déplacement 3x2
        for dr in [-3, 3]:
            for dc in [-2, 2]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < size and 0 <= new_col < size:
                    clause = Clause(size)
                    clause.add_negative(row, col)
                    clause.add_positive(new_row, new_col)
                    expression.append(clause)

        # Déplacement 4x1
        for dr in [-4, 4]:
            for dc in [-1, 1]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < size and 0 <= new_col < size:
                    clause = Clause(size)
                    clause.add_negative(row, col)
                    clause.add_positive(new_row, new_col)
                    expression.append(clause)


    return expression

