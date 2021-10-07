#include <bits/stdc++.h> 
using namespace std;  
void swap(int* a, int* b)  
{  
    int t = *a;  
    *a = *b;  
    *b = t;  
}  
  
int partition (int arr[], int low, int high)  
{  
  int pivot = arr[high]; // pivot  
  int i = (low - 1); // Index of smaller element  
  for (int j = low; j <= high - 1; j++)  
  {  
    if (arr[j] < pivot)  
    { 
      i++; 
      swap(&arr[i], &arr[j]);  
    }  
  }  
  swap(&arr[i + 1], &arr[high]);  
  return (i + 1);  
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
  
int main()  
{  
    int input,size;
    cin >> size;
    int array[size];
    for(int i = 0 ; i < size ; i++ )
    {
        cin >> input;
        array[i] = input;
    }
    
    unsigned t0,t1;

    t0 = clock();
    quickSort(array, 0, size - 1);  
    t1 = clock();

    double time = (double(t1-t0)/CLOCKS_PER_SEC);
    cout << time ;

    return 0;
}  


