#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

unordered_set<int> findAllSegmentLengths(vector<int>& fences, int limit) {
    fences.insert(fences.begin(), 1);
    fences.push_back(limit);
    unordered_set<int> lengths;
    int len = fences.size();
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            lengths.insert(fences[j] - fences[i]);
        }
    }
    return lengths;
}


class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        sort(hFences.begin(), hFences.end()), sort(vFences.begin(), vFences.end());
        unordered_set<int> hLengths = findAllSegmentLengths(hFences, m);
        unordered_set<int> vLengths = findAllSegmentLengths(vFences, n);
        
        long long ans = -1;
        for (int hLen: hLengths) {
            // cout << hLen << endl;
            if (vLengths.count(hLen)) {
                ans = max(ans, (long long)hLen * hLen);
            }
        }
        return ans % MOD;
    }
};