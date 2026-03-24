# Make a simple board game (like Snake or Connect Four) and use a strategy or learning technique to play it.

R, C = 6, 7
b = [["."] * C for _ in range(R)]
def show():
    print("\n".join("".join(r) for r in b))
    print("0 1 2 3 4 5 6\n")
def win(p):
    for r in range(R):
        for c in range(C):
        # horizontal →
            if c + 3 < C and all(b[r][c+i] == p for i in range(4)):
                return True
        # vertical ↓
            if r + 3 < R and all(b[r+i][c] == p for i in range(4)):
                return True
        # diagonal ↘
            if r + 3 < R and c + 3 < C and all(b[r+i][c+i] == p for i in range(4)):
                return True
        # diagonal ↗
            if r - 3 >= 0 and c + 3 < C and all(b[r-i][c+i] == p for i in range(4)):
                return True
    return False
p = 0
while True:
    show()
    # get valid column input
    while True:
        col = input(f"player {'XO'[p]}: ")
        if not col.isdigit():
            print("Enter a number between 0 and 6.")
            continue
        col = int(col)
        if not (0 <= col < C):
            print("Column must be between 0 and 6.")
            continue
        if b[0][col] != ".":
            print("That column is full.")
            continue
            break
        # drop piece
        for r in range(R - 1, -1, -1):
            if b[r][col] == ".":
                b[r][col] = "XO"[p]
                break
            if win("XO"[p]):
                show()
                print(f"Player {'XO'[p]} wins!")
                break
        p ^= 1