def max_experience(levels, experience_matrix):
    for i in range(levels - 2, -1, -1):
        for j in range(i + 1):
            experience_matrix[i][j] += max(experience_matrix[i + 1][j], experience_matrix[i + 1][j + 1])

    return experience_matrix[0][0]


if __name__ == "__main__":
    with open("career.in", "r") as file:
        levels = int(file.readline())
        experience_matrix = [list(map(int, file.readline().split())) for _ in range(levels)]

    result = max_experience(levels, experience_matrix)

    with open("career.out", "w") as file:
        file.write(str(result))
