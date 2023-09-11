#include <iostream>
#include <set>
#include <vector>

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        set<int> ans;
        for (int i : nums)
        {
            ans.insert(i);
        }
        if (ans.size() == nums.size())
            return false;
        return true;
    }
}

int
main()
{
    return 0;
}