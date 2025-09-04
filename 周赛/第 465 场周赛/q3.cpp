#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        // 计算所有数中最大值的二进制位数
        int max_val = *max_element(nums.begin(), nums.end());
        int w = 0;
        int temp = max_val;
        while (temp) {
            w++;
            temp >>= 1;
        }
        // 如果 max_val 是 0，w 会是 0，但至少需要 1 位
        if (max_val == 0) w = 1;

        int u = 1 << w; // 即 2^w
        vector<int> f(u, 0); // f[s] 表示能由 s 的子集构成的原始数的最大值

        // 初始化：每个数字本身
        for (int x : nums) {
            f[x] = x;
        }

        // 标准的 SOS DP：枚举所有集合 s，从小到大
        for (int s = 0; s < u; s++) {
            for (int i = 0; i < w; i++) {
                if (s >> i & 1) { // 如果第 i 位为 1
                    f[s] = max(f[s], f[s ^ (1 << i)]); // 从 s 去掉第 i 位转移
                }
            }
        }

        // 枚举每个数 x，找与其无公共 1 位的最大 f[~x]
        long long ans = 0;
        for (int x : nums) {
            int complement = (u - 1) ^ x; // 取反，限制在 w 位内
            ans = max(ans, (long long)x * f[complement]);
        }

        return ans;
    }
};