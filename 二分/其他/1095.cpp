
// This is the MountainArray's API interface.
// You should not implement it, or speculate about its implementation
class MountainArray {
  public:
    int get(int index);
    int length();
};


class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        
        int l = 1, r = n - 2;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        if (mountainArr.get(l) == target) return l;

        auto search = [&](int l, int r, bool asc) {
            while (l <= r) {
                int mid = l + (r - l) / 2;
                int num = mountainArr.get(mid);
                if (num == target) return mid;
                if (asc ^ (num < target)) r = mid - 1;
                else l = mid + 1;
            }
            return -1;
        };

        int left = search(0, l - 1, true);
        return left != -1 ? left : search(l + 1, n - 1, false);
    }
};