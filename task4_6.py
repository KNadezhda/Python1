from itertools import count
from itertools import cycle

for i in count(4, 3):
    if i > 20:
        break
    else:
        print(i)


c = 0
for el in cycle("ABC dfg uio efb"):
    if c > 20:
       break
    else:
         print(el)
    c += 1