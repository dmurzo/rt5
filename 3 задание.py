x, y = float(input()), float(input())
fl = False
if (-1 <= y <= 1 and x >= 0):
    if (y >= x - 1) or (x ** 2 + y ** 2 <= 1):
        fl = True
print(fl)
