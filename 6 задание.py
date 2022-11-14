x, y = float(input()), float(input())
print(True if ((-1 <= y <= 1 and x >= 0) and ((y >= x - 1) or (x ** 2 + y ** 2 <= 1))) else False)
