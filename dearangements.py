from itertools import permutations
import os

def generate_combinations(elements):
    perm_list = list(permutations(elements))
    perm_list = [p for p in perm_list if not any(i == j for i, j in zip(p, elements))]
    with open("combinations.txt", "w") as f:
        for i, combination in enumerate(perm_list, start=1):
            f.write(f"{i}: {combination}\n")

generate_combinations([1, 2, 3, 4, 5, 6])


cwd = os.getcwd()
print(f"Current working directory: {cwd}")
file_path = os.path.join(cwd, "combinations.txt")
print(f"Path to combinations.txt: {file_path}")