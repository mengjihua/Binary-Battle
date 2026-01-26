#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int distinctPoints(string s, int k) {
        int n = s.size();

        vector<int> preUD(n + 1), preLR(n + 1);
        preLR[0] = preUD[0] = 0;
        for (int i = 0; i < n; i++) {
            char c = s[i];
            if (c == 'U') {
                preUD[i + 1] = preUD[i] + 1;
                preLR[i + 1] = preLR[i];
            }
            else if (c == 'D') {
                preUD[i + 1] = preUD[i] - 1;
                preLR[i + 1] = preLR[i];
            }
            else if (c == 'L') {
                preLR[i + 1] = preLR[i] - 1;
                preUD[i + 1] = preUD[i];
            }
            else {
                preLR[i + 1] = preLR[i] + 1;
                preUD[i + 1] = preUD[i];
            }
        }

        set<pair<int, int>> st;
        for (int i = 0; i < n - k + 1; i++) {
            st.emplace(preUD[i + k] - preUD[i], preLR[i + k] - preLR[i]);
        }
        return st.size();
    }
};