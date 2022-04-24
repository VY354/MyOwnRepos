
bool WriteWeights(NeuralNetwork& NN, ofstream& weights, string pathName)
{
	weights.open(pathName);
	if (!weights.is_open()) return false;
	weights.clear();

	for (int i = 0; i < NN.get_WeightMatrixesNum(); i++)
	{
		WeightMatrix* curWM = NN.get_WeightMatrix(i);
		for (int j = 0; j < curWM->get_RowNum(); j++)
		{
			for (int k = 0; k < curWM->get_ColNum(); k++)
			{
				weights << curWM->get_Value(j, k);
				weights << '\n';
			}
		}
	}
	weights.close();
}
bool ReadWeights(NeuralNetwork& NN, ifstream& weights, string pathName)
{

	weights.open(pathName);
	if (!weights.is_open()) return false;

	for (int i = 0; i < NN.get_WeightMatrixesNum(); i++)
		for (int j = 0; j < NN.get_WeightMatrix(i)->get_RowNum(); j++)
			for (int k = 0; k < NN.get_WeightMatrix(i)->get_ColNum(); k++)
				weights >> NN.get_WeightMatrix(i)->get_Value(j, k);
	weights.close();
}

void ShowLayers(NeuralNetwork net, int index = -1, int width = 11, int slice = 10, int percision = 4)
{
	cout << endl << "===== LAYERS ================" << endl;

	if (index != -1)
	{
		cout << endl << "<" << index << ">----------------------------------------------------------------------------------------------------";

		Layer* curLayer = net.get_Layer(index);
		for (int i = 0; i < curLayer->get_Size(); i++)
		{
			if (i % slice == 0) cout << endl;
			if (strcmp(typeid(curLayer->get_Neuron(i).get_outValue()).name(), "float") == 0 || strcmp(typeid(curLayer->get_Neuron(i).get_outValue()).name(), "double") == 0)
				cout << right << setw(width) << fixed << setprecision(percision) << curLayer->get_Neuron(i).get_outValue();
			else
				cout << right << setw(width) << curLayer->get_Neuron(i).get_outValue();
			float v = curLayer->get_Neuron(curLayer->get_Size() - 1).get_outValue();
		}
	}
	else
	{
		for (int j = 0; j < net.get_LayersNum(); j++)
		{
			Layer* curLayer = net.get_Layer(j);
			cout << endl << "<" << j << ">----------------------------------------------------------------------------------------------------";
			for (int i = 0; i < curLayer->get_Size(); i++)
			{
				if (i % slice == 0) cout << endl;
				if (strcmp(typeid(curLayer->get_Neuron(i).get_outValue()).name(), "float") == 0 || strcmp(typeid(curLayer->get_Neuron(i).get_outValue()).name(), "double") == 0)
					cout << right << setw(width) << fixed << setprecision(percision) << curLayer->get_Neuron(i).get_outValue();
				else
					cout << right << setw(width) << curLayer->get_Neuron(i).get_outValue();
				float v = curLayer->get_Neuron(curLayer->get_Size() - 1).get_outValue();
			}
		}
	}
}
void ShowWeights(NeuralNetwork net, int index = -1, int width = 11, int slice = 10, int percision = 4)
{
	cout << endl << endl << "===== WEIGHTS ================" << endl;

	if (index != -1)
	{
		WeightMatrix* curWeights = net.get_WeightMatrix(index);
		int RowNum = curWeights->get_RowNum();
		int ColNum = curWeights->get_ColNum();

		cout << endl << "<" << index << ">----------------------------------------------------------------------------------------------------" << endl;

		for (int i = 0; i < RowNum; i++)
		{
			for (int j = 0; j < ColNum; j++)
			{
				if (strcmp(typeid(curWeights->get_Value(0, 0)).name(), "float") == 0 || strcmp(typeid(curWeights->get_Value(0, 0)).name(), "double") == 0)
					cout << right << setw(width) << fixed << setprecision(percision) << curWeights->get_Value(i, j);
				else
					cout << right << setw(width) << curWeights->get_Value(i, j);
			}
			cout << endl;
		}
	}
	else
	{
		for (int k = 0; k < net.get_WeightMatrixesNum(); k++)
		{
			WeightMatrix* curWeights = net.get_WeightMatrix(k);
			int RowNum = curWeights->get_RowNum();
			int ColNum = curWeights->get_ColNum();

			cout << endl << "<" << k << ">----------------------------------------------------------------------------------------------------" << endl;

			for (int i = 0; i < RowNum; i++)
			{
				for (int j = 0; j < ColNum; j++)
				{
					if (strcmp(typeid(curWeights->get_Value(0, 0)).name(), "float") == 0 || strcmp(typeid(curWeights->get_Value(0, 0)).name(), "double") == 0)
						cout << right << setw(width) << fixed << setprecision(percision) << curWeights->get_Value(i, j);
					else
						cout << right << setw(width) << curWeights->get_Value(i, j);
				}
				cout << endl;
			}
		}
	}
}
void get_TotalConnections(NeuralNetwork NN)
{
	int CountBounds = 0;
	for (int i = 1; i < NN.get_LayersNum(); i++)
		CountBounds += NN.get_Layer(i - 1)->get_Size() * NN.get_Layer(i)->get_Size();

	cout << endl << "===== TOTAL CONNECTIONS | " << CountBounds << " ================" << endl;
}

