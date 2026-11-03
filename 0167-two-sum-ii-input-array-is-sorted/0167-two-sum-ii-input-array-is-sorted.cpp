class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        unordered_map<int,int> mp;
        int n=numbers.size();
        for (int i=0;i<n;i++){
            if(mp.find(target-numbers[i]) != mp.end()){
                return {mp[target-numbers[i]],i+1};

            }
            else{
                mp[numbers[i]]=i+1;
            }
        }

        return {};
    }
};