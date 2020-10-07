import numpy as np

x = 1 #start of prime search
y = 25 #end of prime search
prime = False

while x <= y: #searching thought the numbers
    if (x > 1):
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print(x)

    x += 1 #goto next number
    
print('______')