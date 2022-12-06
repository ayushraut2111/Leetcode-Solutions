// https://leetcode.com/problems/kth-largest-element-in-an-array/
#include<bits/stdc++.h>
#define ll long long
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int,vector<int>,greater<int>>pq;
        for(int i=0;i<k;i++)
        {
            pq.push(nums[i]);
        }
        for(int i=k;i<nums.size();i++)
        {
            pq.push(nums[i]);
            pq.pop();
        }
        return pq.top();
    }
};
int main()
{
    
}