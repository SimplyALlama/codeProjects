#include <iostream>

using namespace std;

int lowerLimit = 1;
int upperLimit = 100;

int main()
{
	for (int i = lowerLimit; i <= upperLimit; i++)
	{
		if (i % 3 == 5 && i % 5 == 0)
		{
			cout << "FizzBuzz" << endl;
		}

		else if (i % 3 == 0)
		{
			cout << "Fizz" << endl;
		}

		else if (i % 5 == 0)
		{
			cout << "Buzz" << endl;	
		}

		else
		{
			cout << i << endl;
		}
	}

	return 0;
}