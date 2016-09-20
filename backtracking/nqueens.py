def solveNQueens(A):
    def safe(col, queens):
        return col not in queens and all(abs(col - c) != len(queens)-i for i,c in enumerate(queens))
    solutions = [[]]
    for _ in range(A):
        solutions = [sol+[i] for sol in solutions for i in range(A) if safe(i, sol)]
    return [['.'*c + 'Q' + '.'*(A-1-c) for c in sol] for sol in solutions]
a = solveNQueens(15)
for i,s in enumerate(a):
    print('Solution #{}'.format(i+1))
    for r in s:
        print(r)