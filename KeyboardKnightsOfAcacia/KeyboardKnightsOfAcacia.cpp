#include <cctype>
#include <iostream>
#include <string>

using namespace std;

// char board[4][5] = {{"ABCDE"}, 
// 					{"FGHIJ"}, 
// 					{"KLMNO"}, 
// 					{" 123 "}};

string possibleMoves[18] = {"LH", "KMI",  "FLNJ", "OMG", "NH", 
					 "CM", "DN2", "AKEO13", "2LB", "CM", 
					 "B2H", "AC3I", "CBJF", "EC1G", "D2H", 
					 			  "NFH", "KOGI", "LHJ"};

string move(char startingPoint)
{
	int index = 0;
	// changing char values into integers
	if (isalpha(startingPoint))
	{
		index = int(startingPoint) - 65;
	}

	else{
		index = int(startingPoint) - 34;
	}

	cout << "char: " << startingPoint << " index: " << index << endl;

	return possibleMoves[index];
}

void path(char startingPoint, int length, int vowels)
{
	if (length >= 10)
	{
		cout << "reached max length" << endl;
		return;
	}

	if (startingPoint == 'A' || startingPoint == 'E' ||startingPoint == 'I' ||startingPoint == 'O')
	{
		vowels++;

		if (vowels == 2)
		{
			cout << "2 vowels" << endl;
			return;
		}
	}

	int currLength = length;
	currLength++;

	string options = move(startingPoint);
	cout << "options: " << options << endl;

	path(options[0], currLength, vowels);
	
}

int main(int argc, char const *argv[])
{
	int count = 0;

	char temp = 'C';
	string next;

	path(temp, 0, 0);

	return 0;
}

