Quick Sort 

Quick Sort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

Given an array arr[], its starting position low and its ending position high. Quick Sort is achieved using the following algorithm. 

quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, 
           arr[pi] is now at right place */
        pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
Implement the partition() function used in quickSort().


Example 1:

Input: 
N = 5 
arr[] = { 4, 1, 3, 9, 7}
Output: 1 3 4 7 9


Example 2:

Input:
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10

Your Task: 
You don't need to read input or print anything. Your task is to complete the function partition() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot. 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 103
1 <= arr[i] <= 104

Solution:

#User function Template for python3

def partition(arr,low,high):
    # code here
    tmp = 0
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = tmp
    return i+1
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends

