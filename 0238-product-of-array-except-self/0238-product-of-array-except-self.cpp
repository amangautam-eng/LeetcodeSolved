class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod=1,cnt=0,n=nums.size();
        vector<int> ans(n,0);
        

        for(int i=0;i<n;i++){
            if(nums[i]==0){
                cnt++;
            }
            else{
                prod*=nums[i];
            }

        }
        if (cnt>1) return ans;
        if (cnt==1){
            for(int i=0;i<n;i++){
                if (nums[i]==0){
                    ans[i]=prod;
                }
            }
        }
        else{
            for (int i=0;i<n;i++){
                ans[i]=prod/nums[i];
            }
        }

        return ans;
        

    }
};