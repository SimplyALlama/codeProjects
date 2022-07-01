var lowerLimit = 1
var upperLimit = 100

for (var i = lowerLimit; i <= upperLimit; i++)
{
	if (i % 3 == 5 && i % 5 == 0)
	{
		console.log("FizzBuzz")	
	}

	else if (i % 3 == 0)
	{
		console.log("Fizz")	
	}

	else if (i % 5 == 0)
	{
		console.log("Buzz")	
	}

	else
	{
		console.log(i)
	}
}