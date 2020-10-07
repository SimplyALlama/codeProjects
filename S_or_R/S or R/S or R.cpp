#include "pch.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string shape;
	string cont = "yes";
	int size;
	int sizeX;
	int sizeY;

	cout << cont << endl;

	while (cont == "Yes" || cont == "YES" || cont == "yes" || cont == "y" || cont == "Y")
	{
		cout << "Square or Rectangle?" << endl;
		cin >> shape;

		cout << "The shape is " << shape << endl;

		if (shape == "s" || shape == "S" || shape == "Square" || shape == "square")
		{
			cout << "here" << endl;

			cout << "How large would you like the square to be?" << endl;
			cin >> size;

			for (int i = 0; i < size; i++)
			{
				for (int k = 0; k < size; k++)
				{
					cout << "*";
				}
				cout << endl;
			}
		}

		else
		{
			cout << "How tall would you like the rectangle to be?" << endl;
			cin >> sizeY;

			cout << "How wide would you like the rectangle to be?" << endl;
			cin >> sizeX;

			for (int j = 0; j < sizeY; j++)
			{
				for (int m = 0; m < sizeX; m++)
				{
					cout << "*";
				}
				cout << endl;
			}
		}
	}
	return 0;
}