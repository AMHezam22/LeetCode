// https://leetcode.com/problems/binary-search/

#include <iostream>
#include "bits/stdc++.h"

#define mid(a, b) ((a+b)/2)
using namespace std;

class Solution {
public:
	vector <int> arr;
	
	int binary_search(int left, int right, int target) {
		while (true) {
			if (left > right || right < left)return -1;
			int mid = mid(left, right);
			if (arr[mid] == target)return mid;
			else if (arr[mid] < target)left = mid + 1;
			else right = mid - 1;
			
		}
	}
	
	int search(vector <int> &nums, int target) {
		arr = nums;
		return binary_search(0, arr.size() - 1, target);
	}
};
