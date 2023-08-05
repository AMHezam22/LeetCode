// https://leetcode.com/problems/two-sum/

#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
	static vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int,int> my_map;
		for (int i = 0; i < nums.size(); ++i) {
			int current = nums[i];
			int n = target - current;
			if(my_map.find(target-current) != my_map.end()){
				return vector<int> {i,my_map[n]};
			}
			else{
				my_map[current] = i;
			}
		}
		return vector<int>{-1,-1};
		
	}
};