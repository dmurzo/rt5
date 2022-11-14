x, y = float(input()), float(input())
fl = False
if x ** 2 + y ** 2 <= 1:
    fl = True
    if y < x and x > 0:
        fl = False
print(fl)
