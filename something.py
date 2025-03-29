def find_cube_pairs(target):
    solutions = []
    max_num = round(target ** (1 / 3))  # Fixed syntax `targ` to `target` and corrected exponentiation operator

    for a in range(1, max_num + 1):  # Fixed `ranges` to `range`
        for b in range(a, max_num + 1):  # Fixed `ranges` to `range`
            if a**3 + b**3 == target:  # Fixed `a***3` to `a**3` and `targ` to `target`
                solutions.append((a, b))  # Fixed `sol.append` to `solutions.append`
    return solutions  # Fixed `sol` to `solutions`

pairs = find_cube_pairs(1729)  # Fixed trailing comma in assignment and corrected value from 1728 to 1729
print("Valid cube pairs for 1729:")  # Fixed `printf` to `print`

for a, b in pairs:  # Fixed `pair` to `pairs`
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Fixed `a**2` and `b**2` to `a**3` and `b**3`
