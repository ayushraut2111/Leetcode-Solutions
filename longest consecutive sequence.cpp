// https://leetcode.com/problems/longest-consecutive-sequence/
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    
}
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)
        return 0;
        priority_queue <int, vector<int>, greater<int> > pq;
       
        set<int>s;
        for(auto x: nums)s.insert(x);
        if (s.size()==1)
        return 1;
        for(auto x: s)pq.push(x);
        int ans=-1;
        int count=1;
        while(!pq.empty())
        {
            cout<<pq.top();
            if (s.find(pq.top()+1)!=s.end())
            {count+=1;
            ans=max(ans,count);}
            else
            {
                ans=max(ans,count);
                count=1;
            }
            pq.pop();
        }
       
        return ans;
        
    }
};