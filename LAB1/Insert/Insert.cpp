#include <iostream>
#include <time.h>
using namespace std;

void insertion(int arr[],   int tam)
{
    int aux, pos;
    for (int i=0;i<tam;i++)
    {
        pos=i;
        aux=arr[i];
        while((pos>0)&&(arr[pos-1]>aux))
        {
            arr[pos]=arr[pos-1];
            pos--;
        }
        arr[pos]=aux;
    }
    
}

int main(){

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
    insertion(array, size);
    t1 = clock();
    double time = (double(t1-t0)/CLOCKS_PER_SEC);
    cout << time ;
    return 0;
    
}
