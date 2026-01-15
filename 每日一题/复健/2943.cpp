#include <bits/stdc++.h>
using namespace std;


int get_max_consecutive(vector<int>& lst){
    sort(lst.begin(), lst.end());
    int res = 1, cur_len = 1;
    int n = lst.size();
    for (int i = 1; i < n; i++){
        if (lst[i - 1] == lst[i] - 1) cur_len += 1;
        else cur_len = 1;
        res = max(res, cur_len);
    }
    return res;
}


class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        int h_max = get_max_consecutive(hBars);
        int v_max = get_max_consecutive(vBars);
        int side = min(h_max, v_max) + 1;
        return side * side;
    }
};