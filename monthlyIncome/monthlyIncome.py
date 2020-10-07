bills = []

print('How much do you make per month?')
income = int(input())
print()

print('How many bills do you have per month?')
numBill = int(input())
print()

print('On average how much are each of your bills per month?')
for i in range(0, numBill):
    x = int(input())
    bills.insert(i, x)
print()

for p in range(0, numBill):
    income = income - bills[p]

print('You have', income, 'left after paying all monthly bills')
