#include <iostream>

using namespace std;

int main()
{
	int layers;

	cout << "How many layers do you want on the pyramid?" << endl;

	cin >> layers;

	for (int i = 0; i < layers; i++)
	{
		for (int k = 0; k <= i; k++)
		{
			cout << "*";
		}
		cout << endl;
	}
	return 0;
};