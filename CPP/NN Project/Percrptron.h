class Neuron
{
private:
	float inValue;
	float outValue;
	float error;

public:
	Neuron()
	{
		inValue = 0;
		outValue = 0;
		error = 0;
	}

	Neuron& operator=(const Neuron& other)
	{
		inValue = other.inValue;
		outValue = other.outValue;
		error = other.error;
		return *this;
	}
	void* operator new(size_t size)
	{
		return ::operator new(size);
	}

	void ResetNeuron()
	{
		inValue = 0;
		outValue = 0;
		error = 0;
	}

	//================== getting ==================
	float& get_inValue()
	{
		return inValue;
	}
	float& get_outValue()
	{
		return outValue;
	}
	float& get_error()
	{
		return error;
	}
};

class Layer
{
private:
	int Size;
	Neuron* NeuronS;

public:
	Layer()
	{
		Size = 0;
		NeuronS = nullptr;
	}
	Layer(int size)
	{
		Size = size;
		NeuronS = new Neuron[size];
		for (int i = 0; i < Size; NeuronS[i] = *(new Neuron()), i++);
	}

	Neuron& operator[](int index)
	{
		return NeuronS[index];
	}

	//================== Main methods ==================
	void ResetNeurons()
	{
		for (int i = 0; i < Size; i++) NeuronS[i].ResetNeuron();
	}

	//================== Settings ==================
	void set_Size(int _Size)
	{
		Size = _Size;
		NeuronS = new Neuron[Size];
		for (int i = 0; i < Size; NeuronS[i] = *(new Neuron()), i++);
	}

	//================== getting ==================
	int& get_Size()
	{
		return Size;
	}
	Neuron& get_Neuron(int index)
	{
		return NeuronS[index];
	}

	~Layer() {}
};

class WeightMatrix
{
private:
	int Row;
	int Col;
	float** Weights;

public:

	WeightMatrix()
	{
		Row = 0;
		Col = 0;
		Weights = nullptr;
	}
	WeightMatrix(int row, int col)
	{
		Row = row;
		Col = col;
		Weights = new float* [row];
		for (int i = 0; i < Row; Weights[i] = new float[Col], i++);

		for (int i = 0; i < Row; i++)
			for (int j = 0; j < Col; j++)
				Weights[i][j] = 0;
	}

	WeightMatrix& operator=(const WeightMatrix other)
	{
		Row = other.Row;
		Col = other.Col;
		for (int i = 0; i < Row; i++)
			for (int j = 0; j < Col; Weights[i][j] = other.Weights[i][j], j++);
	}
	void* operator new(size_t size)
	{
		return ::operator new(size);
	}

	//================== Main methods ==================
	void FillRandom(int from, int to, int part = 1, int step = 1)
	{
		srand(time(NULL));
		for (int i = 0; i < Row; i += step)
			for (int j = 0; j < Col; j += step)
				Weights[i][j] = ((from + rand() % (to - from)) / float(part) + (from + rand() % (to - from)) / float(part)) / 2;
	}

	//================== Settings ==================
	void set_Size(int row, int col)
	{
		Row = row;
		Col = col;
		Weights = new float* [row];
		for (int i = 0; i < Row; Weights[i] = new float[Col], i++);

		for (int i = 0; i < Row; i++)
			for (int j = 0; j < Col; j++)
				Weights[i][j] = 0;
	}

	//================== getting ==================
	float& get_Value(int row, int col)
	{
		return Weights[row][col];
	}
	int get_RowNum()
	{
		return Row;
	}
	int get_ColNum()
	{
		return Col;
	}

	~WeightMatrix() {}
};

class NeuralNetwork
{
private:
	int LayersNum;
	int WeightMatrixesNum;

	Layer* LayerS;
	WeightMatrix* WeightMatrixeS;

	float BiasWeight;
	float LearningRate;

