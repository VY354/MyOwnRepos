#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <stdbool.h>
#include <string>
#include<fstream>
#include <Windows.h>


using namespace std;


#include "OtherFunctions.h"

#include "Percrptron.h"
#include "TrainData.h"
#include "FunctionsForNN.h"


int main()
{
	srand(time(NULL));
	setlocale(LC_ALL, "UTF-8");

	createTests(Images, Answers);

	float image[100] =
	{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, };

	ofstream of_Weights;
	ifstream if_Weights;
	string pathName = "weight.txt";

	//================== NN Parametrs ==================

	int const InSize = imageSize;
	int const LayersNum = 4;
	int const OutSize = 2;

	int SizesArray[] = { InSize,15,15,OutSize };

	NeuralNetwork NN;
	NN.InitializeNet(SizesArray, LayersNum);

	float LR = 1;
	NN.set_LearningRate(LR);

	int epoch = 20 * 1000;
	int subEpoch = 1;
	int cycleEpoch = epoch / 10;

	int noise = 10;

	//==================================================

	while (true)
	{
		char ch;

		cout << endl;
		cout << "==========================================" << endl;
		cout << "1 - train" << endl;
		cout << "2 - test general" << endl;
		cout << "3 - test special" << endl;
		cout << "4 - reset NN" << endl;
		cout << "6 - save weights" << endl;
		cout << "8 - load weights" << endl;
		cout << "s - settings" << endl;
		cout << "e - exit" << endl;
		cout << "==========================================" << endl;
		cout << "-----> "; cin.clear(); cin >> ch;
		if (ch == 'e') break;
		system("CLS");

		switch (ch)
		{
			case('1'):
			{
				cout << "Please, wait. Neural network is training ..." << endl;
				TrainNN(NN, epoch, subEpoch, cycleEpoch, LR);
				system("CLS");
				break;
			}
			case('2'):
			{
				system("CLS");
				TestNN(NN);
				break;
			}
			case('3'):
			{
				system("CLS");
				TestNN(NN, image, noise);
				break;
			}
			case('4'):
			{
				for (int i = 0; i < NN.get_WeightMatrixesNum(); i++)
					NN.get_WeightMatrix(i)->FillRandom(-100, 100, 100);
				cout << "Weights have been reseted" << endl;
				break;
			}
			case('6'):
			{
				if (!WriteWeights(NN, of_Weights, pathName))
				{
					system("CLS");
					cout << ">>> ERROR : cannot open file <<<" << endl;
					break;
				}
				cout << "Weights have been SAVED" << endl;
				break;
			}
			case('8'):
			{
				if (!ReadWeights(NN, if_Weights, pathName))
				{
					system("CLS");
					cout << ">>> ERROR : cannot open file <<<" << endl;
					break;
				}
				cout << "Weights have been LOADED" << endl;
				break;
			}
			case('s'):
			{
				char ch;

				while (true)
				{

					system("CLS");
					cout << endl;
					cout << "==========================================" << endl;
					cout << "1 - change number of epoch" << endl;
					cout << "2 - change number of sub epoch (default 1)" << endl;
					cout << "3 - change noise frequency" << endl;
					cout << "e - back to main" << endl;
					cout << "==========================================" << endl;
					cout << "-----> "; cin.clear(); cin >> ch;
					if (ch == 'e')
					{
						system("CLS");
						break;
					}
					system("CLS");

					switch (ch)
					{
					case('1'):
					{
						cout << "Enter number of epoch (default 20 000) : "; cin >> epoch;
						system("CLS");
						break;
					}
					case('2'):
					{
						cout << "Enter number of sub epoch (should be 1) : "; cin >> subEpoch;
						system("CLS");
						break;
					}
					case('3'):
					{
						cout << "Enter value of noise (default 10)  : "; cin >> noise;
						system("CLS");
						break;
					}
					default:
					{
						system("CLS");
						cout << ">>> ERROR <<<" << endl;
					}
					}
				}

				break;
			}
			default:
			{
				system("CLS");
				cout << ">>> ERROR <<<" << endl;
			}
		}
	}

	system("CLS");
	return 0;
}
