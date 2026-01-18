#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int max_side = 0;
        for (int i = 0; i < bottomLeft.size(); i++) {
            auto& b1 = bottomLeft[i];
            auto& t1 = topRight[i];
            for (int j = 0; j < i; j++) {
                auto& b2 = bottomLeft[j];
                auto& t2 = topRight[j];
                int width = min(t1[0], t2[0]) - max(b1[0], b2[0]);
                int height = min(t1[1], t2[1]) - max(b1[1], b2[1]);
                int side = min(width, height);
                max_side = max(max_side, side);
            }
        }
        return (long long)max_side * max_side;
    }
};