	//================== Learning ==================
	void CalculateIn(Layer& curLayer, Layer prevLayer, WeightMatrix weightMatrix, int ind)
	{
		for (int i = 0; i < curLayer.get_Size(); i++)
		{
			for (int j = 0; j < prevLayer.get_Size(); j++)
				curLayer.get_Neuron(i).get_inValue() += prevLayer.get_Neuron(j).get_outValue() * weightMatrix.get_Value(j, i);
			if (ind < LayersNum - 1) curLayer.get_Neuron(i).get_inValue() += BiasWeight;
			ActivateNeuron_Sigmoid(curLayer[i]);
		}
	}
	void ActivateNeuron_Sigmoid(Neuron& neuron)
	{
		neuron.get_outValue() = (float)1 / (1 + exp(-neuron.get_inValue()));
	}
	void CalculateOutErrors(Layer& curLayer, float* IdealOut)
	{
		for (int i = 0; i < curLayer.get_Size(); i++)
		{
			float NeuronOutValue0 = curLayer.get_Neuron(0).get_outValue();
			curLayer.get_Neuron(i).get_error() = powf(NeuronOutValue0 - IdealOut[i], 2) * 2 * (NeuronOutValue0 - IdealOut[i]);
		}
	}
	void CalculateLayerErrors(Layer& curLayer, Layer* nextLayer, WeightMatrix* weightMatrix)
	{
		for (int i = 1; i < curLayer.get_Size(); i++)
		{
			curLayer.get_Neuron(i).get_error() = 0;
			float curOut = curLayer.get_Neuron(i).get_outValue();

			for (int j = 0; j < nextLayer->get_Size(); j++)
			{
				float nextVal = nextLayer->get_Neuron(j).get_outValue();
				float grad_next = nextVal * (1 - nextVal);

				float nextErr = nextLayer->get_Neuron(j).get_error();
				float curWeight = weightMatrix->get_Value(i, j);

				curLayer.get_Neuron(i).get_error() += nextErr * grad_next * curWeight;
			}
		}
	}
	void reCalculateWeights(Layer& prevLayer, Layer nextLayer, WeightMatrix& curWeights)
	{
		for (int i = 0; i < prevLayer.get_Size(); i++)
		{
			for (int j = 0; j < nextLayer.get_Size(); j++)
			{
				float nextOut = nextLayer.get_Neuron(j).get_outValue();
				float grad_j = nextOut * (1 - nextOut);

				float nextErr = nextLayer.get_Neuron(j).get_error();
				float curOut = prevLayer.get_Neuron(i).get_outValue();

				float grad_ij = nextErr * grad_j * curOut;
				curWeights.get_Value(i, j) -= LearningRate * grad_ij;
			}
		}
	}

public:

	NeuralNetwork()
	{
		LayersNum = 0;
		WeightMatrixesNum = 0;

		LayerS = nullptr;
		WeightMatrixeS = nullptr;

		BiasWeight = 0;
		LearningRate = 0;
	}

	//================== Main methods ==================
	void InitializeNet(int* SizesArray = nullptr, int size = 0)
	{
		LayersNum = size;
		WeightMatrixesNum = size - 1;

		LayerS = new Layer[LayersNum];
		WeightMatrixeS = new WeightMatrix[WeightMatrixesNum];

		if (SizesArray == nullptr)
		{
			int j = LayersNum;
			for (int i = 0; i < LayersNum; i++)
			{
				LayerS[i].set_Size(j);
				if (i > 0)
				{
					WeightMatrixeS[i - 1].set_Size(j + 1, j);
					WeightMatrixeS[i - 1].FillRandom(-100, 100, 100);
				}
				j--;
			}
		}
		else
		{
			for (int i = 0; i < LayersNum; i++)
			{
				LayerS[i].set_Size(SizesArray[i]);
				if (i > 0)
				{
					WeightMatrixeS[i - 1].set_Size(SizesArray[i - 1], SizesArray[i]);
					WeightMatrixeS[i - 1].FillRandom(-100, 100, 100);
				}
			}
		}
	}
	void Propagation(float* Input)
	{
		set_InputFrom(Input);
		for (int i = 1; i < LayersNum; i++)
		{
			LayerS[i].ResetNeurons();
			CalculateIn(LayerS[i], LayerS[i - 1], WeightMatrixeS[i - 1], i);
		}
	}
	void BackPropagation(float* IdealOut)
	{
		CalculateOutErrors(LayerS[LayersNum - 1], IdealOut);
		for (int i = LayersNum - 2; i >= 0; i--)
			CalculateLayerErrors(LayerS[i], &LayerS[i + 1], &WeightMatrixeS[i]);
		for (int j = 0; j < LayersNum - 1; j++)
			reCalculateWeights(LayerS[j], LayerS[j + 1], WeightMatrixeS[j]);
	}

	//================== Settings ==================
	void set_BiasWeight(float _BiasWeight)
	{
		BiasWeight = _BiasWeight;
	}
	void set_LearningRate(float _LearningRate)
	{
		LearningRate = _LearningRate;
	}
	void set_InputFrom(float* Values)
	{
		for (int i = 0; i < LayerS[0].get_Size(); i++)
			LayerS[0].get_Neuron(i).get_outValue() = Values[i];
	}

	//================== getting ==================
	int get_LayersNum()
	{
		return LayersNum;
	}
	int get_WeightMatrixesNum()
	{
		return WeightMatrixesNum;
	}
	Layer* get_Layer(int index)
	{
		return &LayerS[index];
	}
	WeightMatrix* get_WeightMatrix(int index)
	{
		return &WeightMatrixeS[index];
	}
	float get_Cost(float* IdealOut)
	{
		float Cost = 0;
		for (int i = 0; i < LayerS[LayersNum - 1].get_Size(); i++)
			Cost += powf(IdealOut[i] - LayerS[LayersNum - 1].get_Neuron(i).get_outValue(), 2);
		Cost /= LayerS[LayersNum - 1].get_Size();
		return Cost;
	}

	~NeuralNetwork() {}
};
