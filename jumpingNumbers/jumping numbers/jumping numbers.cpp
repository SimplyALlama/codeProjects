#include "pch.h"
#include <iostream>

using namespace std;

int main()
{
	int base = 2;
	int i;
	
	for (i = 1; i <= 25; i++)
	{
		cout  << "Count: " << i << endl;

		base *= i;
		cout << "Number: " << base << endl;
	}
};