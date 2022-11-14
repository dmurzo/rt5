import math as m

x, y = float(input()), float(input())
print(True if ((0 <= y <= 0.5) and (x >= 0) and (y <= m.sin(x))) else False)
