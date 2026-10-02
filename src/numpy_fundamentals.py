import numpy as np


def main():
    # 1D array
    arr_1d = np.array([10, 20, 30, 40, 50])

    # 2D array
    arr_2d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    # 3D array
    arr_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])

    print("1D Array:")
    print(arr_1d)
    print("Shape:", arr_1d.shape)

    print("\n2D Array:")
    print(arr_2d)
    print("Shape:", arr_2d.shape)

    print("\n3D Array:")
    print(arr_3d)
    print("Shape:", arr_3d.shape)
        # Broadcasting
    numbers = np.array([10, 20, 30, 40])
    broadcasted_result = numbers + 5

    print("\nBroadcasting:")
    print("Original:", numbers)
    print("After adding 5:", broadcasted_result)

    # Vectorised operations
    print("\nVectorised Operations:")
    print("Multiply by 2:", numbers * 2)
    print("Square:", numbers ** 2)
    # Matrix multiplication
matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

matrix_result = matrix_a @ matrix_b

print("\nMatrix Multiplication:")
print(matrix_result)
# Statistics
scores = np.array([70, 75, 80, 85, 90])

mean_score = np.mean(scores)
std_score = np.std(scores)

print("\nStatistics:")
print("Mean:", mean_score)
print("Standard Deviation:", std_score)
# Correlation
study_hours = np.array([2, 3, 4, 5, 6])
scores = np.array([50, 60, 70, 80, 90])

correlation = np.corrcoef(study_hours, scores)[0, 1]

print("\nCorrelation:")
print("Study Hours vs Scores:", correlation)


if __name__ == "__main__":
    main()