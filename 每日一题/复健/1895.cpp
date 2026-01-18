#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

// 判断边长为 k 的正方形是否为幻方
bool check(vector<vector<int>>& rowSum, vector<vector<int>>& colSum, vector<vector<int>>& grid, int m, int n, int k){
    for (int i = 0; i <= m - k; i++){
        for (int j = 0; j <= n - k; j++){
            int target = rowSum[i + 1][j + k] - rowSum[i + 1][j];
            bool flag = true;

            for (int x = 0; x < k; x++){
                if (rowSum[i + x + 1][j + k] - rowSum[i + x + 1][j] != target){
                    flag = false;
                    break;
                }
            }
            if (!flag) continue;

            for (int y = 0; y < k; y++){
                if (colSum[i + k][j + y + 1] - colSum[i][j + y + 1] != target){
                    flag = false;
                    break;
                }
            }
            if (!flag) continue;

            int diag1 = 0, diag2 = 0;
            for (int d = 0; d < k; d++){
                diag1 += grid[i + d][j + d];
                diag2 += grid[i + d][j + k - 1 - d];
            }
            if (diag1 != target || diag2 != target) continue;

            return true;
        }
    }
    return false;
}

class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        vector<vector<int>> rowSum(m + 1, vector<int>(n + 1, 0));
        vector<vector<int>> colSum(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                rowSum[i + 1][j + 1] = rowSum[i + 1][j] + grid[i][j];
                colSum[i + 1][j + 1] = colSum[i][j + 1] + grid[i][j];
            }
        }

        int ans = 1;
        for (int k = 2; k <= min(m, n); k++){
            ans = check(rowSum, colSum, grid, m, n, k) ? k : ans;
        }
        return ans;
    }
};