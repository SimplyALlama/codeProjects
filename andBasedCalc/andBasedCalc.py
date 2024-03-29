import numpy as np

firstCalc = True
longCalc = False

#operations
def add(num1, num2):
	res = float(num1) + float(num2)
	return res

def sub(num1, num2):
	res = add(float(num1), -float(num2))
	return res

def multi(num1, num2):
	res = 0
	for x in range(int(num2)):
		res = add(float(res), float(num1))
	return res

def divis(num1, num2):
	num1 = float(num1)
	num2 = float(num2)

	sign = -1 if ((num1 < 0) ^  (num2 < 0)) else 1

	num1 = abs(num1)
	num2 = abs(num2)

	quotient = 0
	while (num1 >= num2):
		num1 = sub(num1, num2)
		quotient = add(quotient, 1)

	if sign == -1:
		quotient = sub(quotient, quotient)

	return quotient

#calculator "case switch"
def calc(num1, num2, op):
	if op == "+":
		return add(num1, num2)
	
	elif op == "-":
		return sub(num1, num2)
		
	elif op == "*":
		return multi(num1, num2)

	elif op == "/":
		return divis(num1, num2)
		
#taking input from the user
eqInput = input("Enter your equation: ")

arrCount = 0
eqArr = [""] * len(eqInput)

for x in range(len(eqInput)):
	if eqInput[x].isnumeric() == True or eqInput[x] == ".":
		eqArr[arrCount] = eqArr[arrCount] + eqInput[x]
		
	elif eqInput[x] == " ":
		pass

	else:
		arrCount += 1
		eqArr[arrCount] = eqInput[x]
		arrCount += 1

#removing unused array/list sections
popCount = len(eqInput) - (arrCount + 1)
for i in range(popCount):
	eqArr.pop()	

print(eqArr)

#running of the calculator
if (len(eqInput) > 3):
    longCalc = True
    
for x in range(len(eqArr)):
    if eqArr[x].isnumeric() == False:
        
        if firstCalc == True and longCalc == False:
            calcRes = calc(eqArr[x-1], eqArr[x+1], eqArr[x])
    
        elif firstCalc == True and longCalc == True:
            calcRes = calc(eqArr[x-1], eqArr[x+1], eqArr[x])
            firstCalc = False
        
        elif firstCalc == False and longCalc == True:
            calcRes = calc(calcRes, eqArr[x+1], eqArr[x])
    
print("= " +  str(calcRes))
