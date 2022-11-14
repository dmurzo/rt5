x, y = float(input()), float(input())
fl = False
fl = True if (x ** 2 + y ** 2 <= 1) else fl = False
fl = False if (y < x and x > 0) else fl
print(fl)
