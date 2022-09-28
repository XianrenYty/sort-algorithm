#include<iostream>
#include<vector>
#include<stdlib.h>
#include <time.h>

using namespace std;

int randomized_partition(vector<int>& nums, int l, int r)
{
    int pivot = l + rand() % (r - l + 1);
    int i = l - 1;
    for(int j = l; j < r; ++j){
        if(nums[j] < nums[r]){
            i++;
            swap(nums[i], nums[j]);
        }
    }
    swap(nums[i + 1], nums[r]);
    return i + 1;
}

vector<int> quick_sort(vector<int> &nums, int l, int r)
{
    if(l < r){
        int mid = randomized_partition(nums, l, r);
        quick_sort(nums, l, mid - 1);
        quick_sort(nums, mid + 1, r);
    }
    return nums;
}

int main()
{
    srand((unsigned)time(0));
    vector<int> nums;
    for (int i = 0; i < 10; ++i)
    {
        nums.push_back(rand() % 20);
    }

    for (int i = 0; i < nums.size(); ++i) 
    {
        cout << nums.at(i) << ' ';
    }

    cout << endl;

    nums = quick_sort(nums, 0, nums.size() - 1);
    
    for (int i = 0; i < nums.size(); ++i) 
    {
        cout << nums.at(i) << ' ';
    }
    
    return 0;
}