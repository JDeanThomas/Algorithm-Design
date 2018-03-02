//
//  main.cpp
//  Algorithm Design C++
//
//  Created by Jason Thomas on 7/23/16.
//  Copyright © 2016 Jason Thomas. All rights reserved.
//



//C++ Program to Implement Merge Sort

#include <iostream>
using namespace std;

void merge(int *,int, int , int );
void mergesort(int *a, int left, int right)
{
    int mid;
    if (left < right)
    {
        mid=(left+right)/2;
        mergesort(a,left,mid);
        mergesort(a,mid+1,right);
        merge(a,left,right,mid);
    }
    return;
}
void merge(int *a, int left, int right, int mid)
{
    int i, j, k, c[50];
    i = left;
    k = left;
    j = mid + 1;
    while (i <= mid && j <= right)
    {
        if (a[i] < a[j])
        {
            c[k] = a[i];
            k++;
            i++;
        }
        else
        {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[k] = a[i];
        k++;
        i++;
    }
    while (j <= right)
    {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = left; i < k; i++)
    {
        a[i] = c[i];
    }
}
int main()
{
    int a[20], i, b[20];
    cout<<"enter  the elements\n";
    for (i = 0; i < 5; i++)
    {
        cin>>a[i];
    }
    mergesort(a, 0, 4);
    cout<<"sorted array\n";
    for (i = 0; i < 5; i++)
    {
        cout<<a[i];
    }
    cout<<"enter  the elements\n";
    for (i = 0; i < 5; i++)
    {
        cin>>b[i];
    }
    mergesort(b, 0, 4);
    cout<<"sorted array\n";
    for (i = 0; i < 5; i++)
    {
        cout<<b[i];
    }
    cin.get();
}