count_ = 0
for i in range(3):
    x = int(input())
    if x % 2 == 0:
        count_ += 1
fl = False
if count_ >= 2:
    fl = True
print(fl)
