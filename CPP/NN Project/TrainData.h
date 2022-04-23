
int  imageRow = 10;
int  imageSize = imageRow * imageRow;
int  TotalImages = 4 * imageRow;

float** Images;
float** Answers;

void createTests(float**& curImages, float**& curAnswers)
{
	float from = 0;
	float to = 1;
	float isDot = 1;

	float out1 = 0.9;
	float out0 = 0.1;

	curImages = new float* [TotalImages];
	for (int i = 0; i < TotalImages; i++)
		curImages[i] = new float[imageSize];

	curAnswers = new float* [TotalImages];
	for (int i = 0; i < TotalImages; i++)
		curAnswers[i] = new float[2];

	int d2ar = 0;
	int row = 0;
	int col = 0;

	for (int i = 0; i < 20; i++)
	{
		fillrandom(curImages[d2ar], imageSize, from, to);
		fillrandom(curImages[d2ar], imageSize, 1, 2, i + 1);
		curAnswers[d2ar][0] = out0;
		curAnswers[d2ar][1] = out0;
		d2ar++;
	}

	while (row < imageRow)
	{
		fillrandom(curImages[d2ar], imageSize, from, to);
		for (col = 0; col < imageRow; col++)
			curImages[d2ar][row * imageRow + col] = isDot;
		curAnswers[d2ar][0] = out1;
		curAnswers[d2ar][1] = out0;
		d2ar++;
		row++;
	}
	row = 0;
	col = 0;

	while (col < imageRow)
	{
		fillrandom(curImages[d2ar], imageSize, from, to);
		for (row = 0; row < imageRow; row++)
			curImages[d2ar][row * imageRow + col] = isDot;
		curAnswers[d2ar][0] = out0;
		curAnswers[d2ar][1] = out1;
		d2ar++;
		col++;
	}
	row = 0;
	col = 0;
}

void mixTests(float**& Images, float**& Answers)
{
	srand(time(NULL));
	for (int i = 0; i < 300; i++)
	{
		int const rand1 = (rand() % TotalImages + rand() % TotalImages) / 2;
		int const rand2 = (rand() % TotalImages + rand() % TotalImages) / 2;
		swap(Images[rand1], Images[rand2]);
		swap(Answers[rand1], Answers[rand2]);
	}
}
void ShowImagesAndAnswers(float**& curImages, float**& curAnswers)
{
	for (int i = 0; i < TotalImages; i++)
	{
		cout << "<" << setw(3) << i << ">" << "======================================================" << endl;
		printarr(curImages[i], imageSize, 2, 10, 0);
		cout << endl;
		cout << endl;
		for (int j = 0; j < 2; j++)
			cout << curAnswers[i][j] << " ";
		cout << endl;
	}
}
