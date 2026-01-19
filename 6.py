"""6 - Solve the 8-Queens problem using backtracking and display the final board arrangement."""
#Done
def q(c):
    if c == 8:
        for r in b:
            print(*[1 if i == r else 0 for i in range(8)])
        print(b)
        return True

    for r in range(8):
        if all(r != b[i] and abs(r - b[i]) != c - i for i in range(c)):
            b[c] = r
            if q(c + 1):
                return True


b = [0] * 8
q(0)
