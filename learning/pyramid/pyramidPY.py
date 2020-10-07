print('how many layers woudl you like?')
layers = int(input()) + 1
count = int(0)

for i in range(layers):
    for p in range(i):
        print('^', end='')
    print('')

print('')
