class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int, int> mp;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            mp[nums[i]] = 1; // Mark presence, not frequency
        }

        int maxcount = 0;
        for (auto& pair : mp) { // Iterate over unique keys in the map
            int start = pair.first;
            
            // Only start counting if 'start' is the beginning of a sequence
            if (mp.find(start - 1) == mp.end()) {
                int it = start;
                int count = 0;
                while (mp.find(it) != mp.end()) {
                    count++; // Increment by 1 for each unique consecutive number
                    it++;
                }
                maxcount = max(maxcount, count);
            }
        }

        return maxcount;
    }
};
