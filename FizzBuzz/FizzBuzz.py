lowerLimit = 1
upperLimit = 100

for i in range(lowerLimit, upperLimit + 1):
	if (i % 3 == 0 and i % 5 == 0):
		print("FizzBuzz")
	
	elif (i % 3 == 0):
		print("Fizz")

	elif (i % 5 == 0):
		print("Buzz")

	else:
		print(i)