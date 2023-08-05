#include <iostream>
#include "bits/stdc++.h"
using namespace std;

class Solution{
public:
	int getLong(string text){
		unordered_set<char> s;
		for (auto i : text) {
			if(s.find(i) != s.end()){
				return s.size();
			}
			else{
				s.insert(i);
			}
		}
		return s.size();
	}
	int lengthOfLongestSubstring(string text){
		int longest = 0;
		for (int i = 0; i < text.length(); ++i) {
			longest = max(longest, getLong(text.substr(i)));
		}
		return longest;
	}
};