void AdjustLR(float& curLR, int curEpoch, int cycleEpoch)
{
	static int i = 0;
	static float k;
	static int x = 1;
	static float targetLR = 1;
	if (curLR <= 0)
	{
		i = 0;
		x = 1;
		targetLR = 1;
	}

	if (x == 2 * cycleEpoch || i == 0)
	{
		i += 1;
		x = 1;
		if (i % 2 == 0)targetLR /= 2;
		k = tanf(targetLR / cycleEpoch);
	}

	if (x <= cycleEpoch) curLR = k * x;
	else curLR = k * (2 * cycleEpoch - x);

	x++;
}
void TrainNN(NeuralNetwork& NN, int epoch, int subEpoch, int cycleEpoch, float& LR)
{
	LR = -1;
	int index = 0;

	mixTests(Images, Answers);
	for (int i = 0; i < epoch; i++)
	{
		AdjustLR(LR, i, cycleEpoch);
		NN.set_LearningRate(LR);

		if (index == TotalImages - 1)
		{
			mixTests(Images, Answers);
			index = 0;
		}

		for (int j = 0; j < subEpoch; j++)
		{
			NN.Propagation(Images[index]);
			NN.BackPropagation(Answers[index]);
		}

		index++;
	}
}
void TestNN(NeuralNetwork& NN)
{
	float AvgCost = 0;
	createTests(Images, Answers);
	for (int i = 0; i < TotalImages; i++)
	{
		NN.Propagation(Images[i]);
		float curCost = NN.get_Cost(Answers[i]);
		AvgCost += curCost;
		cout << "<" << setw(3) << i << "> ";
		cout << "Cost : " << setw(10) << fixed << setprecision(6) << curCost * 100 << "  %" << endl;
	}
	AvgCost /= TotalImages;
	cout << endl << "Average cost : " << setw(10) << fixed << setprecision(6) << AvgCost * 100 << "  %" << endl;
}
void TestNN(NeuralNetwork& NN, float* image, int noise)
{
	float imageCopy[100];
	for (int i = 0; i < 100; i++) imageCopy[i] = image[i];

	for (int i = 0; i < noise; i++) imageCopy[rand() % 100] = 1;

	NN.Propagation(imageCopy);

	printarr(imageCopy, imageSize, 2, imageRow, 0);
	cout << endl;

	ShowLayers(NN, NN.get_LayersNum() - 1);
	cout << endl;
}


