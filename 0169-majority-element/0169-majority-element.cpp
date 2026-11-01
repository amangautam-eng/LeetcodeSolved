class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> mp;
        int n=nums.size();
        for(int i=0;i<n;i++){
            auto it=mp.find(nums[i]);

            if(it!=mp.end()){
                mp[nums[i]]+=1;
            }
            else{
                mp[nums[i]]=1;
            }
        }
        for (auto i:mp){
            if(i.second > n/2){
                return i.first;
            }
        }

        return 0;
    }
};