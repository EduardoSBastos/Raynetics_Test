import numpy as np

M_SIZE = 1000

def main():
    matrix = np.zeros((M_SIZE,M_SIZE))
    for i in range(M_SIZE):
        for j in range(M_SIZE):
            matrix[i,j] = (i*j) % 17
    row_sums = np.zeros(M_SIZE)
    for i in range(M_SIZE):
        row_sums[i] = np.sum(matrix[i, :])
    even_sum_count:int = 0
    for row_sum in row_sums:
        if row_sum % 2 == 0:
            even_sum_count += 1

    print(f"Amount of rows that have even sum: {even_sum_count}.")

        
if __name__ == "__main__":
    main()