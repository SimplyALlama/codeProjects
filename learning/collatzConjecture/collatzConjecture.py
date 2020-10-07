count = 0

print('What number do you want to start with?')
n = int(input())

while (n != 1):
    print("N:", n)
    if (n % 2 == 0):
        n = n/2
    else:
        n = 3*n + 1

    count = count + 1

print("done")
print("count", count)
