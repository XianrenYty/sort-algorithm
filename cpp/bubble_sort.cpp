#include<iostream>
#include<vector>
#include<stdlib.h>

using namespace std;

vector<int> bubbleSort(vector<int> &nums)
{
    int n = nums.size();
    for (int i = 0; i < nums.size() - 1; ++i){
        for (int j = 0; j < nums.size() - i - 1; ++j) {
            if (nums.at(j) > nums.at(j + 1)){
                swap(nums[j], nums[j + 1]);
            }
        }
    }
    return nums;
}

int main()
{
    srand((unsigned)time(NULL));
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

    nums = bubbleSort(nums);
    
    for (int i = 0; i < nums.size(); ++i) 
    {
        cout << nums.at(i) << ' ';
    }
    
    return 0;
}