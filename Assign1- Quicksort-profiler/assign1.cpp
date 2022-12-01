#include <bits/stdc++.h>
using namespace std;


void swap(int &a, int &b)
{
	int temp = a;
	a = b;
	b = temp;
}


int partition (int arr[], int s, int e)
{
    
	int pivot = arr[s];

    int cnt = 0;
    for(int i = s+1; i<=e; i++) {
        if(arr[i] <=pivot) {
            cnt++;
        }
    }
    int pivotIndex = s + cnt;
    swap(arr[pivotIndex], arr[s]);
    int i = s, j = e;

    while(i < pivotIndex && j > pivotIndex) {
        while(arr[i] <= pivot) 
        {
            i++;
        }
        while(arr[j] > pivot) {
            j--;
        }
        if(i < pivotIndex && j > pivotIndex) {
            swap(arr[i++], arr[j--]);
        }
    }
    return pivotIndex;

}


void quickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		
		int pi = partition(arr, low, high);

		
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}


void print(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}


int main()
{
    int n;
    cout<<"Enter the size of array :"<<endl;
    cin>>n;
    int arr[n];
	for(int i=0;i<n;i++)
    {
        arr[i] = n-i;
    }
	quickSort(arr, 0, n - 1);
	cout << "Sorted array: "<<endl;
	print(arr, n);
	return 0;
}