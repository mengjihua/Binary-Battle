#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int dfs(TreeNode* root) {
            if (!root) return 0;
            int left = dfs(root->left);
            if (left == -1) return -1;
            int right = dfs(root->right);
            if (right == -1) return -1;
            return abs(left - right) > 1 ? -1 : max(left, right) + 1;
    };
public:
    bool isBalanced(TreeNode* root) {
        return dfs(root) != -1;
    }
};