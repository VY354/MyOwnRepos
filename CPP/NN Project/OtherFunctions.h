template <class T>
void fillrandom(T* Arr, int size, int from, int to, int step = 1)
{
	int i;
	for (i = 0; i < size; Arr[i] = from + rand() % (to - from), i += step);
}

template <class T>
void fillrandom(T** Arr, int ROW, int COL, int from, int to, int stepX = 1, int stepY = 1) {
	int i, j;
	for (i = 0; i < ROW; i += stepX)
		for (j = 0; j < COL; j += stepY)
			Arr[i][j] = from + rand() % (to - from);
}

template <class T>
void printarr(T* Arr, int size, int width = 10, int slice = 10, int percision = 3) {
	int i;
	for (i = 0; i < size; i++) {
		if (i % slice == 0) cout << endl;
		if (strcmp(typeid(Arr[0]).name(), "float") == 0 || strcmp(typeid(Arr[0]).name(), "double") == 0)
			cout << right << setw(width) << fixed << setprecision(percision) << Arr[i];
		else
			cout << right << setw(width) << Arr[i];
	}
}

template <class T>
void printarr(T** Arr, int ROW, int COl, int width = 10, int percision = 3) {
	int i, j;
	for (i = 0; i < ROW; i++) {
		for (j = 0; j < COl; j++)
		{
			if (strcmp(typeid(Arr[0][0]).name(), "float") == 0 || strcmp(typeid(Arr[0][0]).name(), "double") == 0)
				cout << right << setw(width) << fixed << setprecision(percision) << Arr[i][j];
			else
				cout << right << setw(width) << Arr[i][j];
		}
		cout << endl;
	}
}