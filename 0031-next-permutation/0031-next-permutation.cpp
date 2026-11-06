class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n=nums.size()-1;
        int r=n;

        while(r>0 && nums[r-1]>=nums[r]){
            r--;
        }
        if (r==0) return sort(nums.begin(),nums.end());
        int idx=n;
        while(idx>r-1){
            if(nums[idx]>nums[r-1]){
                swap(nums[idx],nums[r-1]);
                break;
            }
            idx--;
        }
        sort(nums.begin()+r,nums.end());



    }

};